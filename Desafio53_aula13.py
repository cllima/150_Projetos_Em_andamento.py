# Crie uma programa que leia uma frase qualquer e diga se ele é um
# polindromo, desconsiderando os espaços.
# Ex: após a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo,
# anotaram a data da maratona.

frase=str(input('Digite uma frase: ')).strip().upper()
palavras=frase.split()
junto =''.join(palavras)
inverso = junto[::-1]  ### Simplificando o FOR.

print(f'O inverso de {junto} é igual [{inverso}].')
if inverso == junto:
    print('Temos um PALINDROMO!!!')
else:
    print('A frase digitado não é um PALINDROMO!!!')
