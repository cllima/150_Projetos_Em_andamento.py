## Jogo adivinha a palavra com dica ou sem dica.

from random import choice
from time import sleep
## Criando uma Tabela de cores:
cores={'limpa':'\033[m',
       'branco':'\033[40m',
       'vermelho':'\033[31m',
       'verde':'\033[32m',
       'amarelo': '\033[33m',
       'azul':'\033[34m',
       'lilas':'\033[35m',
       'cinza':'\033[37m',
       'pretobranco':'\033[7;30m',
        'underline':'\033[4m'}
print('*'*40)
print('{}  ADIVINHE-QUAL-É-A-PALAVRA!----V-1.2{}'.format(cores['azul'],cores['limpa']))
print('*'*40)

lista= ['abelha','macaco','matemática','matematica','livro','praia','leão','leao','celular','triângulo','triangulo'
    ,'história','historia','capitalismo']
palavra_secreta1 = choice(lista)
dica1 = str(input('\nVocê precisa de uma dica [SIM ou NÃO]: ')).strip().lower()
#----------------------------------dicas----------------------------------

if palavra_secreta1=='abelha':
    dica2='A sua dica é: Inseto => Amarelo e preto e pica'
    frase='A palavra_secreta tem 6 letras...'

elif palavra_secreta1 == 'macaco':
    dica2 = ' A sua dica é: Animal => Evolução humana '
    frase= ' A palavra secreta tem 6 letras '

elif palavra_secreta1 == 'matemática' or palavra_secreta1 == 'matematica':
    dica2 = ' A sua dica é: Matéria => Pesadelo de muitos na escola '
    frase= ' A palavra secreta tem 10 letras '

elif palavra_secreta1 == 'livro':
    dica2 = ' A sua dica é: A base do Conhecimento '
    frase= ' A palavra secreta tem 5 letras '

elif palavra_secreta1 == 'praia':
    dica2 = ' A sua dica é: Algo relacionado a Férias '
    frase= ' A palavra secreta tem 5 letras '

elif palavra_secreta1 == 'leão' or palavra_secreta1 == 'leao':
    dica2 = ' A sua dica é: Tem na selva => Rei '
    frase= ' A palavra secreta tem 4 letras '

elif palavra_secreta1 == 'celular':
    dica2 = ' A sua dica é: Usamos diariamente => Sem isso, sem vida '
    frase= ' A palavra secreta tem 7 letras '

elif palavra_secreta1 == 'triângulo' or palavra_secreta1 == 'triangulo':
    dica2 = ' A sua dica é: Uma Forma Geométrica!!'
    frase= ' A palavra secreta tem 9 letras '

elif palavra_secreta1 == 'história' or palavra_secreta1 == 'historia':
    dica2 = ' A sua dica é: Todos nós temos => Passado '
    frase= ' A palavra secreta tem 10 letras '

elif palavra_secreta1 == 'capitalismo':
    dica2 = ' A sua dica é: Uma forma de Governo '
    frase= ' A palavra secreta tem 11 letras '

if dica1 == 'sim' or dica1 == 's':
    print(dica2)
#------------------se o jogador não quêr dicas------------------
else:
    print(' Então vamos direto ao jogo! ')
print('\n   {}Tente adivinhar a palavra => (Regras)!! '
      '\n   Se você pediu dica => terá 3 chances para adivinhar a palavra! '
      '\n   Se você não pediu dica => terá 5 chances para adivinhar a palavra{}! '.format(cores['vermelho'],cores['limpa']))

print(f'\n {frase} ')

#------------------------jogo com dica------------------------

if dica1 == 'sim' or dica1 == 's':
    n1a = str(input('  Tente adivinhar a palavra: ')).strip().lower()
    if n1a == palavra_secreta1:
        print('   {}PARABÉNS ! VOCÊ GANHOUUUU!!! {}'.format(cores['verde'],cores['limpa']))
    elif n1a != palavra_secreta1:
        print(' Você errou! ')
        n2a = str(input(' Tente novamente: ')).strip().lower()
        if n2a == palavra_secreta1:
            print('   {}PARABÉNS ! VOCÊ GANHOUUUU!!! {}'.format(cores['verde'],cores['limpa']))
        elif n2a != palavra_secreta1:
            print(' Você errou .')
            n3a = str(input(' Sua última tentativa: ')).strip().lower()
            if n3a == palavra_secreta1:
                print('   {}PARABÉNS ! VOCÊ GANHOUUUU!!! {}'.format(cores['verde'],cores['limpa']))
            elif n3a != palavra_secreta1:
                print(' Você perdeu \n A palavra era {} '.format(palavra_secreta1))
#------------------------------------------jogo sem dica------------------------------------------
else:
    n1b = str(input('  Tente adivinhar a palavra: ')).strip().lower()
    if n1b == palavra_secreta1:
        print('   {}PARABÉNS ! VOCÊ GANHOUUUU!!! {}'.format(cores['verde'],cores['limpa']))
    elif n1b != palavra_secreta1:
        print(' Você errou ')
        n2b = str(input(' Tente novamente: ')).strip().lower()
        if n2b == palavra_secreta1:
            print('   {}PARABÉNS ! VOCÊ GANHOUUUU!!! {}'.format(cores['verde'],cores['limpa']))
        elif n2b != palavra_secreta1:
            print(' Você errou  ')
            n3b = str(input(' Tente novamente: ')).strip().lower()
            if n3b == palavra_secreta1:
                print('   {}PARABÉNS ! VOCÊ GANHOUUUU!!! {}'.format(cores['verde'],cores['limpa']))
            elif n3b != palavra_secreta1:
                print(' Você errou ')
                n4b = str(input('  Tente novamente: ')).strip().lower()
                if n4b == palavra_secreta1:
                    print('   {}PARABÉNS ! VOCÊ GANHOUUUU!!! {}'.format(cores['verde'],cores['limpa']))
                elif n4b != palavra_secreta1:
                    print(' Você errou  ')
                    n5b = str(input('  Sua última tentativa: ')).strip().lower()
                    if n5b == palavra_secreta1:
                        print('   {}PARABÉNS ! VOCÊ GANHOUUUU!!! {}'.format(cores['verde'],cores['limpa']))
                    elif n5b != palavra_secreta1:
                        print(' Você perdeu  \n A palavra era {} '.format(palavra_secreta1))

print('')
print('**** FIM DO JOGO ****')
