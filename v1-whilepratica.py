total = 0
height = 1
while height > 0:
    height = float(input('Qual a altura da pessoa em centimetros ( 0 - sair )? \n>> '))
    if height == 0:
        break    

    gender = input('Qual o sexo da pessoa (M/F)?\n>> ')
    if gender.upper() == 'M':
        resp = (72.7 * height)-58
    elif gender.upper() == 'F':
        resp = (62.1*height)-44.7
    else:
        print('\nInsira um valor válido!')
        continue

    print(f'Seu peso ideal é: {round(resp,2)}kg')
    total += 1
    

print(f'\n\n\n\nO experimento teve {total} participantes.')
    
    