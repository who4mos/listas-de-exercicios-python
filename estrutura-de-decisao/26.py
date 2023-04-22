import sys

liters = float(input("Litros: "))

gas_or_alcohol = input("""\
Tipo do combustivel:
[A]lcool
[G]asolina
> """)

if gas_or_alcohol.lower() == 'a':
    liter_price = 1.9
    discount_per_liter = .03 if liters <= 20 else .05
elif gas_or_alcohol.lower() == 'g':
    liter_price = 2.5
    discount_per_liter = .04 if liters <= 20 else .06
else:
    print("Opcao invalida")
    sys.exit()

price = liters * liter_price
discount = discount_per_liter * price
final_price = price - discount

print(f"Desconto de R${discount:.2f}")
print(f"Valor final: R${final_price:.2f}")
