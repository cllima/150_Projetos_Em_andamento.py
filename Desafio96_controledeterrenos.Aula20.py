## Faça um programa que tenha uma função chamada área(), que receba as dimenções de uma terreno
# retangular (largura e comprimento) e mostre a área do terreno.

print('controle de terrenos'.center(30).upper())
print('='*30)
def area(l,c):
    area=l*c
    print(f'A área de um terreno é {l}x{c} total área {area}m².')

# Programa Principal
l=float(input('LARGURA (m): '))
c=float(input('COMPRIMENTO (m): '))
area(l,c)



