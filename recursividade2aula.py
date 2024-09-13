def fatorial(num):
    if num <= 0:
        return 1

    return num * fatorial(num-1)



num = int(input('INFORME UM NUMERO INTEIRO POSITIVO:\n>> '))

print(f'O somatório de {num} é: {fatorial(num)}')
