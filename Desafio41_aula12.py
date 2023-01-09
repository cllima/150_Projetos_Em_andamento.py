## A confederação nacional de natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.
## Até 9 anos : MIRIM
## Até 14 anos : INFANTIL
## Até 19 anos: JÚNIOR
## Até 25 anos: SÊNIOR
## Acima: MASTER.

y=' CONFEDERAÇÃO NACIONAL DE NATAÇÃO '
print('-'*40)
print('\033[32m{:=^40}\033[m'.format(y))
print('-'*40)

from datetime import date
ano_atual=date.today().year

ano_nasc=int(input('Ano de Nascimento: '))

idade=ano_atual-ano_nasc

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INTANTIL')
elif idade <= 19:
    print('Categoria: JÚNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')







