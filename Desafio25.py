## Crie um programa que leia o nome de uma pessoa e diga se ele
# tem "SILVA" no nome.
# True ou False

nome=str(input('Digite o seu Nome: ')).strip()
print('O seu nome é {}, e tem a palavra chave? (True ou False): {} '.format(nome,'SILVA' in nome.upper()))
