import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)                     #prevents warnings from showing up when you run the code
GPIO.setmode(GPIO.BCM)                      #BCM = Broadcom chip-specific pin numbers

pin_sensor = 2
GPIO.setup(pin_sensor, GPIO.IN)
#GPIO.setup(pin_sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("start test photosensor")

while(True):
    if GPIO.input(pin_sensor) == False:
        print("Light stop")
        sleep(4)
    else:                                   #GPIO.input(pin_sensor) == True
        print("Light pass")