class ficha_aluno:
    codigo = 0
    nome = ''
    telefone = ''
    mail = ''
    def __init__(self, codigo, nome, telefone, mail):
        self.codigo = codigo
        self.nome = nome
        self.telefone = telefone
        self.mail = mail
    
    
codigo = int(input('Informe o código:\n>> '))
nome = input('Informe o nome do aluno:\n>> ')
telefone = input('Informe o telefone do aluno:\n>> ')
mail = input('Informe o email do aluno:\n>> ')

aluno = ficha_aluno(codigo,nome,telefone,mail)
