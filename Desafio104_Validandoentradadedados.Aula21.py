#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
# semelhante ‘a função input() do Python, só que fazendo a validação para
# aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

print('Validando entrada de dados em Python'.center(30).upper())
print('='*30)
def leiaInt():
    n = str(input('Digite um número: '))

    while not n.isnumeric():
        print('\033[0;31m Ops.ERRO!! Apenas números são aceitos!\033[m')
        n = str(input('Digite um número: '))
    n = int(n)
    print(f'Você digitou o número: {n} ')

#programa principal
leiaInt()