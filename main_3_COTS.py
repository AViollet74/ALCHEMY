import functions.function_display as display
import functions.function_UV as uv
import functions.function_photosensor as sensor
import functions.function_motor as motor
import functions.function_vibration as vibration


from gpiozero import LED
from time import sleep
import tkinter as tk 
from screeninfo import get_monitors
import sys
from time import time

import os

################################################################################################################################
### Object properties 
print("Object properties")
origin_path = "/home/alchemy/PRINT/"
origin_path_layers="/home/alchemy/LAYERS" 
file_name=input("Name of the folder containing images (Need to be stored in PRINTS)")
base_path=origin_path + file_name                                                                       #Folder path   
black_image_path = "/home/alchemy/black_image.png"                                                      #Black image path

sequence = sorted(os.listdir(base_path), key=lambda x: int(x.split('.')[0]))
sequence= [os.path.join(base_path,name) for name in sequence]
nb_layers = len([f for f in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, f))])       
layers_state_path = f"/home/alchemy/LAYERS/{file_name}.txt"                                             #file containing the layer's state of the print
try:
    with open(layers_state_path, "r") as f:
        # Read all lines from the file and strip any extra whitespace or newlines
        layers_state_values = [int(line.strip()) for line in f.readlines()]
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Control that the numbre of layers are matching
if nb_layers!=len(layers_state_values):
    print(f"number of layer not consistent: {nb_layers} in print and {len(layers_state_values)} in layer definition")
    sys.exit("error")
else :
    pass

# Layer thickness definition
layer_thickness=(input("layer thickness in mm (ENTER for default value(0.08))"))
if not layer_thickness:
    layer_thickness=0.08
else :
    layer_thickness=float(layer_thickness)
layer_index=0                                                                                           #Determines the current layer
Particles_state=1                                                                                       #Determines if the particles are dispersed or not (initial state : dispersed particle) 

################################################################################################################################




################################################################################################################################### 
### Initialisation of the hardware components (GPIO pins assignation)

#Motor magnets 
l_container=(input("size of resin container in mm (default value 72mm)"))
if not l_container:
    l_container=72
else:
    l_container=float(l_container)
# while True:
response = input("rotate lead screw to place Magnet and press ENTER").strip().lower()
print("Magnets setting success")

# Dispersion elements - vibration motors
motors, time_on=vibration.init_vibration()
vibration.setup_vibration(motors)
print("Vibration motors setup success")


#UV ligth
uv_pin = uv.init_uv()
print("UV light setup success")

#Photoelctric sensor
sensor_pin = sensor.init_sensor()                                                                                                                                                                                                                #le setup GPIO qui va faire fonctionner le sensor est présente dans la fontion start_position_1(sensor_pin)
print("photo sensor setup success")

#GUI creation with TkInter 
for m in get_monitors():
    print("INFO", str(m))

monitors = get_monitors()
monitor=display.name_selection('HDMI-1')                                                                # port for the LCD screen
x_shift = monitor.x
y_shift = monitor.y
w_root = monitor.width
h_root = monitor.height

root = tk.Tk()                                                                                          #Tinker window creation
root.attributes('-fullscreen', True)
root.geometry(f"{w_root}x{h_root}+{x_shift}+{y_shift}")                                                 #Create a root with width=w_root, heigth=h_root, shifted by x_shift from the left and y_shift from the top of the monitor

cnv = tk.Canvas(root, bg="black", highlightthickness=0)
cnv.pack(fill=tk.BOTH, expand=True)

################################################################################################################################


################################################################################################################################
###Conversion of the images paths to Image Objects
black_image_tk  = display.convert_full_0(black_image_path, w_root, h_root, monitors)                    #Convert black image path to black image object, with full screen dimensions                                         
image_paths = display.convert_list(base_path, nb_layers)
# images_tk = display.convert_full_1(sequence, w_root, h_root, monitors)                                #Too demanding for memory, leads to drop in performance for high number of layers
subset_imagetk=1
################################################################################################################################

################################################################################################################################
### MAIN PRINTING
## Initialization and zero position of the printing bed
while True:
    response = input("Is 0-position set? (yes/no): ").strip().lower()
    if response == "yes":
        motor.start_position_1(sensor_pin)
        Z_table_pos=0
        break
    elif response == "no":
        print("setting")
        motor.start_position_1(sensor_pin)                                                               # go down to the screen
        Z_table_pos=0
        input("After settting: Press Enter to continue...")
        break
    else:
       pass

sleep(2)

## Start MAIN 
for j in range(0,nb_layers, subset_imagetk):                                                            # double loop over the image objects can be used to improve performance of the printer by creating a subset of image objects each time
    images_tk=display.convert_full_1(sequence[j:j+subset_imagetk], w_root, h_root, monitors)            # by default, size of subset of image objects i set to 1
    for i in range(len(images_tk)): 
        start_time=time()
        percentage=(i+j)/nb_layers*100
        print(f"printing layer {i+j}_________________________________{percentage:.1f}% Complete")
        motor.move_dist_dir_1(2,1)
        sleep(3)
        motor.move_dist_dir_1(2-layer_thickness,-1)
        sleep(2)
        # motor.move_dist_dir_1(layer_thickness,1)

        Z_table_pos+=layer_thickness
        layer_index+=1
        
        display.show_image(cnv, w_root, h_root, black_image_tk)
        root.update_idletasks()
        root.update()


        ##  PARTICLES ACTUATION IN THE CONTAINER      
        if layer_index<=3:
            cure_time =60                                                                           # 12 for commercial resin, 96 for custom resin 1, 
        else:
            cure_time=24                                                                            # 2.8 for commercial resin, 25 for custom resin 1, 
        attract_time =60                                                                              #time in seconds
        vibration_time=300
    ##  PARTICLES ACTUATION IN THE CONTAINER
    #Consider state of particles and compare to instructions
        if layers_state_values[layer_index] != Particles_state:
            motor.move_dist_dir_1(24, 1)                                                            #Move table up to empty the contianer       
            sleep(2)
            if Particles_state==1:
                motor.move_dist_dir_2((210/2+l_container/2),1)                                      #Move to the other size of the resin container
                sleep(attract_time)                                                                 #Time to slepp to gather particlesto side
                temp_position=0
                while temp_position<l_container:                                                    #Back and forth movement to gather most of the particles with the magnet
                    motor.move_dist_dir_2(9,-1)
                    sleep(attract_time)
                    motor.move_dist_dir_2(3,1)
                    sleep(attract_time)
                    temp_position+=6
                    
            else:
                # motor.move_dist_dir_2((210/2+l_container/2)/4,-1)
                motor.move_dist_dir_2((210/2+l_container/2-l_container),-1)
                sleep(2)      
                vibration.activate_v(motors, vibration_time)                                                   # 200s of agitation
                Particles_state=1    

            motor.move_dist_dir_1(24, -1 )                                                            #Move table down to initial position  
            pass



        uv.switch_on(uv_pin)
        display.show_image(cnv, w_root, h_root, images_tk[i])
        root.update_idletasks()
        root.update()
        sleep(cure_time)
        uv.switch_off(uv_pin)
        sleep(2)


        end_time=time()
        delta_time=end_time-start_time
        print(f"deltatime={delta_time} seconds")


        if i == len(images_tk)-1:
            display.show_image(cnv, w_root, h_root, black_image_tk)        
            root.update_idletasks()
            root.update()
            print("End of the printing")
            root.bind('<Escape>', lambda e: root.quit())   
        else:
            pass



root.mainloop()








