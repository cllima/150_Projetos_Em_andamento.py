## Um professor que sortear um dos seus quatros alunos para apagar o quadro. Faça
## um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
a1=str(input('Primeiro Aluno: '))
a2=str(input('Segundo Aluno: '))
a3=str(input('Terceiro Aluno: '))
a4=str(input('Quarto Aluno:  '))
lista = [a1,a2,a3,a4]
escolhido = random.choice(lista)  ## random.choice faz a escolha de itens aleatórios

print('O Aluno escolhido foi {}'.format(escolhido))


'''compras = ['pão','leite','arroz','feijão'] ''' ## Isso é uma lista de compra ('','','','')