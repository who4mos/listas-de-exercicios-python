n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

avg = (n1+n2) / 2

print(f"Media: {avg:.1f}")

if avg == 10:
    print("Aprovado com distincao")
elif avg >= 7:
    print("Aprovado")
else:
    print("Reprovado")
