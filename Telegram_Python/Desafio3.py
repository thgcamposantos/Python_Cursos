funcionarios = ['Ana' , 'Marcos' , 'Alice' , 'Pedro' , 'Sophia' , 'Bruno' , 'Melissa']
turno_dia = ['Ana' , 'Marcos' , 'Alice' , 'Melissa']
turno_noite = ['Pedro' , 'Sophia' , 'Bruno']
tem_carro = ['Marcos' , 'Alice' , 'Bruno' , 'Melissa']

funcionarios_nao_carros = set(funcionarios).difference(tem_carro)
print(funcionarios_nao_carros)
funcionarios_carros_noite = set(tem_carro).intersection(turno_noite)
print(funcionarios_carros_noite)
funcionarios_carros_dia = set(tem_carro).intersection(turno_dia)
print(funcionarios_carros_dia)