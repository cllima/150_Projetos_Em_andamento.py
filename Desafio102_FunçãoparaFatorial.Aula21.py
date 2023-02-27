##Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o
# número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
# ou não na tela o processo de cálculo do fatorial.

print('Função para Fatorial'.center(30).upper())
print('='*30)

def fatorial(n,show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: Retorna o valor Fatorial  de uma número n.
    """
    mult=1
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            print(' x ' if c > 1 else ' = ', end='') # Coloca o sinal de x e =
        mult*=c
    return mult

#Programa Principal
num=int(input('Informe um número: '))
print(fatorial(num,show=True))
#help(fatorial)