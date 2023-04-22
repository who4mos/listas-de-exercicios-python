strawberries = float(input("Quantidade de morango (Kg): "))
apples = float(input("Quantidade de macas (Kg): "))

price = 0

if strawberries <= 5:
    price += strawberries * 2.5
else:
    price += strawberries * 2.2

if apples <= 5:
    price += apples * 1.8
else:
    price += apples * 1.5

if strawberries + apples > 8 or price > 25:
    price *= .9

print(f"Valor total: R${price:.2f}")
