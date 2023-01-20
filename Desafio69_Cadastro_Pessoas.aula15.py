# Crei um programa que leia o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
## A) Quantas pessoas tem mais de 18 anos.
## B) Quantos homens foram cadastrados.
## C) Quantas mulheres tem menos de 20 anos.
## D) Quantas pessoas foram Cadastradas.
## E) Estado Civil.
## F) O programa deve informar a média, e maior e a menor idade.

print('-' * 32)
print('** ANÁLISE DE DADOS DO GRUPO **')
print('-' * 32)
lista = []
total_18 = total_H = total_M20 = cont = situação = 0

soma = 0
while True:
    idade = int(input('Idade: '))
    cont += 1
    lista.append(idade)
    soma += 1

    sexo = ' '
    while sexo not in 'MF':  ## Enquanto não for digitado M/F o programa não vai copilar.
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    est_civil = ' '
    while est_civil not in 'CS':
        est_civil = str(input('Estado Civil [C/S]: ')).strip().upper()[0]
    print('=' * 32)

    if idade >= 18:
        total_18 += 1
    if sexo == 'M':
        total_H += 1
    if sexo == 'F' and idade < 20:
        total_M20 += 1
    if est_civil == 'C':
        situação += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'\nTemos um total de {total_18} pessoas com MAIS de 18 anos. '
      f'\nAo todo temos {total_H} Homem(s) cadastrado. '
      f'\nTemos {total_M20} Mulher(es) com MENOS de 20 anos. '
      f'\nO total de pessoas casadas são {situação}.'
      f'\nA média de Idade das pessoas {sum(lista) / len(lista):.1F} anos. '
      f'\nA MAIOR Idade do cadastro é {max(lista)} anos, e a MENOR Idade é {min(lista)} anos.'
      f'\nTOTAL de {len(lista)} pessoas CADASTRADAS.')
print('\n\033[1:32m ** FIM DO PROGRAMA!!!!')













