#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

a=input('Digite algo: ')
print('O tipo primitivo desse valor é ',type(a))
print('Só tem espaços? ',a.isspace())        # somente espaços
print('É um número? ',a.isnumeric())         # somente números
print('É alfabético? ',a.isalpha())          # somente Alfabético
print('É alfanumérico? ',a.isalnum())        # somente Alfanumérico
print('Está em maiúsculas? ',a.isupper())    # somente Maiúscula
print('Está em minúsculas? ',a.islower())    # somente Minúscula
print('Está capitalizada? ',a.istitle())     # somente Maiúscula + Minúscula na frase

## versão 3.7 do python não precisa mais usar .format (), apenas coloque um f antes das aspas ''
print(f'É um número? {a.isnumeric()}')

print(f'É {a.isalnum()} que {a} é Alfanumérico;')






