def check_play(tab):    
    check = False
    h = ''
    v = ''
    for i in range(3):
        h = tab[i][0] + tab[i][1] + tab[i][2]
        v = tab[0][i] + tab[1][i] + tab[2][i]
        if h == 'XXX' or v == 'XXX':
            print('O JOGADOR 1 VENCEU!')
            check = True
        
        if h == 'OOO' or v == 'OOO':
            print('O JOGADOR 2 VENCEU!')
            check = True
    
    z = tab[0][0] + tab[1][1] + tab[2][2]
    y =  tab[0][2] +  tab[1][1] +  tab[2][0]
    
    if z == 'XXX' or y == 'XXX':
        print('O JOGADOR 1 VENCEU!')
        check = True
    if z == 'OOO' or y == 'OOO':
        print('O JOGADOR 2 VENCEU!')
        check = True
    
    return check
        
    
    
        



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
    
    

    