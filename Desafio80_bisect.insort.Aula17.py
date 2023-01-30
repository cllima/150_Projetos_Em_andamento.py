## Crie um programa onde os usuário possa digitar 5 valores numéricos e cadastre-os, em uma LISTA,
# já na posição correta de inserção ( sem usar o sort()).
# No final mostre a LISTA ordenada na Tela.
print('*'*30)
### Qual a diferença de usar o módulo bisect.insort e usar o sort: A diferença é que bisect.insort já insere de
# forma ordenada, o sort precisa da lista com elementos primeiro para depois ordenar (é uma etapa a mais).
import bisect
valor_lista = []

for c in range(1,6):
    valor=int(input(f'Digite o {c}º valor: '))
    bisect.insort(valor_lista,valor)
    #print(f'Número {valor} incluído na {valor_lista.index(valor)+1}ª posição.')
print('=' * 30)
print(F'Números digitados: {valor_lista}')

### 2ª OPÇÂO ###
###############################################################################
## Pegar o primeiro valor da lista e colocar na primeiro posição.
    ## Pegar o ultimo valor da lista e colocar na ultima posição.
'''lista = []
for c in range(0,5):
    num = int(input(f'Digite o {c}ª Valor: '))

    if c == 0 or num > max(lista):
        lista.append(num)
        print("Valor adicionado no Final da Lista!!!")
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Valor adicionado na posição {pos} da Lista!!!')
                break
            pos += 1
print('*'*30)
print(f'Os valores digitados em ordem foram: {lista}.')'''

