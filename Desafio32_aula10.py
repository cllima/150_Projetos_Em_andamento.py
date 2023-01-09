## Faça uma programa que leia um ano qualquer e mostre se ele é BISSSEXTO.
## Explo.: 2022 é um ano Bissexto Sim ou Não.
from time import sleep
from datetime import date

ano=int(input('Que ano quer analizar? Coloque (0) para analizar o ano atual: '))
print('PROCESSANDO...')
sleep(0.5)

if ano ==0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('O ano {} é BISSEXTO!!! '.format(ano))
else:
    print('O ano {} NÂO é BISSEXTO!! '.format(ano))
