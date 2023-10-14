import tkinter as tk
from PIL import Image, ImageTk

# Liste des chemins d'accès aux images
chemins_images = ["/home/mborot/Pictures/mont_blanc.jpg", "/home/mborot/Pictures/cervin.jpg", "/home/mborot/Pictures/eiger.jpg"]

# Créez la fenêtre principale
root = tk.Tk()
root.title("Affichage de plusieurs images")

# Créez un widget Canvas pour afficher les images
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

# Liste pour stocker les objets ImageTk.PhotoImage
images_tk = []

# Chargez les images et créez les objets ImageTk.PhotoImage
for chemin in chemins_images:
    image = Image.open(chemin)
    image = image.resize((100, 100), Image.ANTIALIAS)
    image_tk = ImageTk.PhotoImage(image)
    images_tk.append(image_tk)

# Coordonnées d'affichage pour les images
x, y = 10, 10

# Affichez les images dans une boucle
for image_tk in images_tk:
    canvas.create_image(x, y, anchor=tk.NW, image=image_tk)
    x += image_tk.width() + 10  # Espacement horizontal entre les images

# Exécutez la boucle principale de Tkinter
root.mainloop()

"""
import tkinter as tk
from PIL import Image, ImageTk

class ImageDisplayApp:
    def __init__(self, root, image_paths):
        self.root = root
        self.image_paths = image_paths
        self.current_index = 0

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.next_button = tk.Button(root, text="Image suivante", command=self.show_next_image)
        self.next_button.pack()

        self.prev_button = tk.Button(root, text="Image précédente", command=self.show_previous_image)
        self.prev_button.pack()

    def show_image(self):
        if 0 <= self.current_index < len(self.image_paths):
            image_path = self.image_paths[self.current_index]
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo

    def show_next_image(self):
        self.current_index += 1
        if self.current_index >= len(self.image_paths):
            self.current_index = 0
        self.show_image()

    def show_previous_image(self):
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.image_paths) - 1
        self.show_image()

if __name__ == "__main__":
    root = tk.Tk()
    image_paths = ["/home/mborot/Pictures/mont_blanc.jpg", "/home/mborot/Pictures/cervin.jpg", "/home/mborot/Pictures/eiger.jpg"]  # Remplacez par les chemins de vos images
    
    app = ImageDisplayApp(root, image_paths)
    
    app.show_image()
    
    root.mainloop()
"""