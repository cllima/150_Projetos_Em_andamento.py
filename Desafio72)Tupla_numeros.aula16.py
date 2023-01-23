## Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
## O programa deverá ler o número pelo teclado (entre 0 a 20) e mostrá-lo por extenso.

cont=('Zero','Um','Dois','Tres','Quatro',
           'cinco','Seis','Sete','Oito','Nove',
           'Dez','Onze','Doze','Treze','Quatorze'
           ,'Quinze','Dezesseis','Dezessete','Dezoito',
           'Dezenove','Vinte')

while True:
    num=int(input('Digite um número entre [0 e 20]: '))
    if num < 0 or num > 20:
        print('Número Inválido!! Tente novamente.')
        break
    print(f'Você digitou o número: \033[1:34m{cont[num]}\33[m.')
    print('=' * 35)

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if resp == 'N':
        break

print('=' * 35)
print('{:-^35}'.format(' FINALIZADO COM SUCESSO!!! '))








