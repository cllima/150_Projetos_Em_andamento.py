# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o
# MAIOR e o MENOR peso lindos.
print('*'*30)
print(f'{" O MAIOR E O MENOR PESO ":^30}')
print('*'*30)

maior=0
menor=0
for pessoa in range(1,6):
    peso=float(input(f'Informe o peso da {pessoa}º pessoa: '))
    if pessoa==1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O MAIOR peso lido foi {maior}kg.')
print(f'O MENOR pelo lido foi {menor}kg.')
