## Aprimore o desafio 86, mostrando  no final:
#A) A soma de todos os valores PARES digitados.
#B) A soma dos valores da 3ª coluna.
#C) O maior valor da 2ª linha.
print('=' * 30)
print(f'{"Matriz em Python":^30}'.upper())
print('=' * 30)

matriz=[[0,0,0], [0,0,0], [0,0,0]]
# Declarando variáveis
soma_par = maior = soma_col = 0

## For para escrever os VALORES.
for l in range(0,3): ## L == Linha
    for c in range(0,3): ### C == Coluna
        matriz[l][c]=int(input(f'Digite o valor para [{l}, {c}]: '))
print('-' * 30)
## For para mostar a estrutura na TELA.
print('NA MATRIZ, PARA CADA COLUNA, HAVERÁ 3 LINHAS.')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}] ',end='') ## :^5 -> espaços para centralizar.
        if matriz [l][c] % 2 == 0:
            soma_par+=matriz[l][c]
        if c == 2:
            soma_col += matriz[l][2]

    print() ## para montar as colunas
print('*' * 30)
print(f'A soma dos valores PARES é {soma_par}.')
print(f'A soma dos valores da 3ª coluna é {soma_col}.')
print(f'O MAIOR valor da 2ª linha é {max(matriz[1])}.') ## max == máximo valor
