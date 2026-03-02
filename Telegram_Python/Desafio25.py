situacao = lambda x: 'Par' if x % 2 == 0 else 'impar'

numero1 = int(input('Numero: '))

print(f'O {numero1} é : {situacao(numero1)}')