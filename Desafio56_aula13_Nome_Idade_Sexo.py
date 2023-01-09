# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do Homem mais velho.
# Quantas Mulheres tem menos de 20 anos.
print('='*60)
print(f'{"NOME, IDADE E SEXO => Média Idade/Homem+Velho/Mulheres<20":^60}')
print('='*60)

soma_idade=0
media_idade=0
maioridade_homem=0
nome_velho=''
total_mulher20=0
for pessoas in range(1,5):
    print(f'----- {pessoas}ª Pessoa -----')
    nome=str(input('Nome: ')).strip().upper()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade

    if pessoas == 1 and sexo in 'Mm':
        maioridade_homem=idade
        nome_velho=nome
    if sexo in 'Mm' and idade > maioridade_homem:
        maioridade_homem=idade
        nome_velho=nome
    if sexo in 'Ff' and idade < 20:
        total_mulher20 += 1

media_idade= soma_idade/4
print(f'A média de Idade do grupo é de {media_idade:.0f} anos.')
print(f'O homem mais velho tem {maioridade_homem} anos e se chama {nome_velho}.')
print(f'Ao todo temos {total_mulher20} mulhere(s) com menos de 20 anos.')
