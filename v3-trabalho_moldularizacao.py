def calculo(notas):
    tot = 0
    for i in range(len(notas)):
        tot+= notas[i]
    return tot/len(notas)

def show(name, mat, media):
    print('----------------------------------------------------------------')
    print(f'O aluno(a) {name} com matricula {mat} tem {media} de media.\n\n\n');
    print('----------------------------------------------------------------')

mat = 1

while mat != 0:
    notas = [0 for _ in range(4)]
    mat = input('Qual a sua matricula? (0 - sair):\n>> ')
    name = input('Insira seu nome:\n>> ')
    
    for i in range(len(notas)):
        notas[i] = int(input(f'\n\nInforme a {i+1}° nota:\n>>'))
    
    media = calculo(notas)
    show(name, mat, media)