## Escreva um programa que leia um número inteiro qualquer e peça para o usuário
## escolher qual será a base de conversão:
## 1- binário
## 2- Octal
## 3- Hexadecimal
from time import sleep
num=int(input('Digite um número inteiro: '))
print('''Escolha uma das Bases para conversão:
[ 1 ] - Converter para BINÁRIO
[ 2 ] - Converter para OCTAL
[ 3 ] - Converter para HEXADECIMAL
[ 4 ] - Sair''')

opção=int(input('Sua opção: '))
print('')
print('\033[34mPROCESSANDO...!!!\n\033[m')
sleep(1.6)
if opção == 1:
    print('O número {} convertido para BINÁRIO é igual a {}.'.format(num,bin(num)[2:]))
elif opção == 2:
    print('O número {} convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}.'.format(num,hex(num)[2:]))
elif opção == 4:
    print('\033[7:40m******* FIM DO PROGRAMA *******\033[m')
else:
    print('\033[31mexcept ValueError: OPÇÃO INVÁLIDA!!! '
          '\nEscolha entre 1 a 3! Tente novamente!')

