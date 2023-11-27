import RPi.GPIO as GPIO

GPIO.setwarnings(False)                     #prevents warnings from showing up when you run the code
GPIO.setmode(GPIO.BCM)                      #BCM = Broadcom chip-specific pin numbers

uv_pin = 0

def init_uv():
    u = int(input("Enter the GPIO BCM pin number of the UV light : "))
    uv_pin = u
    return(uv_pin)

def switch_on(pin_nb):
    GPIO.setup(uv_pin, GPIO.OUT)
    GPIO.output(pin_nb, GPIO.HIGH)
    print("UV light on")

def switch_off(pin_nb):
    GPIO.setup(uv_pin, GPIO.OUT)
    GPIO.output(pin_nb, GPIO.LOW)
    print("UV light off")

"""
pin_UV = 26
GPIO.setup(pin_UV, GPIO.OUT)


while(True):
    GPIO.output(pin_UV, GPIO.HIGH)
    print("UV light on")
    sleep(4)
    GPIO.output(pin_UV, GPIO.LOW)
    print("UV light off")
    sleep(4)

"""