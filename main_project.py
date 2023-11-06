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
root.attributes('-fullscreen', True)
#root.title("Images display")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()


frame = tk.Frame(root)                                                      #Frame creation
frame.pack()



#Image

#black_image_path = "/Users/borotmarion/Documents/EPFL - MA/MA4/Project_ALCHEMY/black_image.png"                                                                                #Number of the last png image  

#images_paths = ["/home/mborot/Pictures/mont_blanc.jpg", "/home/mborot/Pictures/cervin.jpg", "/home/mborot/Pictures/Eiger.jpg", "/home/mborot/Pictures/mont_cenis.jpg"]              #list of images paths
#images_tk, image_names = display.convert(images_paths)  


base_path = "/home/mborot/Pictures/"

black_image_path = "/home/mborot/Pictures/black.jpg"
black_image_tk  = display.full_convert_0(black_image_path, w, h)                                                    #full screen
#black_image_tk  = display.convert_0(black_image_path)


sequence=[base_path+"cubic_layer_0.png", base_path+"cubic_layer_1.png", base_path+"cubic_layer_0.png"]
layers_tk = display.full_convert_1(sequence, w, h)                                                                      #full screen
#layers_tk = display.convert_1(sequence)


layers = [3, 4, 3]   #number of layer, e.g: 3 times layer 0, then 4 times layer 1 and finally 3 times layer 2

display.show_image_tk_0(root, layers_tk[0])
root.update_idletasks()
root.update()

#To exit the application by pressing Escape
root.bind('<Escape>', lambda e: root.quit())

"""
for i in range(0, len(layers)):

    for k in range(0, layers[i]):

        #display.show_image_tk_0(root, black_image_tk)       
        #root.update_idletasks()
        #root.update()
        
        #sleep(2)

        magnet.coil(Magnet, t1, t2)

        #sleep(2)

        piezo.play1(pins, notes, durations)
        #piezo.play3()

        #sleep(2)

        display.show_image_tk_0(root, layers_tk[i])          
        root.update_idletasks()
        root.update()

        sleep(4)

"""







"""
#Iteration over layers and layers_tk

for i in range(0, len(layers)):

    for k in range(0, layers[i]):

        display.show_image_tk_1(frame, black_image_tk)
        root.update_idletasks()
        root.update()
        
        sleep(2)

        magnet.coil(Magnet, t1, t2)

        sleep(2)

        piezo.play1(pins, notes, durations)
        #piezo.play3()

        sleep(2)

        display.show_image_tk_1(frame, layers_tk[i])
        root.update_idletasks()
        root.update()

        sleep(2)
"""




GPIO.cleanup()                              #clean up all the ports used in the program

root.mainloop()