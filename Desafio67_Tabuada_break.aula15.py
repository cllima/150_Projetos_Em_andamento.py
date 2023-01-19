# Faça um programa que mostre a Tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
print('******** TABUADA ********')

while True: ## Loop infinito

    num = int(input('Quer ver a TABUADA de qual valor?: '))
    print('=' * 35)
    if num < 0: ## Fecha o programa ao digitar número negativo.
        break
    for cont in range(1, 11):
        print(f'{num} x {cont:2} = {num*cont}')

    print('='*35)
print('*** PROGRAMA DE TABUADA ENCERRADO!!! ***')




