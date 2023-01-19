# Faça um programa que jogue PAR ou ÍMPAR com o computador, O jogo só será interrompido quando o jogador perder.
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
print('\033[1:34m=-='*10)
print('     JOGO DE PAR OU ÍMPAR')
print('\033[1:34m=-=\033[m'*10)
from random import randint
vitoria=0
while True:
    jogador=int(input('Digite um VALOR [0 a 10]: '))
    computador=randint(0,10)
    total=jogador+computador
    tipo=' '
    while tipo not in 'PI':
        tipo=str(input('PAR ou ÍMPAR [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total {total}', end=' => ')
    if total % 2 == 0: #Se o tatal deu restou zero é igual a PAR.
        print('DEU PAR!!')
    else:
        print('DEU ÍMPAR!!')
    print('=' * 40)

    if tipo == 'P':
        if total % 2 == 0: #Se o tatal deu restou zero é igual a PAR.
            print('PARABÉNS VOCÊ VENCEUUU!!!')
            vitoria+=1
        else:
            print('VOCÊ PERDEUUU!!')
            break

    elif tipo == 'I':
        if total % 2 == 1: #Se o tatal deu restou 1 é igual a ÍMPAR.
            print('PARABÉNS VOCÊ VENCEUUU!!!')
            vitoria+=1
        else:
            print('VOCÊ PERDEUUU!!')
            break

    print('\033[1:32m*** BORA!!! jogar novamente!!! ***\033[m')
    print('*' * 40)
print(f'\033[1:31m*** GAME OVER!! NÂO desanime!!! Você VENCEU {vitoria} vezes ***\033[m')




