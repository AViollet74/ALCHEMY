import tkinter as tk 
from PIL import Image, ImageTk
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread

def convert(images_paths, images_tk):
    """Upload image and create ImageTk.PhotoImage object"""

    for path in images_paths:       
        image = Image.open(path)
        image_tk = ImageTk.PhotoImage(image)
        images_tk.append(image_tk)
        
    return images_tk


def show_image(frame, images_tk):  
    """Create a Canvas widget and display many images""" 

    x, y, = 10, 10

    for i in images_tk:
        canvas = tk.Canvas(frame, width = i.width(), height = i.height())  #create cavas to display images
        canvas.pack()
        canvas.create_image(x, y, anchor=tk.NW, image=i)
        x += i.width() + 10
    
    return



def display_image(frame, image_tk):
    """Create a Canvas widget and display a single image"""                      

    canvas = tk.Canvas(frame, width=image_tk.width(), height=image_tk.height())  #create cavas to display image
    canvas.pack()
    canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
    
    return


#Button

def next_image(image_index, images_tk):
    if image_index < len(images_tk)-1:
        image_index += 1
        show_image(image_index)


def prv_image(image_index, images_tk):
    if image_index > 0:
        image_index -= 1
        show_image(image_index)


#Matplotlib

def read(images_paths):

    images_read = [] 

    for path in images_paths:
        images_read.append(imread(path))
    return images_read


def show_plot(fig, columns, rows, images_read):

    index=0
    for i in range(1, columns*rows):
        fig.add_subplot(rows, columns, i) 
        plt.imshow(images_read[index]) # showing image
        plt.axis('off')
        plt.title("Image", index+1)
        index +=1

    plt.show() 
