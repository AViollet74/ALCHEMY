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
        PUL=6
        DIR=12
        ENA=16
    print("access funciton")
    chip=gpiod.Chip("gpiochip0")
    linePUL=chip.get_line(PUL)
    linePUL.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
    lineDIR=chip.get_line(DIR)
    lineDIR.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
    lineENA=chip.get_line(ENA)
    lineENA.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
    
    step_num = round(distance/8*360/1.8)
    sleep_time = temps/step_num       #temps d'attente entre chaque step (diviser par deux car haut puis bas)
    
    if sens > 0:
        # start_time = monotonic()
        lineENA.set_value(1)
        sleep(0.1)
        lineDIR.set_value(0)
        sleep(0.1)
        for i in range(step_num):
            linePUL.set_value(1)
            sleep(sleep_time/2)
            linePUL.set_value(0)
        lineENA.set_value(0)

        
        
        """reste a implémenter et traduire le mouvement forward"""
    else :
        # start_time = monotonic()
        lineENA.set_value(1)
        sleep(0.1)
        lineDIR.set_value(1)
        sleep(0.1)
        for i in range(step_num):
            linePUL.set_value(1)
            sleep(sleep_time/2)
            linePUL.set_value(0)
        lineENA.set_value(0)
        
        """reste à implémenter et traduire le mode backward"""
    return
    
    
    
# def forward():
#     GPIO.output(ENA, GPIO.HIGH)
#     # GPIO.output(ENAI, GPIO.HIGH)
#     # print('ENA set to HIGH - Controller Enabled')
#     #
#     sleep(.5) # pause due to a possible change direction
#     GPIO.output(DIR, GPIO.LOW)
#     # GPIO.output(DIRI, GPIO.LOW)
#     # print('DIR set to LOW - Moving Forward at ' + str(delay))
#     # print('Controller PUL being driven.')
#     for x in range(durationFwd): 
#         GPIO.output(PUL, GPIO.HIGH)
#         sleep(delay)
#         GPIO.output(PUL, GPIO.LOW)
#         sleep(delay)
#     GPIO.output(ENA, GPIO.LOW)
#     GPIO.output(ENAI, GPIO.LOW)
#     print('ENA set to LOW - Controller Disabled')
#     sleep(.5) # pause for possible change direction
#     return
# #

# def reverse():
#     GPIO.output(ENA, GPIO.HIGH)
#     GPIO.output(ENAI, GPIO.HIGH)
#     print('ENA set to HIGH - Controller Enabled')
#     #
#     sleep(.5) # pause due to a possible change direction
#     GPIO.output(DIR, GPIO.HIGH)
#     GPIO.output(DIRI, GPIO.HIGH)
#     print('DIR set to HIGH - Moving Backward at ' + str(delay))
#     print('Controller PUL being driven.')
#     #
#     for y in range(durationBwd):
#         GPIO.output(PUL, GPIO.HIGH)
#         sleep(delay)
#         GPIO.output(PUL, GPIO.LOW)
#         sleep(delay)
#     GPIO.output(ENA, GPIO.LOW)
#     GPIO.output(ENAI, GPIO.LOW)
#     print('ENA set to LOW - Controller Disabled')
#     sleep(.5) # pause for possible change direction
#     return

# while cyclecount < cycles:
#     forward()
#     reverse()
#     cyclecount = (cyclecount + 1)
#     print('Number of cycles completed: ' + str(cyclecount))
#     print('Number of cycles remaining: ' + str(cycles - cyclecount))
# #
# GPIO.cleanup()
# print('Cycling Completed')
# #


            
            
            
