frutas = ['Maçã' , 'Banana' , 'Manga' , 'Uva']
print(frutas)

indice_lista = int(input('Qual indice voce deseja mudar: '))
nome_novo_lista = str(input('Qual fruta voce deseja colocar no lugar: '))

frutas[indice_lista] = nome_novo_lista
frutas.append('abacaxi')

print(frutas)