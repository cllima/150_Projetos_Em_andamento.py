## Melhore o Desafio 61, perguntando ao usuário se ele quer mostrar mais alguns termos.
## O programa encerra quando ele disser que quer mostrar (O) Termo.
print('******* GERADOR DE PA *******')
print('-='*15)

primeiro=int(input('1º Termo da PA: '))
razão=int(input('Razão da PA: '))
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{primeiro} -> ',end='')
        primeiro += razão
        cont += 1
    print('PAUSA!!!')
    mais= int(input('Quantos termos você quer mostrar a mais?: '))
print(f'\nFIM DO PROGRAMA - Finalizado com {total} termos MOSTRADOS!!!!')