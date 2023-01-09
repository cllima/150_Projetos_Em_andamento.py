# Crei um programa que mostre na Tela todos os números pares e Ímpares que estão no intervalo entre 0 e 50.
print(' ===== CONTAGEM DE NÚMEROS PARES / ÍMPARES =====')

print('''Escolha uma das OPÇÔES:
[ 1 ] Números PARES
[ 2 ] Números ÍMPARES''')
opção=int(input('Números PAR ou ÍMPAR: '))

while opção <= 0 or opção > 2:  #  opção errada.
    opção = int(input('\033[35mOPÇÂO INVÁLIDA!!! \nEscolha entre as opções 1 ou 2!!!\033[m'))

inicio=int(input('Digite o primeiro número: '))
while inicio != 0: # não pode digitar número diferente de zero.
    i= int(input('\033[31mNÚMERO INVÁLIDA!!! \nDigite (ZERO) !!!\033[m'))
fim=int(input('Digite o segundo número: '))

if opção == 1:
    print('Contagem de Números PARES!!!')
    for cont in range(inicio,fim+1,2):
        print(cont, end='. ')
    print('\nFIMMMM!!!!')
elif opção == 2:
    print('Contagem de Números ÍMPARES!!!')
    for cont in range(inicio,fim+2,3):
        print(cont, end='. ')
    print('\nFIMMMM!!!!')
