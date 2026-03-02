quadrado = lambda y: y * 2

def tabuada(x):
    for i in range(0,11):
        print(f'{x} x {i} = {x * i}')

numero = int(input('Numero: '))
(tabuada(quadrado(numero)))