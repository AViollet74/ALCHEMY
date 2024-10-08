import functions.function_magnet as magnet
import functions.function_piezo as piezo
import functions.function_display as display
import functions.function_UV as uv
import functions.function_photosensor as sensor
import functions.function_motor as motor

import RPi.GPIO as GPIO
from gpiozero import LED



piezos, p_time_on, frequency = piezo.init_piezo()                   
piezo.setup_piezo(piezos)     
print("Piezo setup succes") 
piezo.activate_p(piezos, 10,40000)









