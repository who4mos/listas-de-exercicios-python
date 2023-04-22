a = float(input("Digite um numero: "))
b = float(input("Digite outro numero: "))
c = float(input("Digite outro numero: "))

big = small = None

if a > b: # a > b
    if b > c: # a > b > c
        big = a
        small = c
    elif a > c: # a > b e c > b
        big = a
        small = b
    else: # a > b e c > b e c > a
        big = c
        small = b
else: # b > a
    if a > c: # b > a > c
        big = b
        small = c
    elif b > c: # b > a e c > a
        big = b
        small = a
    else: # b > a e c > a e c > b
        big = c
        small = a

print(f"Maior: {big}")
print(f"Menor: {small}")
