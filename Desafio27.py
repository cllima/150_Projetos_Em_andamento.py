## Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente.
# Expl.: Ana Maria de Souza
# Primeiro nome: Ana
# Segundo nome: Souza

nome=str(input('Digite seu nome completo: ')).strip().split() ## .split separa em forma de lista.
print('Muito prazer em te conhecer!!')
print('Seu primeiro nome é {} '.format(nome[0]))
print('Seu ultimo nome é {} '.format(nome[-1]))


