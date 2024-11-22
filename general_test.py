a=1
b=True
if a==b: 
    print("Equal")

import os
path = "/home/alchemy/PRINT"
liste= os.listdir(path)
nb_layers = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
print("nombre",nb_layers, liste)
# a=input("press enter")
# print(len(a))
# print(f"efef{a}ettete")
# import board
# from adafruit_motor import stepper
# from adafruit_motorkit import MotorKit
# import functions.function_motor as motor
# kit = MotorKit(i2c=board.I2C())

import tkinter as tk
print("success")
# from PIL import Image, ImageTk
# import cnv 
# image=Image.open("/home/alchemy/Pictures/Screenshots/code sensor phot.png")
# import numpy as np
# print(np.pi)

# import sys
# sys.path.append("/home/alchemy/ALCHEMY/alchemy/lib64/python3.12/site-packages")
# print(sys.path)

# w_root = 1920
# h_root = 1080

# cnv.create_image((w_root/2), (h_root/2), anchor=tk.CENTER, image=image)

print("start throttle")
kit = MotorKit(i2c=board.I2C())
kit.motor1.throttle = 1
