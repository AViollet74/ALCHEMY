import RPi.GPIO as GPIO
from time import sleep

def init_piezo():
    """Initialize the pins list by asking the user how many GPIO pins are used (number of int in the list) 
    and what are the GPIO BCM number of those pins"""             

    pins = []

    n = int(input("How many GPIO are used for piezo element(s)? : "))
    if n == 0:
        return([])
    else:
        for i in range(n):
            pins.append(int(input("Enter the GPIO BCM pin number :")))
        return(pins)



def setup_piezo(pins):
    """Set the pins present in the pins list as outputs"""

    for p in pins:
        GPIO.setup(p, GPIO.OUT)                    #setup([pin], [GPIO.IN, GPIO.OUT]), configuring GPIO pins in output mode
    return()



def play1(pins,notes,durations):
    """Actuation of the piezo elements 1 by 1
    Args:   pins: list of int(pin number BCM)
            notes: list of int(note frequencies)
            durations: list of int(time duration for frequencies)
    """
    for p in pins:                                  #p index in list pins
        print("pin number", p,"is playing")

        GPIO.output(p, GPIO.HIGH)                   #GPIO.output([pin][GPIO.HIGH]), digital output, set pin p high, GPIO.HIGH will drive it to 3.3V, equivalent GPIO.HIGH = True = 1
        pin = GPIO.PWM(p, 100)                      #GPIO.PWM([pin][frequency]), analogue output, initialize PWM pin up with 100Hz frequency
        pin.start(50)                               #start([duty cycle]) set initil value / output to a 50% duty cycle

        for n,d in zip(notes,durations):            #iteration over notes (n) and durations (d) lists 
            pin.ChangeFrequency(n)                  #apply frequency n to pin p...
            sleep(d)                                #... over time d
        
        pin.stop()
        GPIO.output(p, GPIO.LOW)                    #GPIO.output([pin][GPIO.LOW]), digital output, set pin p low, GPIO.LOW will drive it to 0V, equivalent GPIO.LOW = Fase = 0
        


def play2(pins,notes,durations):
    """Actuation of the piezo elements all together
    Args:   pins: list of int(pin number BCM)
            notes: list of int(note frequencies)
            durations: list of int(time duration for frequencies)
    """

    for n,d in zip(notes, durations):
        
        for p in pins:
            GPIO.output(p, GPIO.HIGH)
            pin = GPIO.PWM(p, 100)
            pin.start(50)
            pin.ChangeFrequency(n)
            sleep(d)

    for p in pins:
        pin.stop()
        GPIO.output(p, GPIO.LOW)


def play3():
    """Actuation of the piezo elements all together at a frequency oh 100 Hz during 5 sec
    """
    pin16 = 16
    pin20 = 20
    pin21 = 21

    GPIO.setup(16, GPIO.OUT)                    #setup([pin], [GPIO.IN, GPIO.OUT]), set pin 14 as an output
    GPIO.setup(20, GPIO.OUT) 
    GPIO.setup(21, GPIO.OUT) 
    GPIO.output(pin16, GPIO.HIGH)                   #GPIO.output([pin][GPIO.HIGH]), digital output, set pin p high, GPIO.HIGH will drive it to 3.3V, equivalent GPIO.HIGH = True = 1
    GPIO.output(pin20, GPIO.HIGH)    
    GPIO.output(pin21, GPIO.HIGH)    


    Pin16 = GPIO.PWM(pin16, 100)                      #GPIO.PWM([pin][frequency]), analogue output, initialize PWM pin up with 100Hz frequency
    Pin20 = GPIO.PWM(pin20, 100) 
    Pin21 = GPIO.PWM(pin21, 100) 

    Pin16.start(50) 
    Pin20.start(50) 
    Pin21.start(50) 

    sleep(5)

    Pin16.stop() 
    Pin20.stop() 
    Pin21.stop() 

    GPIO.output(pin16, GPIO.LOW)                   #GPIO.output([pin][GPIO.HIGH]), digital output, set pin p high, GPIO.HIGH will drive it to 3.3V, equivalent GPIO.HIGH = True = 1
    GPIO.output(pin20, GPIO.LOW)    
    GPIO.output(pin21, GPIO.LOW) 