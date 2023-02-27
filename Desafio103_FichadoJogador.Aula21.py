#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um
# jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo
# que algum dado não tenha sido informado corretamente.
print('Ficha do Jogador'.center(30).upper())
print('='*30)
## Tipo de validação de Dados

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

#Programa Principal
nome=str(input('Nome do Jogador: '))
gols=str(input('Número de Gols: '))
if gols.isnumeric():
    gols=int(gols)
else:
    gols=0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome,gols)
