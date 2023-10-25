import os
import numpy as np
from PIL import Image
from OpenGL.GL import *
from OpenGL.GLUT import *

def load_stl(file_path):
    # Charge le fichier STL et renvoie les coordonnées des vertices
    vertices = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('vertex'):
                parts = line.split()
                x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                vertices.append((x, y, z))
    return vertices

def create_image(width, height):
    # Crée une image vide
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutCreateWindow("STL Slicer")
    glOrtho(0, width, 0, height, -1, 1)
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

def save_image(file_path, width, height):
    # Capture et enregistre l'image en cours
    data = glReadPixels(0, 0, width, height, GL_RGBA, GL_UNSIGNED_BYTE)
    image = Image.frombytes("RGBA", (width, height), data)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image.save(file_path)

def main(input_stl, output_folder, num_slices):

    vertices = load_stl(input_stl)
    if not vertices:
        print("Aucune donnée de vertices dans le fichier STL.")
    else:
        min_z = min(v[2] for v in vertices)
        max_z = max(v[2] for v in vertices)

    width, height = 800, 600  # Largeur et hauteur de l'image
    create_image(width, height)
    for i in range(num_slices):
        z = min_z + (max_z - min_z) * i / (num_slices - 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_TRIANGLES)
        for v1, v2, v3 in vertices:
            if v1[2] >= z and v2[2] >= z and v3[2] >= z:
                glVertex2f(v1[0], v1[1])
                glVertex2f(v2[0], v2[1])
                glVertex2f(v3[0], v3[1])
        glEnd()
        save_image(os.path.join(output_folder, f"slice_{i}.png"), width, height)

if __name__ == "__main__":
    input_stl = "/Users/borotmarion/Downloads/CubicLattice-136-0.4-0.8.stl"
    output_folder = "/Users/borotmarion/Documents/EPFL - MA/MA4/Project_ALCHEMY/sliced_png"
    num_slices = 10
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    main(input_stl, output_folder, num_slices)
