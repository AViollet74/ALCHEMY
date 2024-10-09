
import functions.function_photosensor as sensor



import RPi.GPIO as GPIO
from time import sleep


import os
import random


sensor_pin = sensor.init_sensor()
GPIO.setup(sensor_pin, GPIO.IN)
print("photo sensor setup success")

while True: 
    value=GPIO.input(sensor_pin)
    print(value)
    sleep(0.25)

