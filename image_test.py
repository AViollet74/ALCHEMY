import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
import functions.function_display as display  

# create figure 
fig = plt.figure(figsize=(8, 8)) 

# setting values to rows and column variables 
rows = 2
columns = 2

images_paths = ["/home/mborot/Pictures/mont_blanc.jpg", "/home/mborot/Pictures/cervin.jpg", "/home/mborot/Pictures/eiger.jpg"]              #list of image's paths
 

#read images
images_read = display.read(images_paths)


#add plot and show images
display.show_plot(fig, columns, rows, images_read)