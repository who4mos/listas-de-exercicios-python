from math import ceil, trunc

LITER_COVERAGE = 6  # cobertura de um litro da tinta em m²

LITERS_PER_CAN = 18
CAN_PRICE = 80

LITERS_PER_GALLON = 3.6
GALLON_PRICE = 25

# area com folga de 10%
area = float(input("Digite a area a ser pintada em m²: ")) * 1.1

# somente latas
can_coverage = LITERS_PER_CAN * LITER_COVERAGE
only_cans = ceil(area / can_coverage)
print()
print("Comprando apenas latas de 18 litros, voce precisara de "
      f"{only_cans} latas (R${only_cans*CAN_PRICE:.2f})")

# somente galoes
gallon_coverage = LITERS_PER_GALLON * LITER_COVERAGE
only_gallons = ceil(area / gallon_coverage)
print()
print("Comprando apenas galoes de 3.6 litros, voce precisara de "
      f"{only_gallons} galoes (R${only_gallons*GALLON_PRICE:.2f})")

# misturado
mix_cans = trunc(area / can_coverage)
mix_gallons = ceil((area % can_coverage) / gallon_coverage)
mix_total_price = mix_cans*CAN_PRICE + mix_gallons*GALLON_PRICE
print()
print("Evitando o desperdicio de tinta, voce deve comprar:")
print(f"{mix_cans} latas de 18 litros (R${mix_cans*CAN_PRICE:.2f})")
print(f"{mix_gallons} galoes de 3.6 litros "
      f"(R${mix_gallons*GALLON_PRICE:.2f})")
print(f"Dando um total de R${mix_total_price:.2f}")
print()
