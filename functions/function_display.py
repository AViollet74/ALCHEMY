import tkinter as tk 
from PIL import Image, ImageTk
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread

def convert(images_paths):
    """Upload image and create ImageTk.PhotoImage object
    Args : list of images paths
    return :list of converted ImageTk.PhotoImage object"""

    images_tk=[]                                                #create empty list

    for path in images_paths:       
        image = Image.open(path)                                #open image path
        image = image.resize((500, 500), Image.ANTIALIAS)       #resize image
        image_tk = ImageTk.PhotoImage(image)                    #create ImageTk.PhotoImage object
        images_tk.append(image_tk)                              #add ImageTk.PhotoImage object to the list
        
    return images_tk



def show_image(frame, images_tk, image_index):
    """Create a Canvas widget and display a single image
       Args: frame, 
            list images_tk, list of ImageTk.PhotoImage objects,
            image_index, image index in the list that corresponds to the images that is displayed"""                      

    image_tk = images_tk[image_index]

    cnv = tk.Canvas(frame, width=500, height=500, bg="ivory")
    cnv.grid(row=0, columnspan=3)
    cnv.create_image((image_tk.width()/2), (image_tk.height()/2), anchor=tk.CENTER, image=image_tk)

    return(image_index)


#Button

""" 
def prev_image(image_index):
    
    if image_index > 0:
        image_index -= 1
        show_image(image_index)


def next_image(image_index):
    
    if image_index < len(images_tk)-1:
        image_index += 1
        show_image(image_index)

"""

def next_image(image_index, images_tk):
    if image_index < len(images_tk)-1:
        image_index += 1
        show_image(image_index)


def prv_image(image_index, images_tk):
    if image_index > 0:
        image_index -= 1
        show_image(image_index)


"""



"""


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
