def dobro_numero(n):
    return n * 2

def quadrado_numero(n):
    return n ** 2

numero_usuario = int(input('Numero: '))
chamada_funcao = quadrado_numero(dobro_numero(numero_usuario))

print(chamada_funcao)