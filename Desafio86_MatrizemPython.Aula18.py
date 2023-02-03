## Faça um programa que crie uma matriz 4x3 e preencha com valores lidos pelo Teclado.
## No final mostre a matriz na tela, com a formatação correta.
print('=' * 30)
print(f'{"Matriz em Python":^30}'.upper())
print('=' * 30)

matriz=[[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0]]

## For para escrever os VALORES.
for l in range(0,4): ## L == Linha
    for c in range(0,3): ### C == Coluna
        matriz[l][c]=int(input(f'Digite o valor para [{l}, {c}]: '))
print('-' * 30)
## For para mostar a estrutura na TELA.
print('NA MATRIZ, PARA CADA COLUNA, HAVERÁ 4 LINHAS.')
for l in range(0,4):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}] ',end='') ## :^5 -> espaços para centralizar.
    print()

print('*' * 30)

