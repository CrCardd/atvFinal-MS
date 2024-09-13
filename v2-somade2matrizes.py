linhas  = int(input('\nInsira a quantitade de linhas que a matriz terá:\n>> '))
colunas = int(input('\nInsira a quantitade de colunas  que a matriz terá:\n>> '))
qtdMtrz = int(input('\nInsira a quantiade de matrizes que terá:\n>> '))

mtrz = [[[0 for _ in range(colunas)] for _ in range(linhas)] for _ in range(qtdMtrz)]

print(mtrz)

for m in range(qtdMtrz):
    for lin in range(linhas):
        for col in range(colunas):
            mtrz[m][lin][col] = int(input(f'Insira o valor da posição {lin}x{col} da matriz {m}:\n>> '))
            

print('\n\n\nSOMA DAS MATRIZES:\n\n\n')
resp = 0

for lin in range(linhas):
    for col in range(colunas):
        resp = 0
        for m in range(qtdMtrz):
            resp += mtrz[m][lin][col]
            
        print(f'{resp}', end='\t')
    print('\n')
