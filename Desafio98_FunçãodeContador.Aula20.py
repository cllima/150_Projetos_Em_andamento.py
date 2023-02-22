#Faça um programa que tenha uma função chamada contador(), que receba
#três parâmetros: início, fim e passo.
#Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
print('Função de Contador'.center(30).upper())
print('='*30)

from time import sleep
def contador(i,f,p): ## Inicio, Fim, Passo

    ## Comando para fazer o teste lógico, número rodar negativo
    p = abs(p)
    ###########################################################

    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(1.5)

    if i < f:
        cont=i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(.3)
            cont += p
        print()
        print(f'<<<<<<<< FIM >>>>>>>>'.center(30))
    else: ## Faz a contagem decrescente
        cont=i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(.3)
            cont -= p
        print()
        print(f'<<<<<<<< FIM >>>>>>>>'.center(30))


# Programa Principal
print('Contagem Crescente')
contador(0,100,10)
print('-'*30)
print('Contagem Decrescente')
contador(10,0,2)
print('-'*30)
print('Agora chegou a hora de você Personalizar sua Contagem!!')
ini=int(input('Inicio: '))
fim=int(input('Fim: '))
pas=int(input('Passo: '))
contador(ini,fim,pas)

