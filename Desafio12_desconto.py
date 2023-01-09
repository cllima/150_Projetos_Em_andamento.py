## Faça um algoritmo que leia o preço de um produto R$,
## e mostre seu novo preço, com 5% de desconto.

preço=float(input('Digite o valor do produto a prazo R$ '))
desconto=preço-(preço*5/100)
print('O valor do produto atualmente custa R$ {:.2f}, e com o desconto de 5% vai custar R$ {:.2f}'.format(preço,desconto))
