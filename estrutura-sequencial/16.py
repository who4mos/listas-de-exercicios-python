from math import ceil

LITER_COVERAGE = 3
LITERS_PER_CAN = 18
PRICE_PER_CAN = 80

area = float(input("Metros quadrados da area a ser pintada: "))

can_coverage = LITER_COVERAGE * LITERS_PER_CAN
cans = ceil(area / can_coverage)

total_price = cans * PRICE_PER_CAN

print(f"Voce precisara de {cans} lata(s) de tinta.")
print(f"O preco total sera de R${total_price:.2f}")
