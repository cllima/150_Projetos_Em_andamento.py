## Faça um programa que leia nome e média de um aluno, guardando também a situação em um Dicionário.
## No final, mostre o conteúdo da estrutura na tela.
# Média Maior que 7 - Aprovado
print('=' * 40)
print(f'{"Dicionário com Python":^40}'.upper())
print('=' * 40)
aluno= {}
aluno['nome']=str(input('Nome do Aluno: '))
aluno['media']=float(input(f'A Média do {aluno["nome"]}: ')) ## Colocar em aspas duplas luno["nome"] ""

if aluno['media'] >= 7:
    aluno['situação']='APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇÂO'
else:
    aluno['situação'] = 'REPROVADO'
print('='*40)
print(aluno)
print('  Keys    Values')
print('='*40)

for k, v in aluno.items():
    print(f'{k} é igual a {v:.>19}.')





