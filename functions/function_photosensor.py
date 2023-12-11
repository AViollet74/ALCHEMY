import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)                     #prevents warnings from showing up when you run the code
GPIO.setmode(GPIO.BCM)                      #BCM = Broadcom chip-specific pin numbers

sensor_pin = 0

def init_sensor():
    s = int(input("Enter the GPIO BCM pin number of the photoelectric sensor : "))
    sensor_pin = s
    return(sensor_pin)


"""
#TEST PHOTOSENSOR

sensor_pin = 2
GPIO.setup(sensor_pin, GPIO.IN)

while(True):
    if GPIO.input(sensor_pin) == False:
        print("Light stop")
    else:                                   #GPIO.input(pin_sensor) == True
        print("Light pass")


"""