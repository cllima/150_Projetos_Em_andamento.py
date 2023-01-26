## Crie um programa que tenha uma Tupla única com nomes de produtos e seus respectivos
## preços, na sequência.
## No final, mostre uma listagem de preços, organizando os dados em forma tabular..

print('='*45)
print(f'{"TABELA DE PRODUTOS E PREÇOS":^40}')
print('='*45)
soma = 0

listagem=('Caneta',2.50,'Lápis',1.50,'Apagador',5.90,'Teclado',65,'Computador'
      ,2650,'Mouse',89.5,'Cadeira',750,'Mesa',1050,'Borracha',2.00,'Mochila',120.02)

for posição in range(0, len(listagem)):
	if posição % 2 == 0:
		print(f'{listagem[posição]:.<35}', end='')
	else:
		print(f'R$ {listagem[posição]:>7.2f}')

		soma += listagem[posição] ### Não esquecer de colocar o += senão não soma todos os ìntens da lista
print('-'*45)
print(f"{'VALOR TOTAL':.<35}R${soma:>8.2f}")

print('='*45)
print(f'{"FIM DO PROGRAMA":^40}')
print('='*45)