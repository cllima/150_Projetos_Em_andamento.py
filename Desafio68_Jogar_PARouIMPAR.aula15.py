# Faça um programa que jogue PAR ou ÍMPAR com o computador, O jogo só será interrompido quando o jogador perder.
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
print('=-='*10)
print("     JOGO DE PAR OU ÍMPAR")
print('=-='*10)

from random import randint
valor=int(input('Diga um VALOR: '))
opção=str(input('PAR ou ÍMPAR [P/I]: '))

computador = randint(1,2)

