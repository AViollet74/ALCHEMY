import functions.function_piezo as piezo

import RPi.GPIO as GPIO
from gpiozero import LED



piezos, p_time_on, frequency = piezo.init_piezo()                   
piezo.setup_piezo(piezos)     
print("Piezo setup succes") 
piezo.activate_p(piezos, 10,40000)









