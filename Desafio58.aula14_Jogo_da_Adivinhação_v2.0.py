#Melhore o jogo do Desafio 28 onde o computador vai 'PENSAR' em um número entre 0 a 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
#palpites foram necessários para vencer.
print('JOGO DE ADIVINHAÇÃO V2.0')
print('='*30)

from random import randint
from time import sleep

computador=randint(0,10) ##  Faz o computador "PENSAR"
print('Sou seu PC, pensei em um número entre 0 e 10. \nAgora tente adivinha qual foi?') ## jogador tentar adivinhar

## Criando uma Variável
acertou=False
palpites=0

while not acertou:
    jogador = int(input("Qual seu palpite?: "))
    if jogador > 10:
        print('\n\033[1:31mVocê não SABE LER...!!! \nEu disse números de 0 a 10 kkk, Tente novamente plis.\033[m')
    palpites+=1
    print('\033[1:33m\nPROCESSANDO...!!!\033[m\n')
    sleep(0.8)

    if jogador == computador:
        acertou=True
        print(f'\033[1:32mPARABÉNS!!\033[m Você Venceu, acertou com {palpites} tentativas.!!!')
    else:
        if jogador <= computador:
            print('MAIS... Tá quente!!! Tente mais uma vez!!')
        elif jogador >= computador:
            print('MENOS... Tá frio!!! mais uma chance!!!')

print('')
print("\033[1:31m***** FIM DO JOGO *****")









