year = int(input("Informe o ano: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"O ano {year} e bissexto")
else:
    print(f"O ano {year} nao e bissexto")
