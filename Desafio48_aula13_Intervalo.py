#Faça um programa que calcule a soma entre todos os números que
# são múltiplos de três e que se encontram no intervalo de 1 até 500.


soma = 0  # Acumulador
cont = 0  # Contador
for c in range(1,501,2):
    if c % 3 == 0: ## Só mostrar os que são divididos por 3.
        soma = soma + c ## soma += c
        cont = cont + 1 ## cont += 1
        print(c, end=' ')
print('\nA soma de todos os {} valores solicitados é {}.'.format(cont,soma))
print(f'A soma de todos os {cont} valores solicitados é {soma}.')

print('\nFIM!!!')