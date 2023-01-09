## Crie uma programa que faça o computador jogar Jokenpô com você.
### Expl.: Pedra, Papel  e Tesoura - vc irá jogar com o PC.
print('👊🖐 ✌ JOGO DO JOKENPÔ 👊🖐 ✌')
from random import randint
from time import sleep

## Tabela de cores:
cores={'limpa':'\033[m',
       'branco':'\033[40m',
       'vermelho':'\033[31m',
       'verde':'\033[32m',
       'verde_bold':'\033[1:32m',
       'amarelo': '\033[33m',
       'azul':'\033[34m',
       'lilas':'\033[35m',
       'cinza':'\033[37m',
       'pretobranco':'\033[7;30m',
       'underline':'\033[4m'}

itens=('PEDRA','PAPEL','TESOURA')
computador = randint(0,2)
#print('O computador escolheu {}'.format(itens[computador]))

print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador=int(input('Qual é a sua jogada: '))

while jogador < 0 or jogador > 2:  # Se o jogador escolher a opção errada
    jogador = int(input('{}JOGADA INVÁLIDA!!! Escolha entre 0 e 2{}'.format(cores['vermelho'],cores['limpa'])))
    quit()  # faz o programa para de rodar sozinho

print('{}JO{}'.format(cores['verde'],cores['limpa']))
sleep(0.6)
print('{}KEN{}'.format(cores['azul'],cores['limpa']))
sleep(0.6)
print('{}PÔ!!!!{}'.format(cores['vermelho'],cores['limpa']))
sleep(0.6)

print('-='*12)
print('Computador Jogou: {}'.format(itens[computador]))
print('Jogador    jogou: {}'.format(itens[jogador]))
print('-='*12)

if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('{}EMPATE!{}'.format(cores['azul'],cores['limpa']))
    elif jogador == 1:
        print('{}PARABÉNS, O JOGADOR VENCEU!{}'.format(cores['verde_bold'],cores['limpa']))
    elif jogador == 2:
        print('{}COMPUTADOR VENCEU!{}'.format(cores['vermelho'],cores['limpa']))
    else:
        print('JOGADA INVÁLIDA!!!')

elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('{}COMPUTADOR VENCEU!{}'.format(cores['vermelho'], cores['limpa']))
    elif jogador == 1:
        print('{}EMPATE!{}'.format(cores['azul'],cores['limpa']))
    elif jogador == 2:
        print('{}PARABÉNS, O JOGADOR VENCEU!{}'.format(cores['verde_bold'],cores['limpa']))
    else:
        print('JOGADA INVÁLIDA!!!')

elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('{}PARABÉNS, O JOGADOR VENCEU!{}'.format(cores['verde_bold'],cores['limpa']))
    elif jogador == 1:
        print('{}COMPUTADOR VENCEU!{}'.format(cores['vermelho'], cores['limpa']))
    elif jogador == 2:
        print('{}EMPATE!{}'.format(cores['azul'],cores['limpa']))

print('')
print('======  FIM DO JOGO =====')



