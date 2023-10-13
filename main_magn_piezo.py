import functions.function_magnet as magnet
import functions.function_piezo as piezo
import functions.function_display as display
import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep
import tkinter as tk 
from PIL import Image, ImageTk


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

image = Image.open("/home/mborot/Pictures/mont_blanc.jpg")
image.show()




y = 1 #index of loop
z = 2 #number of loops

while y <= z :
    piezo.play1(Pins,notes,durations)
    magnet.coil(Magnet, t1, t2)
    #piezo.play3()
    y += 1


GPIO.cleanup()                              #clean up all the ports used in the program