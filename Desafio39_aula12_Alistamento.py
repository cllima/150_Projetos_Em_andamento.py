## Faça um programa que leia o ano de nascimento de um jovem e informe,
## de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo de alistamento.
## O programa deverá mostrar o tempo que falta ou o que passou do prazo.

y=' ALISTAMENTO MILITAR '
print('_'*40)
print('\033[32m{:=^40}\033[m'.format(y))
print('-'*40)

from datetime import date
ano_atual=date.today().year # Pega a ano atual.

while True: # limitar 4 digitos
    nasc = (input('Digite o ano de nascimento: ')).strip()
    if len(str(nasc)) == 4 and nasc.isnumeric():
        break

print('''Gênero:
[ 1 ] - MASCULINO
[ 2 ] - FEMININO ''')
opção= int(input('Informe: '))
print('')

idade=ano_atual-int(nasc) ## Tem que colocar int.

if opção == 1:
    print('Você nasceu em {}, e tem {} anos em {} e do sexo MASCULINO!!'.format(nasc, idade, ano_atual))

    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!!!')
    elif idade < 18:
        saldo= 18 - idade
        print('Ainda falta(m) {} ano(s) para o ALISTAMENTO.'.format(saldo))
        ano = ano_atual + saldo
        print('Seu ALISTAMENTO será em {}.'.format(ano))
    elif idade > 18:
        saldo= idade - 18
        print('Já deveria ter se ALISTADO há {} ano(s).'.format(saldo))
        ano = ano_atual - saldo
        print('Seu ALISTAMENTO foi em {}.'.format(ano))
elif opção == 2:
    print('\033[4:31:40mPelas leis do BRASIL, mulheres não tem ALISTAMENTO Obrigatório!!!\033[m')
    print('\033[34mContinue a preencher o Formulário!!!')

else:
    print('\033[31mGÊNERO INVÁLIDO!!! '
          '\nEscolha entre as opções: 1 ou 2!')
    exit()