print('*'*30)
print(f'{" SORTEADOR DE TAREFAS ":=^30}')
print('*'*30)
from random import randint
from time import sleep


nome = input('Qual o seu nome: ').strip().capitalize()

print(f'\n{nome}. Vou escolher um exercício para você REVISAR!!!')
input('Tecle \033[1:31m[ENTER]\033[m para que eu procure o exercício:')
while True:

    exercicio = randint(1, 101)

    print('\n\33[1:35mEscolhendo...!!!\033[m', end='')
    for a in range(0,1):
        sleep(0.8)
        print('\n\033[1:31m 3 \033[m')
        sleep(0.8)
        print('\033[1:33m 2 \033[m')
        sleep(0.8)
        print('\033[1:32m 1 \033[m')
        sleep(0.8)

    print(f'\n\033[1:35mVocê deve revisar o exercício {exercicio}!!!\033[m')

    b = str(input('Se já revisou esse a pouco tempo? Aperte \33[1;31m[ENTER]\33[m para escolher outro!!!'))
    if b == '':
        pass
    else:
        break