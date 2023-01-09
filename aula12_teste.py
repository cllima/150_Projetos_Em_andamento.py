## Estrutura Condicional Aninhada:

nome=str(input('Digite seu nome: ')).upper().title().strip() ## .title=> Faz com que a 1º letra fique em caixa alta.
if nome== 'Daniel':
    print('Que lindo nome você tem!!!')
elif nome=='Pedro' or nome== 'Maria' or nome== 'João' or nome== 'Joao':
    print('Seu nome e bem popular no BRASIL!!!')
elif nome in 'Ana Claudia Jessica Jéssica ':
    print('Que belo nome FEMININO!!!!')
else:
    print('Nossa seu nome é feio kkk!!!')

print('Tenha um bom dia, {}!!!'.format(nome))