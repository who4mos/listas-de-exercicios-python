letter = input()

vowels = "aeiou"

if letter.isalpha():
    if letter.lower() in vowels:
        print("Vogal")
    else:
        print("Consoante")
else:
    print("Nao e letra")

