## Desenvolva uma programa que leia 4 valores pelo tecladoe guarde-os em uma Tupla.
## No final mostre:
#A) Quantas vezes aparece o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

print('-'*40)
print('{:=^40}'.format(' Análise de dados em uma Tupla '))
print('-'*40)
# Colocando dentro de uma TUPLA

## A variavel tem que ser antes do for, neste caso na mesma linha = List Comprehension
num=tuple(int(input(f"Digite o {c}º número [1 a 10]: "))for c in range(1,5))

print(f'\nForam digitado os valores {num}')
print(f'O número 9 apareceu: {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado!!!')
print(f'Os valores pares digitados são: ', end='')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')
print('')
print('>>>>>>>>>> FIM DO PROGRAMA <<<<<<<<<<')




