per_hour = float(input("Quanto voce ganha por hora? R$"))
hours = int(input("Horas trabalhadas no mes: "))

sal = hours * per_hour
print(f"+ Salario Bruto: R${sal:.2f}")

ir = sal * .11
print(f"- IR (11%) : R${ir:.2f}")

inss = sal * .08
print(f"- INSS (8%) : R${inss:.2f}")

sind = sal * .05
print(f"- Sindicato (5%) : R${sind:.2f}")

liq = sal - (ir + inss + sind)
print(f"= Salario Liquido : RS{liq:.2f}")
