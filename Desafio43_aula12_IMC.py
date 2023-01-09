## Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC
# e mostre seu Status, de acordo coma tabela abaixo:
# Abaixo de 18.5: Abaixo do peso/Magreza
# Entre 18.5 a 24.9: Peso ideial
# De 25 até 29.9: Sobrepeso
# De 30 até 39,9: Obesidade
# Acima de 40: Obsidade Mórbida

y=' Índice de Massa Corporal (IMC '
print('-'*40)
print('\033[32m{:=^40}\033[m'.format(y))
print('-'*40)

peso=float(input('Qual o seu PESO (kg): '))
altura=float(input('Qual a sua ALTURA: '))
sexo=int(input('''Qual o seu Gênero
[1] HOMEM
[2] MULHER
Resp.: '''))

imc=peso/(altura**2)
print('Seu IMC é de {:.1f}'.format(imc))

## HOMEM
if sexo == 1:
    if imc < 18.5:
        indice='ABAIXO DO PESO'
        print('Você está {}, precisa ganhar Peso!!'.format(indice))
    elif imc < 24.9:
        indice = 'NORMAL'
        print('PARABÉNS, você está na faixa de Peso {}!!'.format(indice))
    elif 24.9 <= imc < 29.9: ##Segunda opção.
        indice = 'SOBREPESO'
        print('Você está com {}, faça exercícios e se alimente melhor!!'.format(indice))
    elif imc < 39.9:
        indice = 'OBESIDADE'
        print('Você está com {}, procure um especialista!!'.format(indice))
    else:
        indice = 'OBESIDADE MÓRBIDA'
        print('Você está com {}, cuidado!!!'.format(indice))
## MULHER
elif sexo == 2:
    if imc < 18.5:
        indice='ABAIXO DO PESO'
        print('Você Mulher está {}, precisa ganhar Peso!!'.format(indice))
    elif imc < 24.9:
        indice = 'NORMAL'
        print('PARABÉNS, Mulher você está na faixa de Peso {}!!'.format(indice))
    elif 24.9 <= imc < 29.9: ##Segunda opção.
        indice = 'SOBREPESO'
        print('Você Mulher está com {}, faça exercícios e se alimente melhor!!'.format(indice))
    elif imc < 39.9:
        indice = 'OBESIDADE'
        print('Você Mulher está com {}, procure um especialista!!'.format(indice))
    else:
        indice = 'OBESIDADE MÓRBIDA'
        print('Você Mulher está com {}, cuidado!!!'.format(indice))

print('')
print('-' * 40)
print('================== FIM =================')
print('-' * 40)


