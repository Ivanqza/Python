def center_point(x1, y1, x2, y2, x3, y3, x4, y4):
    if (abs(x1) + abs(y1)) + (abs(x2) + abs(y2)) >= (abs(x3) + abs(y3)) + (abs(x4) + abs(y4)):
        if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
            print(f'({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})')
        else:
            print(f'({int(x2)}, {int(y2)})({int(x1)}, {int(y1)})')
    else:
        if abs(x3) + abs(y3) <= abs(x4) + abs(y4):
            print(f'({int(x3)}, {int(y3)})({int(x4)}, {int(y4)})')
        else:
            print(f'({int(x4)}, {int(y4)})({int(x3)}, {int(y3)})')

center_point(float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()))