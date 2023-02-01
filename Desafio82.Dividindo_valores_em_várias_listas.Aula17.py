# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois, crie 2 listas extras que vão conter apenas os valores PARES
# e os valores ÍMPARES digitados, respectivamente.
## No final mostre os 3 conteúdos das listas geradas.
print('=' * 40)
print(f'{"Dividindo valores em várias listas":^40}'.upper())
print('=' * 40)
num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um valor: ')))
    num.sort()
    par.sort()
    impar.sort()

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break

for i, v in enumerate(num):  ### i==Indice, v==Valor
    if v % 2 == 0:     ## Para saber se é PAR ou ìMPAR
        par.append(v)
    else:
        impar.append(v)
print('=' * 40)

print(f'Foram digitados {len(num)} números, sendo {min(num)} o MENOR número'
      f'\ne o {max(num)} MAIOR número.')
print(f'A Lista completa: {num}' 
    f'\nA lista com Valores PARES: {par}'
    f'\nA lista com Valores ÍMPARES: {impar}')