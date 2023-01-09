# Crie uma programa que leia o Ano de nascimento de 7 pessoas. No final, mostre quantas
# pessoas ainda não atingiram a maioridade e quantas já são maiores de 21 anos.
from datetime import date
ano_atual=date.today().year
print('='*30)
print(f'{"DETECTOR DE MAIORIDADE":^30}')
print('='*30)

total_maior=0
total_menor=0
for pessoas in range(1,8):
    nasc=int(input(f'Em que ano a {pessoas}ª pessoa nasceu: '))
    idade=ano_atual-nasc
    if idade >= 18:
        total_maior+=1
    else:
        total_menor+=1
print(f'Ao todo temos {total_maior} pessoas MAIORES de IDADE!')
print(f'E {total_menor} pessoas MENORES de IDADE!')



