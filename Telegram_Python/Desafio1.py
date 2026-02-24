ponto_carne = int(input('Qual o ponto da carne em Celsius: '))

if ponto_carne < 48:
    print('Precisa ficar mais tempo no forno')
elif ponto_carne > 47 and ponto_carne < 54:
    print('Selada')
elif ponto_carne >= 54 and ponto_carne < 60:
    print('Ao ponto para o mal')
elif ponto_carne >= 60 and ponto_carne < 65:
    print('Ao ponto')
elif ponto_carne >= 65 and ponto_carne < 71:
    print('Ao ponto para o bem')
else:
    print('Bem passada')

