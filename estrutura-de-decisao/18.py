days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

date = input("Digite a data (dd/mm/aaaa): ")

day, month, year = map(int, date.split('/'))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    days[2] += 1

if day <= days[month]:
    print("Data valida!")
else:
    print("Data invalida!")
