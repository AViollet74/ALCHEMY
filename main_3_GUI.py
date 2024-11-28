import tkinter as tk
from tkinter import messagebox
from gpiozero import LED
from time import sleep
from screeninfo import get_monitors
import os

# Import your custom functions
import functions.function_display as display
import functions.function_UV as uv
import functions.function_photosensor as sensor
import functions.function_motor as motor
import functions.function_vibration as vibration

class PrinterApp:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg="black")

        # Initialize state variables
        self.Z_table_pos = 0
        self.Particles_state = 1  # 1 = dispersed, 0 = not dispersed
        self.layer_index = 0

        # Paths
        self.origin_path = "/home/alchemy/PRINT/"
        self.black_image_path = "/home/alchemy/black_image.png"
        self.file_name = "example_print_folder"  # Replace with dynamic input if needed
        self.base_path = os.path.join(self.origin_path, self.file_name)
        self.layer_thickness = 0.2  # Default layer thickness

        # Image placeholders
        self.images_tk = []
        self.black_image_tk = None
        self.layers_state_values = []

        # Create GUI elements
        self.create_widgets()

        # Initialize hardware components
        self.init_hardware()

    def create_widgets(self):
        """Create the graphical user interface."""
        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Stop button
        self.stop_button = tk.Button(self.root, text="Stop", bg="red", fg="white",
                                     font=("Arial", 20), command=self.stop_process)
        self.stop_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

        # Status label
        self.status_label = tk.Label(self.root, text="Status: Ready", bg="black", fg="white",
                                     font=("Arial", 18))
        self.status_label.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        # Z-table position label
        self.z_table_label = tk.Label(self.root, text="Z-table Position: 0.00 mm", bg="black",
                                      fg="white", font=("Arial", 18))
        self.z_table_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def init_hardware(self):
        """Initialize all hardware components."""
        self.update_status("Initializing hardware...")
        try:
            # UV light
            self.uv_pin = uv.init_uv()

            # Photoelectric sensor
            self.sensor_pin = sensor.init_sensor()

            # Vibration motors
            self.motors, self.time_on = vibration.init_vibration()
            vibration.setup_vibration(self.motors)

            self.update_status("Hardware initialized.")
        except Exception as e:
            self.update_status(f"Hardware initialization failed: {e}")

    def update_status(self, status_text):
        """Update the status label."""
        self.status_label.config(text=f"Status: {status_text}")
        self.root.update_idletasks()

    def update_z_table_position(self):
        """Update the Z-table position display."""
        self.z_table_label.config(text=f"Z-table Position: {self.Z_table_pos:.2f} mm")
        self.root.update_idletasks()

    def stop_process(self):
        """Stop the printing process."""
        self.update_status("Stopping...")
        uv.switch_off(self.uv_pin)
        motor.stop_all()
        vibration.stop_vibration(self.motors)
        self.update_status("Stopped.")
        messagebox.showinfo("Process Stopped", "The printing process has been stopped.")
        self.root.quit()

    def load_images_and_states(self):
        """Load images and layer state values."""
        self.update_status("Loading images and states...")
        try:
            # Load black image
            monitors = get_monitors()
            self.black_image_tk = display.convert_full_0(
                self.black_image_path, monitors[0].width, monitors[0].height, monitors)

            # Load sequence
            sequence = sorted(os.listdir(self.base_path), key=lambda x: int(x.split('.')[0]))
            self.images_tk = display.convert_full_1(sequence, monitors[0].width, monitors[0].height, monitors)

            # Load layer state values
            layers_state_path = f"/home/alchemy/LAYERS/{self.file_name}.txt"
            with open(layers_state_path, "r") as f:
                self.layers_state_values = [int(line.strip()) for line in f.readlines()]
        except Exception as e:
            self.update_status(f"Error loading data: {e}")
            raise

    def start_printing(self):
        """Start the main printing process."""
        try:
            # Load images and states
            self.load_images_and_states()

            # Ensure 0-position is set
            self.update_status("Setting 0-position...")
            motor.start_position_1(self.sensor_pin)
            self.Z_table_pos = 0
            self.update_z_table_position()

            # Start printing layers
            for i, image_tk in enumerate(self.images_tk):
                self.update_status(f"Printing layer {i+1}/{len(self.images_tk)}")

                # Move Z-table
                motor.move_dist_dir_1(self.layer_thickness, 1)  # Move down by layer thickness
                self.Z_table_pos += self.layer_thickness
                self.update_z_table_position()

                # Show black image (optional step for clearing)
                display.show_image(self.canvas, get_monitors()[0].width, get_monitors()[0].height, self.black_image_tk)
                self.root.update_idletasks()

                # UV light exposure
                uv.switch_on(self.uv_pin)
                display.show_image(self.canvas, get_monitors()[0].width, get_monitors()[0].height, image_tk)
                self.root.update_idletasks()
                sleep(4)  # Adjust polymerization time
                uv.switch_off(self.uv_pin)

            # Printing completed
            self.update_status("Printing completed.")
            display.show_image(self.canvas, get_monitors()[0].width, get_monitors()[0].height, self.black_image_tk)
            self.root.update_idletasks()
            messagebox.showinfo("Process Completed", "Printing process finished successfully.")
        except Exception as e:
            self.update_status(f"Error: {e}")
        finally:
            self.update_status("Process stopped.")

def main():
    # Set up the root window
    monitors = get_monitors()
    primary_monitor = monitors[0]
    w_root = primary_monitor.width
    h_root = primary_monitor.height

    root = tk.Tk()
    root.geometry(f"{w_root}x{h_root}")

    app = PrinterApp(root)
    app.start_printing()

    root.mainloop()

if __name__ == "__main__":
    main()
