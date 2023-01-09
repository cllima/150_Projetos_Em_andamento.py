# Refaça o Desafio 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço FOR.
print('='*30)
print(f'{" CALCULADORA COM FOR ":=^30}')
print('='*30)
print('\n[1] SOMA\n[2] SUBTRAIR\n[3] DIVISÃO\n[4] MULTIPLICAÇÃO')
opção=int(input('Escolha um número: '))
num=int(input('Digite o número para calcular a Tabuada: '))
print('--'*10)

for c in range(1,10+1):
    if opção == 1:
        print('{} + {:2} = {}'.format(num,c,num+c))
        #print(f'{num} x {c:2} =',num*c)
    elif opção == 2:
        print('{} - {:2} = {}'.format(num, c, num-c))
    elif opção == 3:
        print('{} / {:2} = {:.2f}'.format(num, c, num/c))
    elif opção == 4:
        print('{} x {:2} = {}'.format(num, c, num*c))

print('--' * 10)

like=(input('Curtiu, deixe seu like SIM (s) ou NÃO (n): '))

if like == 's':
    print('Obrigado pelo like!!!')

elif like == 'n':
    print('Volte, SEMPRE!!!')

