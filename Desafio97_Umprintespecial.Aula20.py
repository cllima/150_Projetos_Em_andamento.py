## Faça um programa que tenha uma função chamada escreva(), que receba uma texto qualquer como parâmetro e mostre
# uma mensagem com tamanho adaptável.
# Expl.: escreva('Olá, Mundo!!')
#saída
#~~~~~~~~~~~~~~~~
  #Olá, Mundo!!!
#~~~~~~~~~~~~~~~~
print('Um print especial'.center(30).upper())
print('='*30)

# Função que desenha linha com tamanho adaptável
def escreva(msg):
    tamanho=len(msg)+2
    print('~' * tamanho)
    print(f'{msg}'.center(tamanho))
    print('~' * tamanho)

# Programa Principal
while True:
    msg=str(input('Digite uma palavra: '))
    escreva(f'{msg}')

    while True:
        resp=str(input('Deseja continuar [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!! Responda Sim ou Não.')
    if resp == 'N':
        break

print('\n<<<< fim do programa >>>>'.center(20).upper())