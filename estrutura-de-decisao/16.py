import sys
from math import sqrt

a = float(input("a: "))

if a == 0:
    print("Equacao nao e de segundo grau")
    sys.exit()

b = float(input("b: "))
c = float(input("c: "))

delta = b ** 2 - 4*a*c

if delta < 0:
    print("A equacao nao possui raizes reais")
    sys.exit()

elif delta == 0:
    x1 = (-b + sqrt(delta)) / (2*a)
    print(f"x = {x1}")
else:
    x1 = (-b + sqrt(delta)) / (2*a)
    x2 = (-b - sqrt(delta)) / (2*a)
    print(f"x1 = {x1}\nx2 = {x2}")
