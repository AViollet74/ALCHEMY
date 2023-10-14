import tkinter as tk 
from PIL import Image, ImageTk
from matplotlib.pyplot import imread
import functions.function_display as display



root = tk.Tk()                                                              #Tinker window creation
root.title("Images display")

frame = tk.Frame(root)                                                      #Frame creation
frame.pack()

lbl = tk.Label(frame, text="Image 1", bg="lavender")                        #Label creation
lbl.grid(row=1, column=1)                                                   #Label position in the frame

btn_prev = tk.Button(frame, text="Prev")                                    #Button "Previous" creation
btn_prev.grid(row=1, column=0)                                              #Button "Prev" position in the frame

btn_next = tk.Button(frame, text="Next")                                    #Button "Next" creation
btn_next.grid(row=1, column=2)                                              #Button "Next" position in the frame


images_paths = ["/home/mborot/Pictures/mont_blanc.jpg", "/home/mborot/Pictures/cervin.jpg", "/home/mborot/Pictures/eiger.jpg"]              #list of images paths
images_tk = display.convert(images_paths)                                                                                                   #list of uploaded of ImageTk.PhotoImage objects = images

image_index=0                                                               #index of the image in the images_tk list that we want to display
display.show_image(frame, images_tk, image_index)                           #display of the image that corresponds ton the image_index in the images_tk list

root.mainloop()




""" 

#Image redimensionnee avec bouton et legende en bas :)

image = Image.open("/home/mborot/Pictures/mont_blanc.jpg")
image = image.resize((500, 500), Image.ANTIALIAS)
image_tk = ImageTk.PhotoImage(image)

cnv = tk.Canvas(frame, width=500, height=500, bg="ivory")
cnv.create_image((image_tk.width()/2), (image_tk.height()/2), anchor=tk.CENTER, image=image_tk)
cnv.grid(row=0, columnspan=3)

lbl = tk.Label(frame, text="Image 1", bg="lavender")
lbl.grid(row=1, column=1)

btn_prev = tk.Button(frame, text="Prev")
btn_prev.grid(row=1, column=0)

btn_next = tk.Button(frame, text="Next")
btn_next.grid(row=1, column=2)



#Image taille reelle avec bouton sur les bords

lbl = tk.Label(frame, text="Layer 1", bg="lavender")
lbl.pack(side=tk.BOTTOM)

btn_prev = tk.Button(frame, text="Prev")
btn_prev.pack(side=tk.LEFT)

btn_next = tk.Button(frame, text="Next")
btn_next.pack(side=tk.RIGHT)

image = Image.open("/home/mborot/Pictures/mont_blanc.jpg")
image_tk = ImageTk.PhotoImage(image)

cnv = tk.Canvas(frame, width=image_tk.width(), height=image_tk.height(), bg="ivory")
cnv.pack()

cnv.create_image((image_tk.width()/2), (image_tk.height()/2), anchor=tk.CENTER, image=image_tk)

"""
