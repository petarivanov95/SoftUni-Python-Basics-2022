from math import pi

shape = input()
size_1 = float(input())

if shape == "square":
    area = size_1**2

elif shape == "rectangle":
    size_2 = float(input())
    area = size_1 * size_2

elif shape == "circle":
    area = (size_1**2) * pi

elif shape == "triangle":
    size_2 = float(input())
    area = (size_1 * size_2) * 0.5

print(f"{area:.3f}")
