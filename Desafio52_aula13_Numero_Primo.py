# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# Número primro e divisivel por 1 e por ele mesmo.
print('/'*25)
print('      NÚMERO PRIMO')
print('/'*25)

num=int(input('Informe um número: '))
tot=0
for c in range(1,num + 1):
    if num % c== 0:
        print('\033[33m',end='')
        tot += 1
    else:
        print('\033[31m',end='')
    print(c,end=' ')

if tot == 2:
    print(f'\n\033[mO número {num}, foi divisível \033[33m{tot} vezes\033[m, por 1 e por ele mesmo, sendo assim é considerado número PRIMO!!')
else:
    print(f'\n\033[mO número {num}, foi divisível \033[33m{tot} vezes\033[m desta forma, NÃO é números PRIMO!!!')



