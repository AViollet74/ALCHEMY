import functions.function_magnet as magnet
import functions.function_piezo as piezo
import functions.function_display as display
import functions.function_UV as uv
import functions.function_photosensor as sensor

import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep
import tkinter as tk 
from screeninfo import get_monitors


#Images definition
base_path = "/home/mborot/Pictures/"                                                                    #Folder path
black_image_path = base_path+"black_image.png"                                                          #Black image path
sequence=[base_path+"cubic_layer_0.png", base_path+"cubic_layer_1.png", base_path+"cubic_layer_0.png"]  #List of image paths 
layers = [2, 3, 2]                                                                                      #Number of times that each image of the sequence list will be displayed sucessively (number of layers)


#GPIO settings
GPIO.setwarnings(False)                                                                                 #prevents warnings from showing up when you run the code
GPIO.setmode(GPIO.BCM)                                                                                  #BCM = Broadcom chip-specific pin numbers


#Initialisation of the hardware components
#Grove_Electromagnet 
magnets, m_time_on = magnet.init_magnet()                         
magnet.setup_magnet(magnets)                                      

#Piezo elements - Transducers
pins, p_time_on, frequency = piezo.init_piezo()                   
piezo.setup_piezo(pins)                                          

#UV ligth
uv_pin = uv.init_uv()

#Photoelctric sensor
sensor_pin = sensor.init_sensor()
GPIO.setup(sensor_pin, GPIO.IN)

#Motor
# kit = MotorKit(i2c=board.I2C())
#step_nb = 500


#GUI creation with TkInter 

"""
#Uncomment to get information on monitors
for m in get_monitors():
    print(str(m))
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



root = tk.Tk()                                                                                          #Tinker window creation
root.attributes('-fullscreen', True)
root.geometry(f"{w_root}x{h_root}+{x_shift}+{y_shift}")                                                 #Create a root with width=w_root, heigth=h_root, shifted by x_shift from the left and y_shift from the top of the monitor

cnv = tk.Canvas(root, bg="black", highlightthickness=0)
cnv.pack(fill=tk.BOTH, expand=True)


#Conversion of the Images
black_image_tk  = display.full_convert_0(black_image_path, w_root, h_root)                              #Convert black image path to black image object, with full screen dimensions                                         
images_tk = display.full_convert_1(sequence, w_root, h_root)                                            #Convert image paths from sequence list to a list of image object, with full screen dimensions                      



#MAIN

#motor.start_position(sensor_pin)

for i in range(0, len(layers)):

    for k in range(0, layers[i]):

        display.show_image_tk_0(cnv, w_root, h_root, black_image_tk)        
        root.update_idletasks()
        root.update()

        magnet.coil(magnets, m_time_on)

        piezo.play(pins, p_time_on, frequency)

        uv.switch_on(uv_pin)

        display.show_image_tk_0(cnv, w_root, h_root, images_tk[i])        
        root.update_idletasks()
        root.update()

        sleep(4)

        uv.switch_off(uv_pin)

        #sleep(2)
        #motor.move_up(step_nb)


    if i == len(layers)-1:
        display.show_image_tk_0(cnv, w_root, h_root, black_image_tk)        
        root.update_idletasks()
        root.update()

        print("End of the printing")
        root.bind('<Escape>', lambda e: root.quit())
        
    else:
        pass


#Clean up all the ports used in the program
GPIO.cleanup()                              

root.mainloop()