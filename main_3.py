#import functions.function_magnet as magnet
import functions.function_piezo as piezo
import functions.function_display as display
import functions.function_UV as uv
import functions.function_photosensor as sensor
import functions.function_motor as motor


import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep
import tkinter as tk 
from screeninfo import get_monitors

import os
import random

#Images definition
print("Object properties")
#filename=input("name of folder containing images")
base_path = "/home/mborot/Pictures/lattice/"                                                            #Folder path
black_image_path = "/home/mborot/Pictures/black_image.png"                                              #Black image path
sequence=[base_path+"cubic_layer_0.png", base_path+"cubic_layer_1.png", base_path+"cubic_layer_0.png"]  #List of image paths 
nb_layers = len([f for f in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, f))])


                    #layers_state_path = "/home/mborot/Print/layers.txt" #to be defined how the layer and presence of particles will be chosen 
                    #layers_state_values=open(layers_state_path, "r")
layers_state_values = [random.choice([0, 1]) for _ in range(nb_layers)]




layer_thickness=input("layer thickness in mm")
layer_index=0                           #Determines the current layer level
Particles_state=1                       #Determines if the particles are dispersed or not

#Motor
# kit = MotorKit(i2c=board.I2C())       #useless
#step_nb = 500                          #useless


#GPIO settings
GPIO.setwarnings(False)                                                                                 #prevents warnings from showing up when you run the code
GPIO.setmode(GPIO.BCM)                                                                                  #BCM = Broadcom chip-specific pin numbers


#Initialisation of the hardware components (GPIO pins assignation)

#Motor magnets 
l_container=input("size of resin container in mm")
while True:
    response = input("Are magnets well positioned ? (yes/no): ").strip().lower()
    if response == "yes":
        break
    elif response == "no":
        distance=input("What distance from side in mm?")
        time=distance*0.25 #-> 4mm par seconde
        motor.move_dist_time_dir_2(distance, time, 1)
    else:
       pass
print("Magnets setting success")

#Piezo elements - Transducers
piezos, p_time_on, frequency = piezo.init_piezo()                   
piezo.setup_piezo(piezos)     
print("Piezo setup succes") 

#UV ligth
uv_pin = uv.init_uv()
print("UV light setup success")

#Photoelctric sensor
sensor_pin = sensor.init_sensor()
GPIO.setup(sensor_pin, GPIO.IN)
print("photo sensor setup success")

#GUI creation with TkInter 

"""
#Uncomment to get information on monitors
for m in get_monitors():
    print(str(m))
"""

monitors = get_monitors()
print(type(monitors))

if len(monitors) > 1:   
    for monitor in monitors:
        if monitor.is_primary == False:
            x_shift = monitor.x
            y_shift = monitor.y
            w_root = monitor.width
            h_root = monitor.height
else:
    for monitor in monitors:
        x_shift = monitor.x
        y_shift = monitor.y
        w_root = monitor.width
        h_root = monitor.height



root = tk.Tk()                                                                                          #Tinker window creation
root.attributes('-fullscreen', True)
root.geometry(f"{w_root}x{h_root}+{x_shift}+{y_shift}")                                                 #Create a root with width=w_root, heigth=h_root, shifted by x_shift from the left and y_shift from the top of the monitor

cnv = tk.Canvas(root, bg="black", highlightthickness=0)
cnv.pack(fill=tk.BOTH, expand=True)


#Conversion of the images paths to Image Objects
black_image_tk  = display.convert_full_0(black_image_path, w_root, h_root, monitors)                              #Convert black image path to black image object, with full screen dimensions                                         
image_paths = display.convert_list(base_path, nb_layers)
images_tk = display.convert_full_1(sequence, w_root, h_root, monitors)     



#MAIN

#motor.start_position(sensor_pin)

## Initialization and zero position of the printing bed
while True:
    response = input("Is 0-position set? (yes/no): ").strip().lower()
    
    if response == "yes":
        break
    elif response == "no":
        print("setting")
        #add code to setup the zero position of the bed
        motor.start_position_1(sensor_pin)
        Z_table_pos=0
        ##descente jusq'à éteindre le sensor 
        input("Press Enter to continue...")
        ## go back to top position of the bed
        
        break
    else:
       pass

## Start main 
init_position=200 #mm from zero


for i in range(len(images_tk)):
    #move ztable by 1 layer thickness
    motor.move_dist_time_dir_1(layer_thickness, layer_thickness/10, 1) 
    Z_table_pos+=layer_thickness
    layer_index+=1

    display.show_image(cnv, w_root, h_root, black_image_tk)
    root.update_idletasks()
    root.update()



    ##  PARTICLES ACTUATION IN THE CONTAINER
    #study state of particles and compare to instructions
    if layers_state_values[layer_index] != Particles_state:
        motor.move_dist_time_dir_1(50,50/10, 1 )        #Move table up to empty the contianer
        
        if Particles_state==1:
            motor.move_dist_time_dir_2(260/2+l_container/2, (260/2+l_container/2)/10,1)
            #motor.move_dist_time_dir_2(220, 220/10,-1)
            Particles_state=0
        else:
            motor.move_dist_time_dir_2(260/2+l_container/2, (260/2+l_container/2)/10,-1)
            sleep(2)            
            piezo.activate_p(piezos, p_time_on, frequency)
            Particles_state=1
            
        motor.move_dist_time_dir_1(50,50/10, -1 )       #Move table down to initial position
        

    uv.switch_on(uv_pin)
    display.show_image(cnv, w_root, h_root, images_tk[i])
    root.update_idletasks()
    root.update()
    sleep(4)            #Time to polymerize layer tbd by using Jacob's equation
    uv.switch_off(uv_pin)


    if i == len(images_tk)-1:
        display.show_image(cnv, w_root, h_root, black_image_tk)        
        root.update_idletasks()
        root.update()

        print("End of the printing")
        root.bind('<Escape>', lambda e: root.quit())
        
    else:
        pass



#Clean up all the ports used in the program
GPIO.cleanup()                              

root.mainloop()








