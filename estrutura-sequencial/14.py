w = float(input("Peso dos peixes em quilos: "))

if w > 50:
    excess = w - 50
else:
    excess = 0

fine = excess * 4

print(f"Voce trouxe {excess} quilos acima do permitido. Com isso "
      f"tera que pagar uma multa de R${fine:.2f}")
