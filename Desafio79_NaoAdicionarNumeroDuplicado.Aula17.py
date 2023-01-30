## Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores digitados, em ordem crescente.
print('=' * 55)
print(f'{" Números repetidos não são adicionados na lista ":=^55}')
print('=' * 55)
numeros = list()
cont=0
while True:   ## Aqui estamos trabalhando com Lista com numeração infinita.
    cont+=1
    num=int(input(f'informe o {cont}º valor: '))
    if num not in numeros:
        numeros.append(num)
        print('Adicionado com SUCESSO!!!')
    else:
        print('Valor duplicado, não será adicionado!!!')

    resp=' '
    while resp not in 'SN': ## Necessário colocar para evitar erro ao digitar qualquer outra letra.
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('=' * 55)

numeros.sort()
print(f'Os números digitados foram {numeros}')
print('=' * 55)
print('{:-^55}'.format(' FINALIZADO COM SUCESSO!!! '))
