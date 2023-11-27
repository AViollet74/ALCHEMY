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
from screeninfo import get_monitors



GPIO.setwarnings(False)                     #prevents warnings from showing up when you run the code
GPIO.setmode(GPIO.BCM)                      #BCM = Broadcom chip-specific pin numbers


#Grove_Electromagnet 

magnets, m_time_on = magnet.init_magnet()        #initialization of the GPIO Magnet list and rest time for magnet on (t1) and magnet off (t2)
magnet.setup_magnet(magnets)                     #set pin in Magnet list as an output


#Piezo elements - Transducers

pins, t_time_on, frequency = piezo.init_piezo()                   #initialization of the GPIO pins list
piezo.setup_piezo(pins)                                           #set pin in pins list as an output

#notes=[262,294,330]                                              #list of notes frequencies       
#durations=[0.5,0.5,0.5]                                          #list of time durations


# TKINTER

"""
#Larger image on LCD - change in full_convert_0
w_image = 2200
h_image = 2400


print("x shift = ", x_shift)
print("y shift = ", y_shift)
print("window width = ", w_root)
print("window height = ", h_root)
"""

monitors = get_monitors()

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



root = tk.Tk()                                                              #Tinker window creation
root.attributes('-fullscreen', True)
#w_root, h_root = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{w_root}x{h_root}+{x_shift}+{y_shift}")                     #create a root with width=w_root, heigth=h_root, shifted by x_shift from the left and y_shift from the top of the monitor

cnv = tk.Canvas(root, bg="black", highlightthickness=0)
cnv.pack(fill=tk.BOTH, expand=True)



black_image_path = "/home/mborot/Pictures/black_image.png"
black_image_tk  = display.full_convert_0(black_image_path, w_root, h_root)                                                    #full screen
#black_image_tk  = display.convert_0(black_image_path)


base_path = "/home/mborot/Pictures/"
sequence=[base_path+"cubic_layer_0.png", base_path+"cubic_layer_1.png", base_path+"cubic_layer_0.png"]
layers_tk = display.full_convert_1(sequence, w_root, h_root)                                                                  #full screen
#layers_tk = display.convert_1(sequence)

layers = [2, 2, 2]                                                                                                            #number of layer, e.g: 3 times layer 0, then 4 times layer 1 and finally 3 times layer 2






#MAIN


for i in range(0, len(layers)):

    for k in range(0, layers[i]):

        display.show_image_tk_0(cnv, w_root, h_root, black_image_tk)        
        root.update_idletasks()
        root.update()
        
        sleep(2)

        magnet.coil(magnets, m_time_on)

        sleep(1)

        piezo.play(pins, t_time_on, frequency)

        sleep(2)

        display.show_image_tk_0(cnv, w_root, h_root, layers_tk[i])        
        root.update_idletasks()
        root.update()

        sleep(4)

    if i == len(layers)-1:
        display.show_image_tk_0(cnv, w_root, h_root, black_image_tk)        
        root.update_idletasks()
        root.update()

        print("End of the printing")
        root.bind('<Escape>', lambda e: root.quit())
        
    else:
        pass




"""
display.show_image_tk_0(cnv, layers_tk[2])
root.update_idletasks()
root.update()

#To exit the application by pressing Escape
root.bind('<Escape>', lambda e: root.quit())

"""


GPIO.cleanup()                              #clean up all the ports used in the program

root.mainloop()