import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)                     #prevents warnings from showing up when you run the code
GPIO.setmode(GPIO.BCM)                      #BCM = Broadcom chip-specific pin numbers


snesor_pin = 0

def init_sensor():
    s = int(input("Enter the GPIO BCM pin number of the UV light : "))
    if s == 0:
        return(None)
    else:
        sensor_pin = s
    return(sensor_pin)


"""
while(True):
    if GPIO.input(sensor_pin) == False:
        print("Light stop")
        sleep(4)
    else:                                   #GPIO.input(pin_sensor) == True
        print("Light pass")

"""