## Escreva uma programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
## O programa deverá escrever na tela se o usuário venceu = PARABÉNS ou perdeu = Tente novamente.
import random
from random import randint
from time import sleep

computador=randint(0,5) ##  Faz o computador "PENSAR"
#print('Pensei no número: {}'.format(computador))

print('Vou pensar em um número entre 0 e 5. Tente adivinhar.')
lista=[0,1,2,3,4,5]
jogador=random.choice(lista)

print('-=-'*18)

jogador = int(input("Em que número eu pensei? "))  ## jogador tentar adivinhar
print('\033[33mPROCESSANDO...!!!\033[m\n')
sleep(1.2)

if jogador == computador:
    print('PARABÉNS!! Você Venceu!!!')
elif jogador>=6:
    print('Eu disse número de 0 a 5!!')
else:
    print('O Computador VENCEU! Ele pensou no número {} e não no {}!!'.format(computador, jogador))

print('')
print("\033[31m***** FIM DO JOGO *****")

