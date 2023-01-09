## Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias=int(input('Quantos dias ficou alugado? '))
km=float(input('Quantos km rodado? '))
pagto=(60*dias)+(0.15*km)

print('O total a pagar e de R$ {:.2f}. '.format(pagto))

