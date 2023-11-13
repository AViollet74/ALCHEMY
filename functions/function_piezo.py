import RPi.GPIO as GPIO
from time import sleep
import time
import numpy as np

def init_piezo():
    """Initialize the pins list by asking the user how many GPIO pins are used (number of int in the list) 
    and what are the GPIO BCM number of those pins"""             

    pins = []
    t_on = 0
    freq = 0 

    n = int(input("How many GPIO are used for transducer(s)? : "))
    if n == 0:
        return([], None, None)
    else:
        for i in range(n):
            pins.append(int(input("Enter the GPIO BCM pin number :")))

        t_on = int(input("How long transducers on [s] ?"))
        #t_off = int(input("How long transducers off [s] ?"))

        freq = int(input("At what frequency transducers work [Hz] ? :"))

        return(pins, t_on, freq)



def setup_piezo(pins):
    """Set the pins present in the pins list as outputs"""

    for p in pins:
        GPIO.setup(p, GPIO.OUT)                    #setup([pin], [GPIO.IN, GPIO.OUT]), configuring GPIO pins in output mode
    return()



def play(pins, time_on, freq):
    """Actuation of the piezo elements all together
       Args:   pins: list of int(pin number BCM)
               freq: int(note frequencies)
               time_on: int(rest time on)
    """ 

    pins_pwm =[]

    for p in pins:
        #GPIO.setup(p, GPIO.OUT)                         #setup([pin], [GPIO.IN, GPIO.OUT]), configuring GPIO pins in output mode
        pins_pwm.append(GPIO.PWM(p, freq))              #GPIO.PWM([pin][frequency]), analogue output, initialize PWM pin up with given frequency

    for pwm in pins_pwm:
        pwm.start(50)                                   #start([duty cycle]) set initil value / output to a 50% duty cycle

    print("Tranducer(s) on for", time_on, "sec") 
    GPIO.output(pins, GPIO.HIGH)                        #GPIO.output([pin][GPIO.HIGH]), digital output, set pin p high, GPIO.HIGH will drive it to 3.3V, equivalent GPIO.HIGH = True = 1

    sleep(5)

    print("Transducer(s) off")
    GPIO.output(pins, GPIO.LOW)                         #GPIO.output([pin][GPIO.LOW]), digital output, set pin p low, GPIO.LOW will drive it to 0V, equivalent GPIO.LOW = Fase = 0

    for pwm in pins_pwm:
        pwm.stop()                                      #To turn PWM on that pin off





################################################################################

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
        
        pin.stop()                                  #to turn PWM on that pin off
        GPIO.output(p, GPIO.LOW)                    #GPIO.output([pin][GPIO.LOW]), digital output, set pin p low, GPIO.LOW will drive it to 0V, equivalent GPIO.LOW = Fase = 0
        


def play2(pins,notes,durations):
    """Actuation of the piezo elements all together
    Args:   pins: list of int(pin number BCM)
            notes: list of int(note frequencies)
            durations: list of int(time duration for frequencies)
    """
    for p in pins:
        p = GPIO.PWM(p, 100)                       #GPIO.PWM([pin][frequency]), analogue output, initialize PWM pin up with frequency
        p.start(50)                                 #start([duty cycle]) set initil value / output to a 50% duty cycle
    

    
    GPIO.output(pins, GPIO.HIGH)                    #GPIO.output([pin][GPIO.HIGH]), digital output, set pin p high, GPIO.HIGH will drive it to 3.3V, equivalent GPIO.HIGH = True = 1

    sleep(5)

    
    GPIO.output(pins, GPIO.LOW)                     #GPIO.output([pin][GPIO.LOW]), digital output, set pin p low, GPIO.LOW will drive it to 0V, equivalent GPIO.LOW = Fase = 0

    #for p in pins:
     #   p.stop()
    for n,d in zip(notes, durations):
        #duration = time.perf_counter()
        pwm = []
        for p in pins:
            GPIO.output(p, GPIO.HIGH)
            pwm.append(GPIO.PWM(p, 100))
        for pw in pwm:
            pw.start(50)
            pw.ChangeFrequency(n) 
        sleep(d)

        if len(pins) == 1:
            pwm[0].stop()
            GPIO.output(pins[0], GPIO.LOW)

    for pw, p in zip(pwm, pins):
        pw.stop()
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
    
    Pin16 = GPIO.PWM(pin16, 262)                      #GPIO.PWM([pin][frequency]), analogue output, initialize PWM pin up with 100Hz frequency
    Pin20 = GPIO.PWM(pin20, 294) 
    Pin21 = GPIO.PWM(pin21, 330) 

    Pin16.start(50) 
    Pin20.start(50) 
    Pin21.start(50)    
    
    print("pins are on")
    
    GPIO.output(pin16, GPIO.HIGH)                   #GPIO.output([pin][GPIO.HIGH]), digital output, set pin p high, GPIO.HIGH will drive it to 3.3V, equivalent GPIO.HIGH = True = 1
    GPIO.output(pin20, GPIO.HIGH)    
    GPIO.output(pin21, GPIO.HIGH) 

    
    sleep(5)


    print("pins are off")

    Pin16.stop() 
    Pin20.stop() 
    Pin21.stop() 

    sleep(5)
    

    GPIO.output(pin16, GPIO.LOW)                   #GPIO.output([pin][GPIO.HIGH]), digital output, set pin p high, GPIO.HIGH will drive it to 3.3V, equivalent GPIO.HIGH = True = 1
    GPIO.output(pin20, GPIO.LOW)    
    GPIO.output(pin21, GPIO.LOW) 