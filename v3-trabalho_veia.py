def check_play(tab, jog):
    if tab[0][0] == tab[0][1] and tab[0][1] == tab[0][2] and tab[0][2] != '-' or  tab[1][0] == tab[1][1] and tab[1][1] == tab[1][2] and tab[1][2] != '-' or   tab[2][0] == tab[2][1] and tab[2][1] == tab[2][2] and tab[2][2] != '-' or tab[0][0] == tab[1][0] and tab[1][0] == tab[2][0] and tab[2][0] != '-' or tab[0][1] == tab[1][1] and tab[1][1] == tab[2][1] and tab[2][1] != '-' or tab[0][2] == tab[1][2] and tab[1][2] == tab[2][2] and tab[2][2] != '-' or tab[0][0] == tab[1][1] and tab[1][1] == tab[2][2] and tab[2][2]  != '-'or tab[0][2] == tab[1][1] and tab[1][1] == tab[2][0] and tab[2][0] != '-':
        if jog%2 == 0:
            print('O JOGADOR 1 VENCEU!')
        else:
            print('O JOGADOR 2 VENCEU!')
        return True
        







check = True
jog = 0
tabuleiro = [['-' for _ in range(3)] for _ in range(3)]


for i in range(3):
    for j in range(3):
        print(f'{i*3 + j}',end='\t')
    print('\n')


while check:
        
        
    if jog%2 == 0:
        print('JOGADOR 1')
    else:
        print('JOGADOR 2')
    pos = int(input('Insira a posição que deseja jogar:\n>> '))

    posL = int(pos/3)
    posC = int(pos%3)

    if tabuleiro[posL][posC] != '-':
        print('\nLOCAL INVALIDO!\n')
        jog-=1
        continue
    
    if jog%2 == 0:
        tabuleiro[posL][posC] = 'X'
    else:
        tabuleiro[posL][posC] = 'O'
    
    for i in range(3):
        for j in range(3):
            print(f'{tabuleiro[i][j]}',end='\t')
        print('\n')
        
        
    if check_play(tabuleiro, jog):
        break
    jog+=1
    
    

    