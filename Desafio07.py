## Desenvolva um programa que leia as três notas de um
## aluno, calcule e mostre a sua média.

from time import sleep
nome=input('Digite seu nome: ')
n1=float(input('Primeira nota do Aluno: '))
n2=float(input('Segunda nota da Aluno: '))
n3=float(input('Terceira nota do Aluno '))
soma=(n1+n2+n3)
media=soma/3
print('Aluno(a) {}, a média das sua notas foram {:.1f} pontos.'.format(nome,media))

## Outra forma de escrever mais simples ##
print('Aluno(a) {}, a média das suas notas foram {:.1f} pontos.'.format(nome,(n1+n2+n3)/3))

print('\033[33m**** ANALIZANDO ****')
sleep(1.5)

print('')
if media>=7:
    print('\033[34mPARABÉNS!!! Você foi APROVADO, com média superior a 7 pontos.!!')
else:
    print('\033[31mREPROVADO... Você precisa estudar mais, sua média foi inferior a 7 pontos.!!!')





