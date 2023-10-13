from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep

def init_magnet():
    """Initialize the magnets list by asking the user how many GPIO pins are used (number of int in the list) 
    and what are the GPIO BCM number of those pins. Return t1 and t2, int of rest time for magnet on/off""" 

    magnets = []
    t1 = 0
    t2 = 0

    n = int(input("How many GPIO are used for magnet element(s)? : "))
    if n == 0:
        return([] , None, None)
    else:
        for i in range(n):
            magnets.append(int(input("Enter the GPIO BCM pin number :")))
        
        t1 = int(input("How long magnet on [s] ?"))
        t2 = int(input("How long magnet off [s] ?"))

    return(magnets, t1, t2)


def setup_magnet(magnets):
    """Set the pins present in the magnets list as outputs"""

    for m in magnets:
        GPIO.setup(m, GPIO.OUT)                    #setup([pin], [GPIO.IN, GPIO.OUT]), configuring GPIO pins in output mode
    return()



def coil(magnets, t1, t2):
     """Actuation of the coil
    Args:   magnets: list of int(pin number BCM)
            t1, t2: int of rest time on/off  
    """
     
     for m in magnets:
        print("Magnet", m ,"on for", t1, "sec")
        GPIO.output(m, GPIO.HIGH)  
        sleep(t1)
        print("Magnet", m ,"off for", t2, "sec")
        GPIO.output(m, GPIO.LOW) 
        sleep(t2)
 