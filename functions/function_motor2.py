# Based on: https://www.raspberrypi.org/forums/viewtopic.php?t=242928\.
# Route 3.3 VDC to the controller "+" input for each: ENA, PUL, and DIR
#
from time import sleep
import gpiod
from time import sleep
import time
from time import monotonic

#
PUL = 17  # Stepper Drive Pulses
DIR = 27  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
ENA = 22  # Controller Enable Bit (High to Enable / LOW to Disable).
# DIRI = 14  # Status Indicator LED - Direction
# ENAI = 15  # Status indicator LED - Controller Enable
#
# NOTE: Leave DIR and ENA disconnected, and the controller WILL drive the motor in Default direction if PUL is applied.
# 
## MOTOR1 (Z-table)
def move_dist_time_dir_dm(distance, temps, sens, ID):
    
    if ID==1:
        PUL = 22  # Stepper Drive Pulses
        DIR = 23  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
        ENA = 24 
    else:
        PUL=21
        DIR=20
        ENA=26
    
    print(PUL, ENA, DIR)
    chip=gpiod.Chip("gpiochip0")
    linePUL=chip.get_line(PUL)
    linePUL.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
    lineDIR=chip.get_line(DIR)
    lineDIR.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
    lineENA=chip.get_line(ENA)
    lineENA.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
    
    stepfactor=2
    step_num = round(distance/8*360/1.8*stepfactor)
    
    sleep_time = temps/step_num       #temps d'attente entre chaque step (diviser par deux car haut puis bas)
    
    on=1
    off=0
    if sens > 0:
        # start_time = monotonic()
        lineENA.set_value(on)
        sleep(0.1)
        lineDIR.set_value(0)
        sleep(0.1)
        for i in range(step_num):
            linePUL.set_value(1)
            sleep(sleep_time/2)
            linePUL.set_value(0)
            sleep(sleep_time/2)
        lineENA.set_value(off)

    else :
        # start_time = monotonic()
        lineENA.set_value(on)
        sleep(0.1)
        lineDIR.set_value(1)
        sleep(0.1)
        for i in range(step_num):
            linePUL.set_value(1)
            sleep(sleep_time/2)
            linePUL.set_value(0)
            sleep(sleep_time/2)
        lineENA.set_value(off)
    return