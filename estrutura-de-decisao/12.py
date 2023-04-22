hour_price = float(input("Valor da hora: R$"))
hours = int(input("Horas trabalhadas: "))

sal = hours * hour_price

if sal <= 900:
    ir_percent = 0
elif sal <= 1500:
    ir_percent = .05
elif sal <= 2500:
    ir_percent = .10
else:
    ir_percent = .20

ir_discount = sal * ir_percent
synd_discount = sal * .03
fgts = sal * .11

total_discount = ir_discount + synd_discount

new_sal = sal - total_discount

print(f"Salario Bruto: ({hours} * {hour_price})\t: R${sal:.2f}")
print(f"(-) IR ({ir_percent*100}%)\t\t\t: R${ir_discount}")
print(f"(-) Sindicato (3%)\t\t: R${synd_discount}")
print(f"FGTS (11%)\t\t\t: R${fgts:.2f}")
print(f"Total de descontos\t\t: R${total_discount:.2f}")
print(f"Salario Liquido\t\t\t: R${new_sal:.2f}")
