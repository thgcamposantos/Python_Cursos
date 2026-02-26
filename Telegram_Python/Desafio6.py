frutas = ['Maçã' , 'Banana' , 'Manga' , 'Uva']
print(frutas)

fruta_retirar = str(input('Qual fruta deseja remover da lista: '))
if fruta_retirar in frutas:
    frutas.remove(fruta_retirar)
    frutas.pop()
else:
    print('Fruta nao encontra na lista')

print(frutas)