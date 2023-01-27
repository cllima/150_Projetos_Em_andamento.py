## Crie um programa que tenha uma Tupla com várias palavras (não usar acentos).
## Depois disso, o programa deve mostrar, para cada palavra, quais são as vogais.
print('='*50)
print(f'{"Contando vogais em Tupla":^50}'.upper())
print('='*50)
palavras=('aprender','programar','linguagem','python','curso',
          'grátis','estudar','praticar','trabalhar','mercado',
          'programador','futuro','avião')
for c in palavras:
    print(f'\nNa palavra: "{c.upper()}" temos => ', end='')
    for letra in c:
        if letra.lower() in 'aáàãeéêiíoõôuú':
            print(f'{letra:.>3}', end=' ')
