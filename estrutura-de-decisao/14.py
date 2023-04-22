n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

avg = (n1+n2) / 2

concept = None

if avg < 4:
    concept = 'E'
elif avg < 6:
    concept = 'D'
elif avg < 7.5:
    concept = 'C'
elif avg < 9:
    concept = 'B'
elif avg <= 10:
    concept = 'A'

if concept:
    print(f"Notas: {n1:.1f} {n2:.1f}")
    print(f"Media: {avg:.1f}")
    print(f"Conceito: {concept}")

    if concept in "ABC":
        print("APROVADO")
    else:
        print("REPROVADO")

else:
    print("Notas invalidas")
