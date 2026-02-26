idade_usuario = int(input('Idade: '))
if idade_usuario < 13:
    print('Voce é uma criança')
elif idade_usuario > 13 and idade_usuario <= 19:
    print('Voce é um adolescente')
else:
    print('voce é um adulto')