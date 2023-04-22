n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

avg = (n1+n2+n3) / 3

if avg == 10:
    print(f"Aprovado com Distincao!\nMedia: {avg:.1f}")
elif avg >= 7:
    print(f"Aprovado!\nMedia: {avg:.1f}")
else:
    print(f"Reprovado!\nMedia: {avg:.1f}")
