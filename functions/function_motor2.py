# Based on: https://www.raspberrypi.org/forums/viewtopic.php?t=242928\.
# Route 3.3 VDC to the controller "+" input for each: ENA, PUL, and DIR
#
from time import sleep
import RPi.GPIO as GPIO
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
def move_dist_time_dir_1(distance, temps, sens):
        # for p in piezos:
    chip=gpiod.Chip("gpiochip0")
    linePUL=chip.get_line(PUL)
    linePUL.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
    lineDIR=chip.get_line(DIR)
    lineDIR.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
    lineENA=chip.get_line(ENA)
    lineENA.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
    
    step_num = round(distance/8*360/1.8)
    sleep_time = temps/step_num
    
    if sens > 0:
        start_time = monotonic()
        """reste a implémenter et traduire le mouvement forward"""
        # for i in range(step_num):
        #     kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        #             # Wait for the delay without blocking other processes
        #     while monotonic() - start_time < sleep_time:
        #         pass
        #     start_time=monotonic()
    else :
        start_time = monotonic()
        """reste à implémenter et traduire le mode forward"""
        # for i in range(step_num):
        #     kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        #     while monotonic() - start_time < sleep_time:
        #         pass
        #     start_time=monotonic()

    
    









# def setup_controller(motors):
#     """Set the pins present in the pins list as outputs"""
#     if motors==[]:
#         return()
#     else:
#         # for p in piezos:
#         chip=gpiod.Chip("gpiochip0")
#         line=chip.get_lines(motors)
#         line.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
#         return()


# GPIO.setmode(GPIO.BCM)
# GPIO.setup(PUL, GPIO.OUT)
# GPIO.setup(DIR, GPIO.OUT)
# GPIO.setup(ENA, GPIO.OUT)
# GPIO.setup(DIRI, GPIO.OUT)
# GPIO.setup(ENAI, GPIO.OUT)
#
# Could have usesd only one DURATION constant but chose two. This gives play options.
durationFwd = 5000 # This is the duration of the motor spinning. used for forward direction
durationBwd = 5000 # This is the duration of the motor spinning. used for reverse direction
print('Duration Fwd set to ' + str(durationFwd))
print('Duration Bwd set to ' + str(durationBwd))
#
delay = 0.0000001 # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
print('Speed set to ' + str(delay))
#
cycles = 1000 # This is the number of cycles to be run once program is started.
cyclecount = 0 # This is the iteration of cycles to be run once program is started.
print('number of Cycles to Run set to ' + str(cycles))
#
#




# def activate_v(motors, time_on):
#     """Actuation of the piezo element(s) for a given time
#        Args:   piezos: list of int GPIO pin number(s)
#                time_on: int activation time
#                freq: int frequency
#     """ 
#     if motors==[] or time_on==0  or time_on<0  or not motors:
#         return()
#     else:
#         chip=gpiod.Chip("gpiochip0")
#         line=chip.get_lines(motors)
#         line.request(consumer="main",type=gpiod.LINE_REQ_DIR_OUT)
#         print("vibration start")
#         line.set_values([1 for _ in range(len(motors))])
#         sleep(time_on) 
#         line.set_values([0 for _ in range(len(motors))])                          #line.set_value([value]), set the line to the given value, 0 for low, 1 for high
#         print("vibration end")
#         return()
    
    
    
    
def forward():
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(ENAI, GPIO.HIGH)
    print('ENA set to HIGH - Controller Enabled')
    #
    sleep(.5) # pause due to a possible change direction
    GPIO.output(DIR, GPIO.LOW)
    GPIO.output(DIRI, GPIO.LOW)
    print('DIR set to LOW - Moving Forward at ' + str(delay))
    print('Controller PUL being driven.')
    for x in range(durationFwd): 
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)
    GPIO.output(ENA, GPIO.LOW)
    GPIO.output(ENAI, GPIO.LOW)
    print('ENA set to LOW - Controller Disabled')
    sleep(.5) # pause for possible change direction
    return
#
#
def reverse():
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(ENAI, GPIO.HIGH)
    print('ENA set to HIGH - Controller Enabled')
    #
    sleep(.5) # pause due to a possible change direction
    GPIO.output(DIR, GPIO.HIGH)
    GPIO.output(DIRI, GPIO.HIGH)
    print('DIR set to HIGH - Moving Backward at ' + str(delay))
    print('Controller PUL being driven.')
    #
    for y in range(durationBwd):
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)
    GPIO.output(ENA, GPIO.LOW)
    GPIO.output(ENAI, GPIO.LOW)
    print('ENA set to LOW - Controller Disabled')
    sleep(.5) # pause for possible change direction
    return

while cyclecount < cycles:
    forward()
    reverse()
    cyclecount = (cyclecount + 1)
    print('Number of cycles completed: ' + str(cyclecount))
    print('Number of cycles remaining: ' + str(cycles - cyclecount))
#
GPIO.cleanup()
print('Cycling Completed')
#




## MOTOR1 (Z-table)
def move_dist_time_dir_1(distance, temps, sens):
    """Move the building platform
    Args : distance in mm, time in seconds, direction in integer (1: forward, -1: backward)"""
    
    # print(f"Stepper motor moves by {distance}mm in {temps}s, in direction {sens}")
    step_num = round(distance/8*360/1.8)
    sleep_time = temps/step_num
    if sens > 0:
        start_time = monotonic()
        for i in range(step_num):
            kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
                    # Wait for the delay without blocking other processes
            while monotonic() - start_time < sleep_time:
                pass
            start_time=monotonic()
    else :
        start_time = monotonic()
        for i in range(step_num):
            kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            while monotonic() - start_time < sleep_time:
                pass
            start_time=monotonic()
            
            
            
            
