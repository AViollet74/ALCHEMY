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



#Image

images_paths = ["/home/mborot/Pictures/mont_blanc.jpg", "/home/mborot/Pictures/cervin.jpg", "/home/mborot/Pictures/Eiger.jpg", "/home/mborot/Pictures/mont_cenis.jpg"]              #list of images paths
black_image_path = "/home/mborot/Pictures/black.jpg"

#image = Image.open("/home/mborot/Pictures/mont_blanc.jpg")
#image.show()


# TKINTER

root = tk.Tk()                                                              #Tinker window creation
root.title("Images display")

frame = tk.Frame(root)                                                      #Frame creation
frame.pack()

images_tk, image_names = display.convert(images_paths)                                                                                                                                            #list of uploaded of ImageTk.PhotoImage objects = images
black_image_tk  = display.convert_black_image(black_image_path)



# MATPLOTLIB

# create figure 
#fig = plt.figure(figsize=(8, 8)) 

# setting values to rows and column variables 
#rows = 2
#columns = 2



for i in range(len(images_tk)):

    #display.show_image_mpl(images_paths, i, columns, rows)
    display.show_black_image_tk(frame, black_image_tk)
    root.update_idletasks()
    root.update()
    sleep(2)
    magnet.coil(Magnet, t1, t2)
    piezo.play1(pins, notes, durations)
    sleep(2)
    display.show_image_tk(frame, images_tk[i], image_names[i])
    root.update_idletasks()
    root.update()    
    sleep(2)
    #piezo.play3()

 





GPIO.cleanup()                              #clean up all the ports used in the program
last_i = len(images_tk) - 1
image_class = display.ImageSelector(frame, last_i, images_tk, image_names)
image_class.show_last_image_tk(images_tk[last_i], image_names[last_i])
root.mainloop()