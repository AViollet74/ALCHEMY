from PyQt5.QtWidgets import QApplication
import sys
import prusa_slicer

def slice_stl(input_stl, output_folder):
    app = QApplication(sys.argv)
    
    # Create a PrusaSlicer instance
    slicer = prusa_slicer.PrusaSlicer()
    
    # Load an STL file
    slicer.run_command(f"Load Model...|{input_stl}")
    
    # Configure slicing settings (e.g., layer height, print quality, etc.)
    # You can customize these settings as needed
    slicer.run_command("Layer height...|0.2")
    
    # Set the output folder
    slicer.run_command(f"Output filename...|{output_folder}/output.gcode")
    
    # Slice the model
    slicer.run_command("Slice Now")
    
    # Export 2D images (JPG) from the sliced model
    slicer.run_command(f"Export G-code...|{output_folder}/output.gcode")
    
    # Quit the application
    slicer.run_command("Exit")

if __name__ == '__main__':
    input_stl = "/Users/borotmarion/Documents/EPFL - MA/MA4/22Lattice-TPL.stl"
    output_folder = "/Users/borotmarion/Documents/EPFL - MA/MA4/Project_ALCHEMY/sliced_png"
    slice_stl(input_stl, output_folder)
