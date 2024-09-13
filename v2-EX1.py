
HORA = int(input('Insira salário por hora:\n'))

qtdHora = int(input('Informe o numero de horas normais trabalhadas no ano:\n>> '))
qtdHoraE = int(input('\n\nInforme o numero de horas extras trabalhadas no ano:\n>> '))

valHora = qtdHora * HORA
valHoraE = qtdHoraE * (HORA * 1.5)
result = valHora + valHoraE
poup = result * 0.8

print(f'______________________________________________________\n')
print(f'Valor de horas normais:{valHora} reais\n\n')
print(f'Valor de horas extras: {valHoraE} reais\n\n')
print(f'Total de ganho no ano = {result} reais\n\n')
print(f'Valor a guardar na poupan�a = {poup} reais\n\n');
print(f'______________________________________________________\n')
 