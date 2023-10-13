import tkinter as tk 
from PIL import Image, ImageTk
import functions.function_display as display

root = tk.Tk()                  #Tinker window creation
root.title("Images display")

frame = tk.Frame(root)          #frame creation
frame.pack()

images_paths = ["/home/mborot/Pictures/mont_blanc.jpg", "/home/mborot/Pictures/cervin.jpg", "/home/mborot/Pictures/eiger.jpg"]              #list of image's paths
images_tk = []  


#Button

image_index = 0

btn_next = tk.Button(frame, text="Next", command=display.next_image(image_index, images_tk))
btn_prv = tk.Button(frame, text="Before", command=display.prv_image(image_index, images_tk))

btn_next.pack(side=tk.RIGHT)
btn_prv.pack(side=tk.LEFT)

#Display

images_tk = display.convert(images_paths, images_tk)     #list of ImageTk.PhotoImage objects
display.show_image(frame, images_tk)

root.mainloop()




""" 

image1 = Image.open("/home/mborot/Pictures/mont_blanc.jpg")
image1_tk = ImageTk.PhotoImage(image1)

image2 = Image.open("/home/mborot/Pictures/cervin.jpg")
image2_tk = ImageTk.PhotoImage(image2)

canvas = tk.Canvas(frame, width=image1_tk.width(), height=image1_tk.height())  #create cavas to display images
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=image1_tk)


"""
