## Crie um programa que leia 3 notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida.
## Média abaixo de 5.0: REPROVADO
## Média entre 5.0 e 6.9: RECUPERAÇÂO
## Média 7.0 ou superior: APROVADO

from statistics import median
nota1=float(input('Primeira NOTA: '))
nota2=float(input('Segunda NOTA: '))
nota3=float(input('Terceira NOTA: '))

média=(nota1+nota2+nota3)/3
#média=median([n1,n2,n3])
## Criando uma Tabela de cores:
cores={'limpa':'\033[m',
       'branco':'\033[40m',
       'vermelho':'\033[31m',
       'verde':'\033[32m',
       'amarelo': '\033[33m',
       'azul':'\033[34m',
       'lilas':'\033[35m',
       'cinza':'\033[37m',
       'pretobranco':'\033[7;30m',
       'underline':'\033[4m'}

print('A média das suas notas no semestre foi {:.2f} pontos.'.format(média))

if média < 5:
    print('Você está {}"REPROVADO"{}!!!'.format(cores['vermelho'],cores['limpa']))
elif média >= 5 and média < 7:
    print('Você está de {}"RECUPERAÇÂO"{}!!!'.format(cores['amarelo'],cores['limpa']))
elif média >= 7:
    print('PARABÉNS você foi {}"APROVADO"{}!!!'.format(cores['verde'],cores['limpa']))

