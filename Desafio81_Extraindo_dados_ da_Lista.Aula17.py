# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso , mostre:
### A) Quantos números foram digitados.
### B) A lista de valores, ordenada em forma decrescente.
### C) Se o valor 5 foi digitado e está ou não na Lista.
## D) Em que posição a números 5 se encontra.
print('=' * 35)
print(f'{"Extraindo dados de uma Lista":^35}'.upper())
print('=' * 35)
lista=[]
cont_cinco=0

while True:
    num=int(input('Digite um VALOR: '))
    if num == 5:
        cont_cinco += 1
    lista.append(num)

    resp=' '
    while resp not in 'SN':
        resp=str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('*'*35)

lista.sort(reverse=True)
print(f'Temos {len(lista)} números digitados! '
      f'\nA lista em ordem Decrecente é {lista}.')

if 5 in lista:
    print(f'O valor 5 faz SIM, parte da LISTA e '
          f'\nfoi digitado {cont_cinco} vezes.')
else:
    print('O valor 5 NÂO faz, parte da sua LISTA!!!')
