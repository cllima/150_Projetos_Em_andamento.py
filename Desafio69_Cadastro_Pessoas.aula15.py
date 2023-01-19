#Crei um programa que leia o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
## A) Quantas pessoas tem mais de 18 anos.
## B) Quantos homens foram cadastrados.
## C) Quantas mulheres tem menos de 20 anos.

print('-' * 32)
print('** ANÁLISE DE DADOS DO GRUPO **')
print('-' * 32)
lista=[]
total_18=0
total_H=0
total_M20=0
cont=0
while True:
    idade = int(input('Idade: '))
    cont += 1
    lista.append(idade)

    sexo=' '
    while sexo not in 'MF': ## Enquanto não for digitado M/F o programa não vai copilar.
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('=' * 32)

    if idade >= 18:
        total_18+=1
    if sexo == 'M':
        total_H+=1
    if sexo == 'F' and idade < 20:
        total_M20+=1

    resp=' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Temos um total de {total_18} pessoas com MAIS de 18 anos. '
          f'\nAo todo temos {total_H} Homem(s) cadastrado. '
          f'\nE temos {total_M20} Mulher(es) com MENOS de 20 anos. '
          f'\nTOTAL de {len(lista)} pessoas CADASTRADAS.')
print('\n\033[1:32m ** FIM DO PROGRAMA!!!!')













