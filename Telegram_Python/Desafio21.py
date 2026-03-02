cidades = {
    'Brasil': 'Brasilia' ,
    'Argentina': 'Buenos Aires' ,
    'Chile': 'Santiago' ,
    'Uruguai': 'Montevideu' ,
    'Bolivia': 'Bogota'
}

pais_usuario = str(input('Digite o nome do pais: '))
if pais_usuario in cidades:
    print(f'A capital de pais é: {pais_usuario} é capital {cidades[pais_usuario]}')
else:
    print('Desculpe, nao encontramos')