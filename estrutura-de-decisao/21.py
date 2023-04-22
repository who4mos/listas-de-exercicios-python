MIN = 10
MAX = 600

withdraw = int(input("Quanto deseja sacar: R$"))
while withdraw < MIN or withdraw > MAX:
    withdraw = int(input("Minimo R$10,00 | Maximo R$600,00\n> R$"))
remaining = withdraw

n100 = remaining // 100
remaining -= n100 * 100
    
n50 = remaining // 50
remaining -= n50 * 50

n10 = remaining // 10
remaining -= n10 * 10

n5 = remaining // 5
remaining -= n5 * 5

n1 = remaining // 1
remaining -= n1 * 1

print(f"""\
Notas de 100: {n100}
Notas de 50:  {n50}
Notas de 10:  {n10}
Notas de 5:   {n5}
Notas de 1:   {n1}\
""")
