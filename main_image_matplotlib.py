import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib.pyplot import imread
import functions.function_display as display  


# code for displaying multiple images with row and colomne in one figure 

# create figure 
fig = plt.figure(figsize=(8, 8)) 

# setting values to rows and column variables 
rows = 2
columns = 2

images_paths = ["/home/mborot/Pictures/mont_blanc.jpg", "/home/mborot/Pictures/cervin.jpg", "/home/mborot/Pictures/Eiger.jpg", "/home/mborot/Pictures/mont_cenis.jpg"]              #list of image's paths
 

#add plot and show images
#display.show_plot(images_paths, columns, rows)



for i in range(0, columns*rows):
    title = "Image " + str(i+1)

    image = plt.imread(images_paths[i])
    fig.add_subplot(rows, columns, i+1)
    plt.imshow(image)
    plt.axis('off')
    plt.title(title, fontsize=16)

plt.show()






"""
# code for displaying multiple images as a line in one figure 
  
#import libraries

from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Liste des chemins des images
images_paths = ["/home/mborot/Pictures/mont_blanc.jpg", "/home/mborot/Pictures/cervin.jpg", "/home/mborot/Pictures/Eiger.jpg", "/home/mborot/Pictures/mont_cenis.jpg"]    


# Créez une nouvelle figure Matplotlib
fig = plt.figure(figsize=(10, 5))  # Ajustez la taille de la figure selon vos besoins

# Utilisez une boucle for pour charger et afficher chaque image
for i, image_path in enumerate(images_paths):

    title = "Image " + str(i+1)

    img = mpimg.imread(image_path)  # Chargez l'image à partir du chemin
    plt.subplot(1, len(images_paths), i + 1)
    plt.imshow(img)  # Affichez l'image
    plt.axis('off')
    plt.title(title)
    
plt.show()
# Affichez la figure


"""