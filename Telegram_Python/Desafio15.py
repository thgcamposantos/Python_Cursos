lista_carros = ['BMW X6' , 'BMW I5' , 'BMW I8']
for c in lista_carros:
    print(c)

carro_usuario = str(input('Digite o nome carro: '))
if carro_usuario in lista_carros:
    print(f'Temos em estoque , esta no estacionamento {lista_carros.index(carro_usuario)}')
else:
    print('Desculpe, este carro não está disponivel')