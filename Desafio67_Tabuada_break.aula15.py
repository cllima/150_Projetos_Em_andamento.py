# Faça um programa que mostre a Tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
print('******** TABUADA ********')

while True:
    print('=' * 35)
    num = int(input('Quer ver a TABUADA de qual valor?: '))
    if num == -2:
        break

    for cont in range(1, 11):
        print(f'{num} x {cont:2} = {num*cont}')

print('='*35)
print('*** PROGRAMA DE TABUADA ENCERRADO!!! ***')




