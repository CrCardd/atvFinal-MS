num = int(input('Informe um número para calcular a tabuada do mesmo:\n>> '))
limit = int(input('\n\nInforme até onde deverá ir a tabuada:\n>>'))

print('\n\n\nT A B U A D A')
print('\n-----------------------------------------------')
for i in range(1,limit+1):
    print(f'{i}\tX\t{num}\t=\t{i*num}')