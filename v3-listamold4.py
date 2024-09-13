def calculo(x, y):
    return x*y

medLateral = float(input('INFORME A MEDIDA LATERAL DO TERRENO:\n>> '))
medBase = float(input('INFORME A BASE DO TERRENO:\n>> '))
print(f'\n\n\n\n\nÁrea do terreno: {calculo(medLateral,medBase)}\n\nmedidas\n{medLateral}x{medBase}')

