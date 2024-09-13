def somatorio(num):
    if num <= 0:
        return 0

    return num + somatorio(num-1)



num = int(input('INFORME UM NUMERO INTEIRO POSITIVO:\n>> '))

print(f'O somatório de {num} é: {somatorio(num)}')
