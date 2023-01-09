## Deselvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de
# até 200km e R$ 0,45 para viagens mais longas.

distância=float(input('Qual a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distância:.1f}km.')

if distância <= 200:
    preço=distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de {:.2f}'.format(preço))