a=input("press enter")
print(len(a))
print(f"efef{a}ettete")


# import numpy as np
# print(np.pi)


import sys
print(sys.path)

import board
from adafruit_motorkit import MotorKit
kit = MotorKit(i2c=board.I2C())
kit.motor1.throttle = 1
