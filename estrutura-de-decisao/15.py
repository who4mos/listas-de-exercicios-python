a = int(input("Digite o primeiro lado: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))

if a+b>c and b+c>a and a+c>b:
    print(f"Os lados {a}, {b} e {c} podem formar um triangulo", end=" ")
    if a == b == c:
        print("equilatero")
    elif a != b and a != c and b != c:
        print("escaleno")
    else:
        print("isosceles")
else:
    print(f"Os lados {a}, {b} e {c} nao podem formar um triangulo")
