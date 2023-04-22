#                    ate 5kg                mais de 5kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

meat = input("""\
Qual carne deseja comprar?
[F]ile Duplo
[A]lcatra
[P]icanha
> """).lower()

while len(meat) != 1 or meat not in "fap":
    meat = input("Escolha uma das opcoes acima: ")

kg = float(input("Quantos quilos: "))

if meat == 'f':
    meat_name = "File Duplo"
    kg_price = 4.9 if kg <= 5 else 5.8
elif meat == 'a':
    meat_name = "Alcatra"
    kg_price = 5.9 if kg <= 5 else 6.8
else:
    meat_name = "Picanha"
    kg_price = 6.9 if kg <= 5 else 7.8


price = kg * kg_price
card_discount = price * .05

print(f"""\
Carne:                    {meat_name}
Quantidade:               {kg}Kg
Preco:                    R${price:.2f}
Desconto cartao Tabajara: R${card_discount:.2f}
Preco com cartao:         R${price - card_discount:.2f}\
""")
