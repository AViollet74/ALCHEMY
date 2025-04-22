import questionary

skip=0
thickness=questionary.select(
"Select layer thickness",
choices=["0.08 mm", "0.10 mm", "0.16 mm", "0.20 mm"]).ask()
layer_thickness=float(thickness[:4])

print(thickness, "\n" , type(thickness))


print(layer_thickness, "\n" , type(layer_thickness))
