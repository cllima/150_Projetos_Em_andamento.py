# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e
# fechados na ordem correta.
print('=' * 40)
print(f'{"Validando expressões matemáticas":^40}'.upper())
print('=' * 40)

## Forma simplificada
expr=str(input('Digite uma Expressão: '))
pi = expr.count('(')
pf = expr.count(')')
if expr.index(')') > expr.index('('):
    if pi == pf:
        print('Sua expressão esta VÁLIDA!!!')
    else:
        print('Expressão INVALIDA!!!')
else:
    print('Expressão inválida')

print('='*40)

#$#$#$##$$##$$#$$##$$$#$#$#$##$#$##$#$#$#$#$#$#$#$#

'''
expr=str(input('Digite uma expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop() ### Deleta o último número da Lista
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta VÁLIDA!!!')
else:
    print('Expressão INVALIDA!!!')
'''

