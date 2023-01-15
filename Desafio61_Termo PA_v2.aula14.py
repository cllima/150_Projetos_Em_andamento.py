## Refaça o Desafio 51, lendo o primeiro Termo e a razão de uma PA, mostrando os 10
# primeiros termos da progressão usando o estrutura while.
print('='*30)
print(f'{" 10 TERMO DE UMA PA v.2 ":=^30}')
print('='*30)

primeiro=int(input('1º Termo da PA: '))
razão=int(input('Razão da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo} -> ',end='')
    termo += razão
    cont += 1
print('\nACABOUUUUUUUUUU!!!')