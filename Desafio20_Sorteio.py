## O professor quer sortear a ordem de apresentação dos trabalhos dos alunos.
## Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada.
import random

a1=str(input('Primeiro Aluno: '))
a2=str(input('Segundo Aluno: '))
a3=str(input('Terceiro Aluno: '))
a4=str(input('Quarto Aluno '))
lista = [a1,a2,a3,a4]
random.shuffle(lista) ##  random.shuffle => serve para embaralhar os itens.
print('A ordem de apresentação dos trabalhos será.')
print(lista)