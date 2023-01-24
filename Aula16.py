# Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. \n'
# 'As tuplas são variáveis compostas e imutáveis que permitem armazenar vários \n'
# 'valores em uma mesma estrutura, acessíveis por chaves individuais.')
print('** AULA DE TUPLA **')
print('*=* FATIAMENTO *=*')
'''lanche=('Hamburque','Suco','Pizza','Pudim')
### Tuplas são Imutáveis
#for c in lanche:
print(lanche[1:3])
print(lanche[-2])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])'''
############################################## #

lanche=('Hamburque','Suco','Pizza','Pudim', 'Batata Frita')
## Sem numerar
'''for comida in lanche:
    print(f'Estou com fome e vou comer/beber um(a) {comida}.')
print(f'Resumindo estou de Barriga cheia e comi no TOTAL: {len(lanche)} lanches!!!')'''
############################################## #

## Com número
'''for cont in range(0, len(lanche)):
    print(f'Estou com fome e vou comer/beber um(a) {lanche[cont]} na sequência {cont}.')

print(f'Resumindo estou de Barriga cheia e comi no TOTAL: {len(lanche)} lanches!!!')'''
############################################## #

## Com número
'''for pos, comida in enumerate(lanche):
    print(f'Estou com fome e vou comer/beber um(a) {comida} {pos}.')
print(f'Resumindo estou de Barriga cheia e comi no TOTAL: {len(lanche)} lanches!!!')'''
############################################## #
## sorted => coloca em ordem alfabética.
#print(sorted(lanche))

############################################## #
'''dados = ('Clayton', 45, 'Sexo', 'M','Estado', 'SP')
print(dados)'''

############################################## #
a= (2,5,6,8)
b= (5,1,3,7)
c = a + b

print(sorted(c))
print(c)
print(f'Quantas vezes aparece o número (5) {c.count(5)} vezes.')
print(f'O maior número é {max(c)}.')
print(f'O menor número é {min(c)}.')
print(f'Quantidade de números = {len(c)}.')
print(f'Em qual posição está o número informado: {c.index(1)} posição.') # Qual posição está determinado número.