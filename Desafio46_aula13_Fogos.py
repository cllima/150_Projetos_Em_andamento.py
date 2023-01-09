# Faça um programa que mostre na Tela uma contagem regressiva para o estou de fogos de artificio,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
## FELIZ ANO NOVO => BUM FOGOS ESTOURANDO!!!
from time import sleep

print('===== CONTAGEM REGRESSIVA ======')
print('''OPÇÔES:
[ 1 ] Ascender com segurança
[ 2 ] Os Fogos Falharam''')
opção=int(input('Digite uma Opção: '))

if opção == 1:
    for cont in range(10,-1,-1):
        print(cont)
        sleep(0.6)
    print('\033[32mBUM!!!  BUM!!!  POOOOWW!!!! \nFELIZZZ ANO NOVOOOO')

elif opção == 2:
    print('Retorne a Loja para a troca dos FOGOS!!!')
else:
    print('Opção INVÁLIDA!!!')


