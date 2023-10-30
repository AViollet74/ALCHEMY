import functions.function_magnet as magnet
import functions.function_piezo as piezo
import functions.function_display as display

import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep
import tkinter as tk 
import numpy as np
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread



GPIO.setwarnings(False)                     #prevents warnings from showing up when you run the code
GPIO.setmode(GPIO.BCM)                      #BCM = Broadcom chip-specific pin numbers


#Grove_Electromagnet 

Magnet, t1, t2 = magnet.init_magnet()        #initialization of the GPIO Magnet list and rest time for magnet on (t1) and magnet off (t2)
magnet.setup_magnet(Magnet)                  #set pin in Magnet list as an output


#Piezo elements

pins = piezo.init_piezo()                   #initialization of the GPIO pins list
piezo.setup_piezo(pins)                     #set pin in pins list as an output
 
notes=[262,294,330]         #list of notes frequencies       
durations=[0.5,0.5,0.5]     #list of time durations


# TKINTER

root = tk.Tk()                                                              #Tinker window creation
root.title("Images display")

frame = tk.Frame(root)                                                      #Frame creation
frame.pack()


#Image

#images_paths = ["/home/mborot/Pictures/mont_blanc.jpg", "/home/mborot/Pictures/cervin.jpg", "/home/mborot/Pictures/Eiger.jpg", "/home/mborot/Pictures/mont_cenis.jpg"]              #list of images paths
#black_image_path = "/Users/borotmarion/Documents/EPFL - MA/MA4/Project_ALCHEMY/black_image.png"

black_image_path = "/home/mborot/Pictures/black.jpg"
layer_0_path = "/home/mborot/Pictures/cubic_layer_0.png"
layer_1_path = "/home/mborot/Pictures/cubic_layer_1.png"
layer_2_path = "/home/mborot/Pictures/cubic_layer_0.png"

#nb_slice = 26                                                                                       #Number of the last png image  

black_image_tk  = display.convert_single_image(black_image_path)
layer_0_tk = display.convert_single_image(layer_0_path)
layer_1_tk = display.convert_single_image(layer_1_path)
layer_2_tk = display.convert_single_image(layer_2_path)

#png_paths = display.convert_png(nb_slice)
#png_tk, image_names = display.convert(png_paths) 
#images_tk, image_names = display.convert(images_paths)  

nb_layer_0 = 3
nb_layer_1 = 4
nb_layer_2 = 3

nb_layers = [3, 4, 3]   #number of layer, e.g: 3 times layer 0, then 4 times layer 1 and finally 3 times layer 2


for i in nb_layers:

    layer_tk = []
    

    for k in range(nb_layers[i]):
        
        display.show_single_image_tk(frame, black_image_tk)
        root.update_idletasks()
        root.update()
        
        sleep(2)

        magnet.coil(Magnet, t1, t2)
        piezo.play1(pins, notes, durations)
        #piezo.play3()

        sleep(1)

        display.show_single_image_tk(frame, layer_0_tk)
        root.update_idletasks()
        root.update()

        sleep(2)
        

"""
for i in range(len(png_tk)):

    display.show_single_image_tk(frame, black_image_tk)
    root.update_idletasks()
    root.update()

    sleep(2)

    magnet.coil(Magnet, t1, t2)
    piezo.play1(pins, notes, durations)

    sleep(0.5)

    display.show_image_tk(frame, png_tk[i], image_names[i])
    root.update_idletasks()
    root.update()

    sleep(2)
    #piezo.play3()
"""


 

GPIO.cleanup()                              #clean up all the ports used in the program

#Show last image with Buttons

#last_i = len(png_tk) - 1
#image_class = display.ImageSelector(frame, last_i, png_tk, image_names)
#image_class.show_last_image_tk(png_tk[last_i], image_names[last_i])

root.mainloop()