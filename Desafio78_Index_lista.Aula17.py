## Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o MAIOR e o MENOR número digitado e as suas respectivas posições na lista.

print('=' * 42)
print(f'{"FAZENDO UMA LISTA COM 5 VALORES":^40}')
print('=' * 42)

listanum = []

for c in range(1, 6):   ## Aqui a lista tem um limite de 5 ítens.
    listanum.append(int(input(f'Informe o {c}º valor da lista: ')))
print('-' * 42)
print(f'A lista contém os números: {listanum}.')

'''for i, v in enumerate(listanum):
    if v == min(listanum):
        print(f'O MENOR valor digitado foi {min(listanum)}, ', end=''
              f'na {i+1}ª posição!')
print()
for i, v in enumerate(listanum):
    if v == max(listanum):
        print(f'O MAIOR valor digitado foi {max(listanum)}, ', end=''
              f'na {i+1}ª posição!')'''
print()
## Esta opção e bem melhor!!
print(f'\nO MENOR valor digitado foi {min(listanum)}, ', end=''
      f'na {listanum.index(min(listanum))+1}ª posição!')
print(f'\nO MAIOR valor digitado foi {max(listanum)}, '
      f'na {listanum.index(max(listanum))+1}ª posição!')
