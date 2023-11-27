import functions.function_magnet as magnet
import functions.function_piezo as piezo
import functions.function_display as display
import functions.function_UV as uv
import functions.function_photosensor as sensor

import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep
import tkinter as tk 
import numpy as np
from PIL import Image, ImageTk
from screeninfo import get_monitors



GPIO.setwarnings(False)                                 #prevents warnings from showing up when you run the code
GPIO.setmode(GPIO.BCM)                                  #BCM = Broadcom chip-specific pin numbers


#Grove_Electromagnet 
magnets, m_time_on = magnet.init_magnet()               #initialization of the GPIO Magnet list and rest time for magnet on (t1) and magnet off (t2)
magnet.setup_magnet(magnets)                            #set pin in Magnet list as an output


#Piezo elements - Transducers
pins, p_time_on, frequency = piezo.init_piezo()         #initialization of the GPIO pins list
piezo.setup_piezo(pins)                                 #set pin in pins list as an output

#UV ligth
uv_pin = uv.init_uv()
GPIO.setup(uv_pin, GPIO.OUT)

#Photoelctric sensor
sensor_pin = sensor.init_sensor()
GPIO.setup(sensor_pin, GPIO.IN)

# TKINTER

"""
#INFO MONITORS
for m in get_monitors():
    print(str(m))

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
root.geometry(f"{w_root}x{h_root}+{x_shift}+{y_shift}")                     #create a root with width=w_root, heigth=h_root, shifted by x_shift from the left and y_shift from the top of the monitor

cnv = tk.Canvas(root, bg="black", highlightthickness=0)
cnv.pack(fill=tk.BOTH, expand=True)


#IMAGES
black_image_path = "/home/mborot/Pictures/black_image.png"
black_image_tk  = display.full_convert_0(black_image_path, w_root, h_root)                                                    #full screen


#PNG slicing 
nb_slice = 13
folder_path = "/home/mborot/Pictures/slicing/" 
png_paths = display.convert_png(folder_path, nb_slice)
png_tk = display.full_convert_1(png_paths, w_root, h_root) 



#MAIN

uv.switch_on(uv_pin)

for i in range(len(png_tk)):

    display.show_image_tk_0(cnv, w_root, h_root, black_image_tk)
    root.update_idletasks()
    root.update()

    sleep(2)

    magnet.coil(magnets, m_time_on)

    sleep(1)

    piezo.play(pins, p_time_on, frequency)

    sleep(2)

    display.show_image_tk_0(cnv, w_root, h_root, png_tk[i])
    #display.show_image_tk_2(root, png_tk[i], image_names[i])
    root.update_idletasks()
    root.update()
    
    sleep(4)
    
    if i == len(png_tk)-1:
        display.show_image_tk_0(cnv, w_root, h_root, black_image_tk)        
        root.update_idletasks()
        root.update()

        print("End of the printing")
        root.bind('<Escape>', lambda e: root.quit())
        
    else:
        pass

uv.switch_off(uv_pin)

GPIO.cleanup()                              #clean up all the ports used in the program

root.mainloop()