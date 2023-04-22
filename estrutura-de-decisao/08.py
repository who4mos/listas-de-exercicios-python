p1 = float(input("Preco do primeiro produto: R$"))
p2 = float(input("Preco do segundo produto: R$"))
p3 = float(input("Preco do terceiro produto: R$"))

small = None

if p1 > p2:
    if p2 > p3:
        small = p3
    elif p1 > p3:
        small = p2
    else:
        small = p2
else:
    if p1 > p3:
        small = p3
    elif p2 > p3:
        small = p1
    else:
        small = p1

print(f"Voce deve comprar o produto que custa R${small:.2f}")
