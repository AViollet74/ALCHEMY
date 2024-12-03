# import RPi.GPIO as GPIO
import gpiod
from time import sleep
import time


def init_vibration():
    """Initialize the piezo list with the GPIO pins numbers of the piezo element(s) and return the actuation time and the applied frequency (user input).
    return: piezo: list of int GPIO pin number(s) of the piezo element(s)
            t_on: int actuation time of the piezo element(s)
            freq: int of the frequency
    """ 

    motors = []
    t_on = 0
    
    
    n = int(input("How many GPIO are used for vibration element(s)? : "))
    if n == 0:
        return([], 0, None)
    else:
        for i in range(n):
            motors.append(int(input("Enter the GPIO BCM pin number :")))

        t_on = int(input("How long motors on [s] ?"))

        return(motors, t_on)
    

def setup_vibration(motors):
    """Set the pins present in the pins list as outputs"""
    if motors==[]:
        return()
    else:
        # for p in piezos:
        chip=gpiod.Chip("gpiochip0")
        line=chip.get_lines(motors)
        line.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
        # line.set_values([1 for _ in range(len(piezos))])                                #line.set_value([value]), set the line to the given value, 0 for low, 1 for high
        return()


def activate_v(motors, time_on):
    """Actuation of the piezo element(s) for a given time
       Args:   piezos: list of int GPIO pin number(s)
               time_on: int activation time
               freq: int frequency
    """ 

    chip=gpiod.Chip("gpiochip0")
    line=chip.get_lines(motors)
    line.request(consumer="main",type=gpiod.LINE_REQ_DIR_OUT)
    print("vibration start")
    line.set_values([1 for _ in range(len(motors))])
    sleep(time_on) 
    line.set_values([0 for _ in range(len(motors))])                          #line.set_value([value]), set the line to the given value, 0 for low, 1 for high
    print("vibration end")
    return()












