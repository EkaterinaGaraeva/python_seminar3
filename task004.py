# 4. Найти корни квадратного уравнения Ax² + Bx + C = 0
# D = B^2 - 4AC
# x1,2 = (-B +- sqrt(D)) / 2A

import math

def quar(a, b, c):
    desc = b**2 - 4*a*c
    x1 = (-b + math.sqrt(desc))/(2*a)
    x2 = (-b - math.sqrt(desc))/(2*a)
    return (x1, x2)

print(quar(1, -4, 1))
