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

Pins = piezo.init_piezo()                   #initialization of the GPIO Pins list
piezo.setup_piezo(Pins)                     #set pin in Pins list as an output
 
notes=[262,294,330]         #list of notes frequencies       
durations=[0.5,0.5,0.5]     #list of time durations



#Image

images_paths = ["/home/mborot/Pictures/mont_blanc.jpg", "/home/mborot/Pictures/cervin.jpg", "/home/mborot/Pictures/Eiger.jpg", "/home/mborot/Pictures/mont_cenis.jpg"]              #list of images paths

#image = Image.open("/home/mborot/Pictures/mont_blanc.jpg")
#image.show()


# TKINTER

root = tk.Tk()                                                              #Tinker window creation
root.title("Images display")

frame = tk.Frame(root)                                                      #Frame creation
frame.pack()

lbl = tk.Label(frame, text="Image 1", bg="lavender")                        #Label creation
lbl.grid(row=1, column=1)                                                   #Label position in the frame

btn_prev = tk.Button(frame, text="Prev")                                    #Button "Previous" creation
btn_prev.grid(row=1, column=0)                                              #Button "Prev" position in the frame

btn_next = tk.Button(frame, text="Next")                                    #Button "Next" creation
btn_next.grid(row=1, column=2)                                              #Button "Next" position in the frame


images_tk = display.convert(images_paths)                                                                                                                                            #list of uploaded of ImageTk.PhotoImage objects = images



image_index=0                                                               #index of the image in the images_tk list that we want to display                                                        
##display.show_image_tk(frame, images_tk, image_index)                        #Tkinter display of the image that corresponds to the image_index in the images_tk list
##root.mainloop()



# MATPLOTLIB

# create figure 
fig = plt.figure(figsize=(8, 8)) 

# setting values to rows and column variables 
rows = 2
columns = 2

n=len(images_paths)
i=0

while i <= n-1:

    display.show_image_mpl(images_paths, i, columns, rows)
    magnet.coil(Magnet, t1, t2)
    piezo.play3()
    i += 1
 


# MAIN

""" 
i = 0                                                                        #index of loop
z = 3                                                                       #number of loops
 

while i <= z :
    display.show_image(frame, images_tk, i)                                 #display in the frame of the image that corresponds ton the image_index = i in the images_tk list
    #piezo.play1(Pins,notes,durations)
    magnet.coil(Magnet, t1, t2)
    piezo.play3()
    i += 1
"""



GPIO.cleanup()                              #clean up all the ports used in the program