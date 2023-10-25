import os
import numpy as np
from PIL import Image
from stl import mesh

def load_stl(file_path):
    # Charge le fichier STL et renvoie les données du maillage
    mesh_data = mesh.Mesh.from_file(file_path)
    return mesh_data

def slice_stl_to_png(mesh_data, output_folder, num_slices):
    # Accédez aux coordonnées des points
    points = mesh_data.points

    # Obtenez le nombre total de points
    num_points = len(points)

    min_z = np.min(points[:, 2])  # Accédez à la colonne Z
    max_z = np.max(points[:, 2])

    for i in range(num_slices):
        z = min_z + (max_z - min_z) * i / (num_slices - 1)
        
        # Filtrer les triangles dont au moins un point est au-dessus de la tranche z
        filtered_triangles = []
        for triangle_indices in mesh_data.vectors:
            triangle = points[triangle_indices]
            if np.any(triangle[:, 2] >= z):
                filtered_triangles.append(triangle_indices)

        if not filtered_triangles:
            continue  # Pas de données pour cette tranche
        
        # Créer un nouveau maillage avec les triangles filtrés
        new_triangles = np.array(filtered_triangles)
        slice_mesh = mesh.Mesh(new_triangles)
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
