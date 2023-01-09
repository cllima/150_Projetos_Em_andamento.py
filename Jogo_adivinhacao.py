print('**********************************')
print('**     Jogo de Adivinhação      **')
print('**********************************')
print('')
numero_secreto = 42
total_de_tentativas = 3
rodada = 1
"""
nivel=1 == 10
nivel=2 == 5
nivel=3 == 3
"""

##while(rodada <= total_de_tentativas):
for rodada in range (1, total_de_tentativas + 1):
    print('Rodada: {} e total de tentativas: {} '.format(rodada, total_de_tentativas))
    chute=int(input('Digite um número: '))
    ##print('Você digitou: {} '.format(chute))

    acertou= numero_secreto == chute
    maior= chute > numero_secreto
    menor= chute < numero_secreto

    if(acertou):
        print('Parabéns, você Acertooouu!!')
        break

    elif(maior):
        print('Você errou! O seu chute foi maior que o número secreto!!')
    elif(menor ):
        print('Você errou! O seu chute foi menor que o número secreto!!')

    ##rodada = rodada + 1
    print('')

print('**********************************')
print('********** FIM DO JOGO ***********')
print('**********************************')




