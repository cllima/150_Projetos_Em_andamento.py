print('=' * 50)
print(f'{"BOLETIM ESCOLAR - COLÉGIO VACCARO":^50}')
print('=' * 50)
alunos = []
notas = []
cont = 0 #Definindo a variável para calcular - Aprova ou Reprova

num = int(input('Informe número dos Alunos: '))
c = 0
for i in range(num):
    c += 1
    boletim = {'nome': 0, 'n1': 0, 'n2': 0, 'n3': 0, 'n4': 0, 'media':0} ## Dicionário
    boletim['nome'] = input(f'Nome do {c}º Aluno: ')
    boletim['n1'] = float(input('Digite a 1ª nota: '))
    boletim['n2'] = float(input('Digite a 2ª nota: '))
    boletim['n3'] = float(input('Digite a 3ª nota: '))
    boletim['n4'] = float(input('Digite a 4ª nota: '))
    print('=' * 50)

    boletim ['media'] = boletim ['n1'], boletim ['n2'], boletim ['n3'], boletim ['n4']
    alunos.append(boletim)
    notas.append(boletim['media'])
    soma_das_notas = 0

    for nota in notas[cont]: #Garantindo que o índice acompanhará o número de alunos
        soma_das_notas += nota
    boletim['media'] = soma_das_notas / 4
    if boletim['media'] >= 7:
        boletim['media'] = 'Aprovado'
    else:
        boletim['media'] = 'Reprovado'

    cont += 1
print(f'{"Nota dos alunos":^50}')
print('-' * 50)
for aluno in alunos:
    print(f'{aluno["nome"]:.<15}   {aluno["n1"]}   {aluno["n2"]}   {aluno["n3"]}   {aluno["n4"]}   {aluno["media"]}')

print('='*50)
print(f'{"FIM DO PROGRAMA":^50}')
print('='*50)
