from math import sqrt, floor


def calculate_distance(x1, y1):
    return sqrt((x1**2) + (y1**2))
# def cartesian_coordinate_longer(x1, y1, x2, y2, x3, y3, x4, y4):
#     a = ((0 - x1) ** 2) + ((0 - y1) ** 2)
#     b = ((0 - x2) ** 2) + ((0 - y2) ** 2)
#     c = ((0 - x3) ** 2) + ((0 - y3) ** 2)
#     d = ((0 - x4) ** 2) + ((0 - y4) ** 2)
#     x = ""
#     y = ""
#     if a + b >= c + d:
#         if a <= b:
#             print(f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})")
#         else:
#             print(f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})")
#     else:
#         if c <= b:
#             print(f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})")
#         else:
#             print(f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
line_a = calculate_distance(x1, y1) + calculate_distance(x2, y2)
line_b = calculate_distance(x3, y3) + calculate_distance(x4, y4)
distance_a = calculate_distance(x1, y1)
distance_b = calculate_distance(x2, y2)
distance_c = calculate_distance(x3, y3)
distance_d = calculate_distance(x4, y4)
if line_a >= line_b:
    if distance_a <= distance_b:
        print(f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})")
    else:
        print(f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})")
else:
    if distance_c <= distance_d:
        print(f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})")
    else:
        print(f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})")