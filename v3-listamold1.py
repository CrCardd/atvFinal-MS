def calculo(valLitro, valPag):
    return valPag/valLitro


name = input('Informe seu nome:\n>>')
valLitro = float(input('Informe o valor por litro da gasolina:\n>> '))
valPag = float(input('\n\nInforme o valor que será gasto para abastecer:\n>>'))

print(f'\n\n{name}. Com R${valPag} você será capaz de abastecer {round(calculo(valLitro, valPag),2)} Litros de gasolina')

