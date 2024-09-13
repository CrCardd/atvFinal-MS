def produto(x, y):
    if y <= 1:
        return x
    return x + produto(x, y-1)




mult_ando = int(input('Informe o multiplicando:\n>> '))
mult_ador = int(input('Informe o multiplicador:\n>> '))

resp = produto(mult_ando, mult_ador)

print(f'O resultado da soma do multiplicando pelo numero de vezes do multiplicador é: {resp}.')
