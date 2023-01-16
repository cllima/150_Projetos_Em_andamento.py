## Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o MAIOR e o MENOR valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
lista=[]
resp='s'
while resp in 'Ss':
    num=int(input('Digite uma número: '))
    resp=str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    lista.append(num)
    if resp == 'Nn':
        break

print(f'Você DIGITOU {len(lista)} número e a MÉDIA {sum(lista) / len(lista):.2f}'
      f' \nO MAIOR valor foi {max(lista)} e o MENOR valor foi {min(lista)}.')

print('FIM... VOLTE SEMPRE!!!')






