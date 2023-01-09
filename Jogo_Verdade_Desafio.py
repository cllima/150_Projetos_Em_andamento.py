import random
from time import sleep

y = ' Verdade ou Desafio '
print('_' * 41)
print('\033[34m{:=^41}\n\033[m'.format(y))

v1 = 'Já fez algo de que se arrependa?,se sim o que?'
v2 = 'Ja tirou a Virgindade?'
v3 = 'Você tem um dia inesquecivel?, se sim como foi?'
v4 = 'Você ja desistiu de algo muito importante?, se sim o que foi?'
v5 = 'Já sofreu ou praticou bullying na escola?'
v6 = 'Tem algum grande desejo?qual?'
v7 = 'Ja entrou em uma briga?como foi?'
v8 = 'Você quer ter filhos?, se sim quantos?'

d1 = 'Imite um macaco'
d2 = 'Deixe a pessoa do seu lado direito te daar um tapa'
d3 = 'Teve sorte, pule a sua vez'
d4 = 'Fale uma raça de cachorro que começa com y, se não conseguir imite um '
d5 = 'Não fale nada pelos proximos 5 minutos'
d6 = 'Fale para uma pessoa que não está na brincadeira que a ama( não vale parente)'
d7 = 'Você so poderá escolher desafio nas proximas 5 rodadas'
d8 = 'Agora você tem poder, mande um dos jogadores fazer o que você quiser'
d9 = 'Imite uma galinha'

lista_v = [v1, v2, v3, v4, v5, v6, v7, v8]
lista_d = [d1, d2, d3, d4, d5, d6, d7, d8, d9]

cont1 = 's'
while cont1 == 's':
    print('_' * 41)
    escolha = (input('\nCaso queira verdade escreva (v)!'
                     '\nCaso queira desafio escreva (D)! '
                     '\n <==>: '))

    print('\033[32mPROCESSANDO!!!!\033[m')
    sleep(1.2)

    random.shuffle(lista_v) ## choice=escolha => shuffle=embaralhar
    random.shuffle(lista_d)

    if 'v' == escolha:
        print('\033[34m{}\033[m'.format(lista_v[0]))

    else:
        print('\033[33m{}\033[m'.format(lista_d[0]))

    print('_' * 41)
    cont1 = input('\nQuer continuar? S/N:  ')


y = ' FIM DO JOGO '
print('_' * 41)
print('\033[31m\n{:=^41}\n\033[m'.format(y))
print('_' * 41)