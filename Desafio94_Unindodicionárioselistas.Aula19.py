# Crie um programa que leia: Nome, sexo, e idade de várias pessoas, guardando os dados de cada pessoa em um
# dicionário e todos os dicionários em uma LiSta. No final mostre:
#A) Quantas pessoas foram cadastradas.
#B) A média de idade do grupo.
#C) Uma lista com todas as Mulheres.
#D) Uma lista com todas as pessoas com idade acima da média.
print('=' * 40)
print(f'{"Unindo dicionários e listas":^40}'.upper())
print('=' * 40)
## Guardando vários Dicionários em uma LISTA.
galera=[] ##Lista
pessoa={} ##Dicionário
soma = média = 0

while True:
    #pessoa.clear() ## Esvazia pessoa para uma nova pessoa. Não precisou usar>>>

    pessoa['nome']=str(input('Nome: '))

    while True:  # Validando sexo M ou F.
        pessoa['sexo']=str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro!! Responda apenas M ou F.')

    pessoa['idade']=int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy()) ### Faz uma copia de pessoa para Galera.

    while True:
        resp=str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro!! Responda apenas Sim ou Não.')
    if resp == 'N':
        break
## Até aqui foram a leitura dos DADOS.
print('='*40)
print(galera) ## Lista com vários Dicionários.
print('='*40)

print(f'<<< ANALIZE DOS DADOS COLETADOS >>>'.center(40))
print('<>'*20)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma/len(galera)
print(f'B) A média de idade do grupo é {média:.1f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for pessoas in galera:
    if pessoas["sexo"] in 'F':
        print(f'{pessoas["nome"]}, ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for pessoas in galera:
    if pessoas["idade"] >= média:
        for k,v in pessoas.items():
            print(f' {k} = {v}; ', end='')
        print()

print('-'*40)
print(f'<<< FIM DO PROGRAMA >>>'.center(40))


