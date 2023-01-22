## Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('='*40)
print('{:^40}'.format(' CAIXA ELETRÔNICO - BANCO CLLIMA '))
print('='*40)

valor=float(input('Qual valor deseja SACAR: R$ '))
total = valor
cedula = 100
total_cedula= 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cedula(s) de R$ {cedula}.')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('='*40)
print('BANCO CLLIMA - Agradece por sua SACADA!!')



