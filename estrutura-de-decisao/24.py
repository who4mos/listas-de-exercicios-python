from math import trunc

x = float(input("Digite um numero: "))
y = float(input("Digite outro numero: "))

op = input(f"""Qual operacao deseja realizar?
(+)  - Soma
(-)  - Subtracao
(*)  - Multiplicacao
(/)  - Divisao
(%)  - Resto da divisao
(**) - Exponenciacao
> """)

while op not in "+-**%/":
    op = input("Entre uma das operacoes acima: ")

if op == '+':
    result = x + y
elif op == '-':
    result = x - y
elif op == '*':
    result = x * y
elif op == '/':
    result = x / y
elif op == '%':
    result = x % y
else:
    result = x ** y

even_or_odd = "par" if result % 2 == 0 else "impar"
int_or_decimal = "inteiro" if result == trunc(result) else "real"
if result > 0:
    pos_or_neg = "positivo"
elif result < 0:
    pos_or_neg = "negativo"
else:
    pos_or_neg = "neutro"

print(f"""\
Resultado: {result if int_or_decimal == 'real' else int(result)}
Um numero {pos_or_neg}, {int_or_decimal} e {even_or_odd}.\
""")
