# Crie um programa que leia 2 valores e mostre um menu na tela:
## [1] SOMAR
## [2] MULTIPLICAR
## [3] MAIOR
## [4] Novos Números
## [5] Sair do Programa
## O programa deverá realizar a operação solicitada em cada caso.

print('=-=-=-= Criando um Menu de Opções =-=-=-=')
from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção=0
while opção != 5:
    print('''   \033[33m [ 1 ] SOMA
    [ 2 ] MULTIPLICAÇÂO
    [ 3 ] MAIOR
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa \033[m''')
    opção=int(input('>>>Digite sua Opção: '))
    print('=*=' * 10)

    if opção == 1:
        somar = n1+n2
        print(f'\033[1:34mA SOMA dos números {n1} + {n2} = {somar}.\033[m')
        print('=*=' * 10)

    elif opção == 2:
        mult = n1 * n2
        print(f'\033[1:34mA MULTIPLICAÇÂO dos números {n1} x {n2} = {mult}.\033[m')
        print('=*=' * 10)

    elif opção == 3:
        if n1 > n2:
            maior = n1
        elif n1 < n2:
            maior = n2
        print(f'\033[1:34mEntre os números {n1} e {n2} o MAIOR é {maior}.\033[m')
        print('=*=' * 10)

    elif opção == 4:
        print('Informe os números novamente!!!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('    \033[32mAGUARDE PROCESSANDO!!!\033[m')
        print('    \033[32mAGUARDE PROCESSANDO!!!\033[m')
        print('=*=' * 10)

    elif opção == 5:
        print('\033[1:32mFINALIZANDO... FINALIZANDO... FINALIZANDO...\033[m')
        sleep(0.8)
        print('=*=' * 10)

    else:
        print('\033[1:31mOPÇÂO INVÁLIDA!! INFORME AS OPÇÕES ENTRE 1 A 5!!!\033[m')
        print('=*=' * 15)

    sleep(1.5)
print('\033[34mFIM DO PROGRAMA!!! Volte Sempre!!')



