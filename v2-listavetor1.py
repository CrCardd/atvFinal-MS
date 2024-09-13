notas = []

count = 0

alunos = []

for i in range(5):
    alunos.append(input('Qual seu nome?\n>> '))
    notas.append(float(input('Qual sua nota?\n>>')))
    
print('\n\n\n\nNOTAS ACIMA DE 7.5:\n\n\n')

for i in range(len(alunos)):
    if notas[i] > 7.5:
        print(f'O aluno {alunos[i]} tirou nota acima de 7.5\nNOTA: {notas[i]}\n\n')
        count+=1
        

print(f'{count} alunos tiraram nota superior a 7.5.')