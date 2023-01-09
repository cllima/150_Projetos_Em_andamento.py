# Desenvolva um programa que lei o primeiro termo e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.
print('='*30)
print(f'{" 10 TERMO DE UMA PA ":=^30}')
print('='*30)
primeiro=int(input('Informe o 1º Termo da PA: '))
razão=int(input('Informe a Razão da PA: '))
décimo=primeiro + (10-1) * razão
for c in range(primeiro,décimo + razão,razão):
    print(c, end=' →')
print('\nACABOUUUUUUUUUU!!!')


