import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)                     #prevents warnings from showing up when you run the code
GPIO.setmode(GPIO.BCM)                      #BCM = Broadcom chip-specific pin numbers

pin_UV = 21
GPIO.setup(pin_UV, GPIO.OUT)


while(True):
    GPIO.output(pin_UV, GPIO.HIGH)
    print("UV light on")
    sleep(4)
    GPIO.output(pin_UV, GPIO.LOW)
    print("UV light off")
    sleep(4)


GPIO.cleanup() 