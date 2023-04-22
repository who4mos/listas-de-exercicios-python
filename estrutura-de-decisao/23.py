from math import trunc

x = float(input("Digite um numero: "))

if x == trunc(x):
    print(f"{x:.0f} e um numero inteiro")
else:
    print(f"{x} e um numero real")
