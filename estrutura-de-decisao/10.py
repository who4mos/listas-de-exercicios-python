x = input("""\
Em que turno voce estuda?
[M]atutino
[V]espertino
[N]oturnoo
> """).lower()

if x == 'm':
    print("Bom dia!")
elif x == 'v':
    print("Boa tarde!")
elif x == 'n':
    print("Boa noite!")
else:
    print("Valor invalido!")
