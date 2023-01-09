## Escreva um programa que leia dois números inteiros  e compare-os,
## mostrando na tela uma mensagem:
# - O primeiro valor é MAIOR.
# - O segundo valor é MAIOR.
# - Não existe valor MAIOR, os dois são iguais.

n1=int(input('Primeiro número: '))
n2=int(input('Segundo número: '))
print('\033[34mPRIMEIRO: {}\033[m \n\033[32mSEGUNDO: {}\033[m'.format(n1,n2))

if n1 > n2:
    print('O PRIMEIRO valor é \033[34mMAIOR\033[m que o SEGUNDO!!')
elif n1 < n2:
    print('O SEGUNDO valor e \033[32mMAIOR\033[m que o PRIMEIRO!!')
else:
    print('NÂO, existe valor \033[31mMAIOR\033[m, ou dois são \033[31mIGUAIS\033[m!!!')

