import math


def calculate_distance(x1, y1):
    return math.sqrt((x1**2) + (y1**2))
    # # a = (x1**2) + (y1**2)
    # # b = (x2**2) + (y2**2)
    # a = ((0 - x1)**2) + ((0 - y1)**2)
    # b = ((0 - x2)**2) + ((0 - y2)**2)
    # if a <= b:
    #     return print(f"({floor(x1)}, {floor(y1)})")
    # else:
    #     return print(f"({floor(x2)}, {floor(y2)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
distance_a = calculate_distance(x1, y1)
distance_b = calculate_distance(x2, y2)

if distance_a <= distance_b:
    print(f"({math.floor(x1)}, {math.floor(y1)})")
else:
    print(f"({math.floor(x2)}, {math.floor(y2)})")