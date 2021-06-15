from math import pi
figure_type = input()

if figure_type == "square":
    side = float(input())
    area = side * side
elif figure_type == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif figure_type == "circle":
    r = float(input())
    area = pi * r * r
elif figure_type == "triangle":
    c = float(input())
    h = float(input())
    area = c * h / 2

print(f"{area:.3f}")
