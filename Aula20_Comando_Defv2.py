'''def soma(a,b):
    print(f'A é igual {a} e B é igual {b}')
    soma=a+b
    print(f' => O TOTAL de A + B = {soma}')
    print('-' * 30)

#Programa Principal
soma(8,9)
soma(5,6)
soma(4,6)'''

##################
#Tupla
def contador(*num): ## Desempacotamento
    tamanho=len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números.')

# Programa Principal
contador(1,2,3)
contador(5,6,8,9)
contador(4,8,7,2)

##################
#Lista
'''def dobra(lista):
    pos=0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores=[9,6,5,4,5,8]
dobra(valores)
print(valores)'''
