questions = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

positives = 0

for q in questions:
    a = input(q + " [S/n]: ")

    if not a or a in "Ss":
        positives += 1

if positives < 2:
    print("Inocente")
elif positives == 2:
    print("Suspeito")
elif 3 <= positives <= 4:
    print("Cumplice")
else:
    print("Assasino")
