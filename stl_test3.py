import os
import numpy as np
from PIL import Image
from stl import mesh

def load_stl(file_path):
    # Charge le fichier STL et renvoie les données du maillage
    mesh_data = mesh.Mesh.from_file(file_path)
    return mesh_data


def slice_stl_to_png(mesh_data, output_folder, num_slices):
    min_z = np.min(mesh_data.v0[:, 2])
    max_z = np.max(mesh_data.v0[:, 2])
    for i in range(num_slices):
        z = min_z + (max_z - min_z) * i / (num_slices - 1)
        slice_mesh = mesh.Mesh(np.array([v for v in mesh_data.data if np.all(v[:, 2] >= z)]))
        slice_mesh.save(os.path.join(output_folder, f"slice_{i}.stl"))


def stl_to_png(stl_file, output_folder, num_slices):
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    mesh_data = load_stl(stl_file)
    slice_stl_to_png(mesh_data, output_folder, num_slices)

if __name__ == "__main__":
    stl_file = "/Users/borotmarion/Downloads/22Lattice-TPL.stl"
    output_folder = "/Users/borotmarion/Documents/EPFL - MA/MA4/Project_ALCHEMY/sliced_png"
    num_slices = 10
    stl_to_png(stl_file, output_folder, num_slices)
