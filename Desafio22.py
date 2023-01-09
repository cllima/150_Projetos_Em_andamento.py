## Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras Maiúsculas.
# O nome com todas as letras Minúsculas
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome=str(input('Digite seu nome completo: ')).strip()  ## Eliminar os espaços em branco

print('Seu nome em letra Maiúscula é {} '.format(nome.upper()))
print('Seu nome em letra Minúscula é {} ' .format(nome.lower()))
print('Seu nome tem ao todo {} Letras '.format(len(nome)-nome.count(' '))) ## Qtd. de letras (-) menos os espaços, conta apenas as letras.
print('Seu nome tem ao todo {} caracteres '.format(len(nome.strip())))   ## Mostra a qtd de caracteres na frase com os espaços entre as letras.
print('Seu primeiro nome tem {} letras '.format(nome.find(' ')))         ## Encontrou o primeiro nome.
separa=nome.split()
print(separa)    ## Separa em forma de lista e faz a contagem
print('Seu 1º nome é {} e tem {} letras. '.format(separa[0], len(separa[0])))








