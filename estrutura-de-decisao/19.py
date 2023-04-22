x = int(input("Digite um numero menor que 1000: "))

while x >= 1000:
    x = int(input("O numero precisa ser menor que 1000: "))

phrases = []

ones = x  % 10
tens = x % 100 // 10
hundreds = x // 100

if hundreds:
    phrases.append(f"{hundreds} centena{'' if hundreds == 1 else 's'}")

if tens:
    phrases.append(f"{tens} dezena{'' if tens == 1 else 's'}")

if ones:
    phrases.append(f"{ones} unidade{'' if ones == 1 else 's'}")


final_phrase = ", ".join(phrases)
print(final_phrase[::-1].replace(' ,', ' e ', 1)[::-1])
