from math import *

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
A = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
B = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
C = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
p = (A + B + C) / 2
S = sqrt(p * (p - A) * (p - B) * (p - C))
print('Площадь треугольника = ', S)
