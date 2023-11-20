from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep

def init_magnet():
    """Initialize the magnets list by asking the user how many GPIO pins are used (number of int in the list) 
    and what are the GPIO BCM number of those pins. Return t1 and t2, int of rest time for magnet on/off""" 

    magnets = []
    t_on = 0
    #t_off = 0

    n = int(input("How many GPIO are used for magnet element(s)? : "))
    if n == 0:
        return([] , 0)
    else:
        for i in range(n):
            magnets.append(int(input("Enter the GPIO BCM pin number :")))
        
        t_on = int(input("How long magnet on [s] ?"))
        #t_off = int(input("How long magnet off [s] ?"))

    return(magnets, t_on)


def setup_magnet(magnets):
    """Set the pins present in the magnets list as outputs"""

    for m in magnets:
        GPIO.setup(m, GPIO.OUT)                    #setup([pin], [GPIO.IN, GPIO.OUT]), configuring GPIO pins in output mode
    return()


def coil(magnets, time_on):
     """Actuation of the coil
    Args:   magnets: list of int(pin number BCM)
            time_on: int of rest time on  
    """
     
     print("Magnet(s) on for", time_on, "sec")
     GPIO.output(magnets, GPIO.HIGH)
     sleep(time_on)
     
     print("Magnet(s) off")
     GPIO.output(magnets, GPIO.LOW) 



############################################################################

def coil1(magnets, time_on, time_off):
     """Actuation of the coil
    Args:   magnets: list of int(pin number BCM)
            time_on, time_off: int of rest time on/off  
    """
     
     for m in magnets:
        print("Magnet", m ,"on for", time_on, "sec")
        GPIO.output(m, GPIO.HIGH)  
        sleep(time_on)
        print("Magnet", m ,"off")
        GPIO.output(m, GPIO.LOW) 
        sleep(time_off)
 