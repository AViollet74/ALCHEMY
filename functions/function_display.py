import tkinter as tk 
from PIL import Image, ImageTk
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
from time import sleep

def convert_black_image (black_image_path):
    """Upload black image and create ImageTk.PhotoImage object
    Args : black image path
    return :converted ImageTk.PhotoImage object of the black image"""

    black_image = Image.open(black_image_path)
    black_image = black_image.resize((600, 600), Image.BILINEAR)      
    black_image_tk = ImageTk.PhotoImage(black_image) 

    return black_image_tk 


def convert_png(nb_slice):
    """Create a list of the png image paths from sliced png image 
    Args : number of the last png image in the png_filled output folder
    TO DO: enter the path of the png_filled output folder
    return :list of image paths"""

    paths = []
    for i in range(nb_slice):
        paths.append("/Users/borotmarion/Documents/EPFL - MA/MA4/Project_ALCHEMY/outputs/png_filled/" + str(i) + ".png")                  #folder path for png
    return paths


def convert(images_paths):
    """Upload image and create ImageTk.PhotoImage object
    Args : list of images paths
    return :list of converted ImageTk.PhotoImage object"""

    images_tk=[]     
    image_names=[]                                           #create empty list

    for i, path in enumerate(images_paths):       
        image = Image.open(path)                                #open image path
        image = image.resize((600, 600), Image.BILINEAR)      #resize image
        image_tk = ImageTk.PhotoImage(image)                    #create ImageTk.PhotoImage object
        images_tk.append(image_tk)                              #add ImageTk.PhotoImage object to the list
        image_names.append("Image " + str(i+1))

        
    return images_tk, image_names


def show_image_tk(frame, image_tk, image_name):
    """Create a Canvas widget and display a single image
       Args: frame, 
            list images_tk, list of ImageTk.PhotoImage objects,
            image_index, image index in the list that corresponds to the images that is displayed"""      

    

    #lbl1 = tk.Label(frame, text=image_name, bg="lavender")                        #Label creation
    #lbl1.grid(row=1, column=1)                                                   #Label position in the frame

    #btn_prev = tk.Button(frame, text="Prev")                                    #Button "Previous" creation
    #btn_prev.grid(row=1, column=0)                                              #Button "Prev" position in the frame

    #btn_next = tk.Button(frame, text="Next")                                    #Button "Next" creation
    #btn_next.grid(row=1, column=2)                                              #Button "Next" position in the frame                


    cnv1 = tk.Canvas(frame, width=600, height=600, bg="black")
    cnv1.grid(row=0, columnspan=3)
    cnv1.create_image((image_tk.width()/2), (image_tk.height()/2), anchor=tk.CENTER, image=image_tk)
    

def show_black_image_tk(frame, black_image_tk):
    

    #lbl2 = tk.Label(frame, text="Printing in process", bg="lavender")                        #Label creation
    #lbl2.grid(row=1, column=1)                                                   #Label position in the frame

    #btn_prev = tk.Button(frame, text="Prev")                                    #Button "Previous" creation
    #btn_prev.grid(row=1, column=0)                                              #Button "Prev" position in the frame

    #btn_next = tk.Button(frame, text="Next")                                    #Button "Next" creation
    #btn_next.grid(row=1, column=2)                                              #Button "Next" position in the frame                


    cnv2 = tk.Canvas(frame, width=600, height=600, bg="black")
    cnv2.grid(row=0, columnspan=3)
    cnv2.create_image((black_image_tk.width()/2), (black_image_tk.height()/2), anchor=tk.CENTER, image=black_image_tk)
   




#Button

class ImageSelector:
    def __init__(self, frame, image_index, images_tk, image_names):
        self.frame = frame
        self.image_index = image_index
        self.images_tk = images_tk
        self.image_names = image_names


    def prev_image(self):
        
        if self.image_index > 0:
            self.image_index -= 1
            self.show_last_image_tk(self.images_tk[self.image_index], self.image_names[self.image_index])


    def next_image(self):
        
        if self.image_index < len(self.images_tk)-1:
            self.image_index += 1
            self.show_last_image_tk(self.images_tk[self.image_index], self.image_names[self.image_index])


    def show_last_image_tk(self, image_tk, image_name):
        """Create a Canvas widget and display a single image
        Args: frame, 
                list images_tk, list of ImageTk.PhotoImage objects,
                image_index, image index in the list that corresponds to the images that is displayed"""      

        

        lbl3 = tk.Label(self.frame, text=image_name)                                 #Label creation
        lbl3.grid(row=1, column=1)                                                   #Label position in the frame

        btn_prev = tk.Button(self.frame, text="Prev", command=self.prev_image)                                    #Button "Previous" creation
        btn_prev.grid(row=1, column=0)                                              #Button "Prev" position in the frame

        btn_next = tk.Button(self.frame, text="Next", command=self.next_image)                                    #Button "Next" creation
        btn_next.grid(row=1, column=2)                                              #Button "Next" position in the frame                


        cnv3 = tk.Canvas(self.frame, width=500, height=500, bg="ivory")
        cnv3.grid(row=0, columnspan=3)
        cnv3.create_image((image_tk.width()/2), (image_tk.height()/2), anchor=tk.CENTER, image=image_tk)
        


"""


#image = Image.open("/home/mborot/Pictures/mont_blanc.jpg")
#image.show()

# MATPLOTLIB

# create figure 
#fig = plt.figure(figsize=(8, 8)) 

# setting values to rows and column variables 
#rows = 2
#columns = 2



#fig = plt.figure(figsize=(8, 8)) 

def show_image_mpl(images_paths, i, columns, rows):

    title = "Image " + str(i+1)

    image = plt.imread(images_paths[i])
    plt.subplot(rows, columns, i+1)
    plt.imshow(image)
    plt.axis('off')
    plt.title(title)
    
    plt.show()

#display.show_image_mpl(images_paths, i, columns, rows)

 """