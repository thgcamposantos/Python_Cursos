def calculo(r , a , l):
    calculo_parede = a * l
    calculo_final = calculo_parede / r
    return calculo_final


rendimento_lata = float(input('Qual o rendimento da tinta: '))
altura_parede = float(input('Qual a altura da parede: '))
largura_parede = float(input('Qual a largura da parede: '))

valor = calculo(rendimento_lata , altura_parede , largura_parede)
print(valor)
