numeros = [1,2,3,4,5,6,7,8,9,10]
# numeros = list(range(1,11))

for n in numeros:
    if n % 2 == 0:
        print(f'O numero {n} é par')
    else:
        print(f'O numero {n} é impar')
print('fim')