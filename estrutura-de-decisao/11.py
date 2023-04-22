sal = float(input("Digite o salario do colaborador: R$"))

if sal <= 280:
    percent = .2
elif sal <= 700:
    percent = .15
elif sal <= 1500:
    percent = .10
else:
    percent = .05

inc = sal * percent
new_sal = sal + inc

print(f"Salario antes do reajuste: R${sal:.2f}")
print(f"Percentual de aumento aplicado: {percent*100}%")
print(f"Valor aumentado: R${inc:.2f}")
print(f"Novo salario: R${new_sal:.2f}")
