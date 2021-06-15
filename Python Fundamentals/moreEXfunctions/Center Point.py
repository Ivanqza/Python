def center_point(x1, y1, x2, y2):
    if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
        print(f'({int(x1)}, {int(y1)})')
    else:
        print(f'({int(x2)}, {int(y2)})')


center_point(float(input()), float(input()), float(input()), float(input()))