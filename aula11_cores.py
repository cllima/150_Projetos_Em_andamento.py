from time import sleep
n1=int(input('Primeiro número: '))
n2=int(input('Segundo númerro: '))

## Criando uma Tabela de cores:
cores={'limpa':'\033[m',
       'branco':'\033[97m',
       'vermelho':'\033[31m',
       'verde':'\033[32m',
       'amarelo': '\033[33m',
       'azul':'\033[34m',
       'lilas':'\033[35m',
       'cinza':'\033[37m',
              'pretobranco':'\033[7;97m'}

print('Calma!!!, estamos processando a informação!!')
print("\033[4;31;40mANALISANDO...!!!\033[m")
print("\033[4;30;43mANALISANDO...!!!\033[m")
print("\033[7;30;47mANALISANDO...!!!\033[m")
sleep(1.5)

print('Os valores são \033[31m{}\033[m e \033[34m{}\033[m...!!! '.format(n1,n2))
# OU
print('Os valores são {}{}\033[m e {}{}\033[m...!!!'.format(cores['branco'],n1, cores['verde'],n2))

