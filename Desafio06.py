## Crie um algoritimo que leia um número e mostre o seu dobro,
## triplo e a raiz quadrada.

n=int(input('Digite um número: '))
dobro=n*2
triplo=n*3
raiz=n**(1/2)
print('O dobro do número {} = {},\nSeu triplo = {},\nE sua raiz quadrada = {:.2f}'.format(n,dobro,triplo,raiz))

print('\033[32m =/=/=/= Outra forma de fazer =/=/=/= \033[m')
print('O dobro do número {} = {},\nSeu triplo = {},\nE sua raiz quadrada = {:.2f}'.format(n,(n*2),(n*3),(n**(1/2))))

print('\033[35m****************************')
print('\033[32m******** FIM DO JOGO *******')
print('\033[36m****************************')