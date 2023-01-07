'''ESTRUTURA DE REPEIÇÃO - FOR'''
'''#contador = c
for c in range(0,3):
    print('OI!!')
print('FIM!!\n')
##############################
for c in range(6,0,-1):
    print(c)
print('FIM...!!!\n')
##############################
n = int(input('Digite um número: '))
for c in range(0,n+1):
    print(c)
print("Fim...!\n")
##############################
i=int(input('INICIO: '))
f=int(input('FIM: '))
p=int(input('Passo: '))
for c in range(1, f+1 ,p):
    print(c)
print('FIM')
##############################
for c in range(0,4):
    n=int(input('Digite um Valor: '))
print('FIM DO PROGRAMA')'''
##############################
s=0
for c in range(0,4):
    n=int(input("Digite um valor: "))
    s +=n
print('A soma dos valor foi {}'.format(s))