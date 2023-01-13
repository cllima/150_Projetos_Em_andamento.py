# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar desconsidere-o TBM.

soma_par = 0
cont_par = 0
soma_impar = 0
cont_impar = 0
for c in range(1,7):
    num = int(input('Digite 0 {}º valor: '.format(c)))
    if num % 2 == 0: #Divididi por 2
        soma_par += num
        cont_par += 1
    elif num % 2 != 0:
        soma_impar += num
        cont_impar += 1

print(f'Foi informado {cont_par} números PARES e {cont_impar} Ímpares '
      f'\ne a soma de PARES foi {soma_par} e a soma de ÍMPAR foi {soma_impar}.')
