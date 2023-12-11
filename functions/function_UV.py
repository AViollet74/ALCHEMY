import RPi.GPIO as GPIO

GPIO.setwarnings(False)                     #prevents warnings from showing up when you run the code
GPIO.setmode(GPIO.BCM)                      #BCM = Broadcom chip-specific pin numbers

uv_pin = 0

def init_uv():
    """Initialize the UV ligth with the GPIO pins numbers of the UV ligth (user input).
    return: sensor_pin: int GPIO pin number(s) of the UV ligth
    """

    u = int(input("Enter the GPIO BCM pin number of the UV light : "))
    uv_pin = u
    return(uv_pin)



def switch_on(pin_nb):
    """Turn on the UV ligth.
    Arg:    pin_nb: int of the GPIO pin number of the UV ligth
    """

    GPIO.setup(pin_nb, GPIO.OUT)            #setup([pin], [GPIO.IN, GPIO.OUT]), configuring GPIO pins in output mode
    GPIO.output(pin_nb, GPIO.HIGH)          #GPIO.output([pin][GPIO.HIGH]), digital output, set pin p high, GPIO.HIGH will drive it to 3.3V, equivalent GPIO.HIGH = True = 1
    print("UV light on")



def switch_off(pin_nb):
    """Turn off the UV ligth.
    Arg:    pin_nb: int of the GPIO pin number of the UV ligth
    """

    GPIO.setup(pin_nb, GPIO.OUT)            #setup([pin], [GPIO.IN, GPIO.OUT]), configuring GPIO pins in output mode
    GPIO.output(pin_nb, GPIO.LOW)           #GPIO.output([pin][GPIO.LOW]), digital output, set pin p low, GPIO.LOW will drive it to 0V, equivalent GPIO.LOW = Fase = 0
    print("UV light off")



"""
#TEST PHOTOSENSOR
#uncomment the code below to test the UV ligth

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