a = float(input("Digite um numero: "))
b = float(input("Digite outro numero: "))
c = float(input("Digite outro numero: "))

big = None

if a > b: # a > b
    if b > c: # a > b > c
        big = a
    elif a > c: # a > b e c > b
        big = a
    else: # a > b e c > b e c > a
        big = c
else: # b > a
    if a > c: # b > a > c
        big = b
    elif b > c: # b > a e c > a
        big = b
    else: # b > a e c > a e c > b
        big = c

print(f"Maior: {big}")
