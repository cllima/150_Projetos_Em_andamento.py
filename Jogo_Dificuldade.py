print('-' * 24)
import random
play = str(input('Está pronto para começar? \n==> ')).strip().lower()

s = 'sim' in play
n = 'não' in play

if s == True:
    difficulty = str(input('Chose a difficulty (hard, normal or easy): ')).strip().lower()

    easy = 'easy' in difficulty
    normal = 'normal' in difficulty
    hard = 'hard' in difficulty
    d1 = random.randint(1, 3)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 9)

    if easy == True:
        print('Ue, escolheu a dificuldade fácil? que medroso...')
        num1 = int(input('escolha logo um número entre 1 e 3: '))

        if num1 == d1:
            print('Certo, você acertou, mas com a dificuldade no fácil, todos conseguem.')
        else:
            print(f'Cara, até no fácil você errou? eu pensei no número {d1}, não no {num1}')

    if normal == True:
        print('Normal? tá começando a ficar interessante...')
        num2 = int(input('Escolhe um número entre 1 e 6: '))

        if num2 == d2:
            print('Você acertou!? tenho certeza que no hard você não teria tanta sorte assim...')
        else:
            print(f'Como esperado, você errou, se você não acerta aqui, imagina no hard LOL! Eu pensei no {d2}, '
                  f'não no {num2}')

    if hard == True:
        print('Está tão confiante assim? hahahaha')
        num3 = int(input('Escolhe um número entre 1 e 9: '))

        if num3 == d3:
            print('Impossível!!! eu nunca perdi nessa dificuldade!!!')
        else:
            print('Não se envergonhe... eu fui programado para nunca perder nesse nível. Eu pensei '
                  f'no {d3}, não no {num3}')

if n == True:
    print('Seu medroso...')

print('-----END-----')
print('-' * 24)