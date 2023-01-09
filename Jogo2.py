###Radar de Velocidade
from time import sleep
from random import randint
#import playsound
print('Hoje está um belo dia para um passeio de carro.')
sleep(2)
print('Você pede um uber até a loja de aluguel de carro.')
sleep(1)
print('03...!!!')
sleep(1)
print('02...!!')
sleep(1)
print('01...!')
sleep(2)
print('Você chega na loja.')
sleep(2)
print('Hoje as opções de carro para alugar são...')
sleep(2)
print("""
1- Volkswagen Fusca
2- Hyundai HB20 
3- Tesla Model S
4- Mclaren SpeedTail""")
esc = int(input('Escolha um carro digitando seu respectivo numero: '))
if esc == 1:
    print('Você escolheu Volkswagen Fusca, um classico dos tempos antigos.')
    sleep(2)
    print('Você vai para uma rodovia testar essa belezinha.')
    sleep(2)
    print('Um carro cola do seu lado e buzina para começar um racha.')
    sleep(3)
    print('Você todo empolgado começar acelerar')
    fusca = randint(40, 115)
    if fusca <= 110:
        print('Vocês correm por varios Km...')
        sleep(2)
        print('Você na emoção do momento acaba nem percebendo o radar de velocidade logo a frente, mas para sua sorte você estava dentro da velocidade permitida')
    else:
        print('Vocês correm por varios Km...')
        sleep(2)
        print('Você no calor do momento acaba nem percebendo o radar de velocidade logo a frente...')
        playsound.playsound('somflash.mp3')
        sleep(2)
        print('E acaba passando o limite de velocidade permitido na rodovia.')
        multa = (fusca - 110) * 7
        sleep(2)
        print(f'No dia seguinte você recebe uma carta com uma multa de velocidade de R${multa} por passar no radar com a velocidade de {fusca}Km/h')
elif esc == 2:
    print('Você escolheu Hyundai HB20, o queridinho dos jovens de faculdade.')
    sleep(2)
    print('Você vai para uma rodovia testar essa belezinha.')
    sleep(2)
    print('Um carro cola do seu lado e buzina para começar um racha.')
    sleep(3)
    print('Você todo empolgado começar acelerar')
    hb20 = randint(40, 161)
    if hb20 <= 110:
        print('Vocês correm por varios Km...')
        sleep(2)
        print('Você na emoção do momento acaba nem percebendo o radar de velocidade logo a frente, mas para sua sorte você estava dentro da velocidade permitida')
    else:
        print('Vocês correm por varios Km...')
        sleep(2)
        print('Você no calor do momento acaba nem percebendo o radar de velocidade logo a frente...')
       # playsound.playsound('somflash.mp3')
        sleep(2)
        print('E acaba passando o limite de velocidade permitido na rodovia.')
        multa = (hb20 - 110) * 7
        sleep(2)
        print(f'No dia seguinte você recebe uma carta com uma multa de velocidade de R${multa} por passar no radar com a velocidade de {hb20}Km/h')

elif esc == 3:
    print('Você escolheu Tesla Model S, um belo e rapido carro eletrico.')
    sleep(2)
    print('Você vai para uma rodovia testar essa belezinha.')
    sleep(2)
    print('Um carro cola do seu lado e buzina para começar um racha.')
    sleep(3)
    print('Você todo empolgado começar acelerar')
    tesla = randint(40, 320)
    if tesla <= 110:
        print('Vocês correm por varios Km...')
        sleep(2)
        print('Você na emoção do momento acaba nem percebendo o radar de velocidade logo a frente, mas para sua sorte você estava dentro da velocidade permitida')
    else:
        print('Vocês correm por varios Km...')
        sleep(2)
        print('Você no calor do momento acaba nem percebendo o radar de velocidade logo a frente...')
        #playsound.playsound('somflash.mp3')
        sleep(2)
        print('E acaba passando o limite de velocidade permitido na rodovia.')
        multa = (tesla - 110) * 7
        sleep(2)
        print(
            f'No dia seguinte você recebe uma carta com uma multa de velocidade de R${multa} por passar no radar com a velocidade de {tesla}Km/h')
elif esc == 4:
    print('Você escolheu Mclaren SpeedTail, um dos carros mais rapido mundo.')
    sleep(2)
    print('Você vai para uma rodovia testar essa belezinha.')
    sleep(2)
    print('Um carro cola do seu lado e buzina para começar um racha.')
    sleep(3)
    print('Você todo empolgado começar acelerar')
    mclaren = randint(40, 403)
    if mclaren <= 110:
        print('Vocês correm por varios Km...')
        sleep(2)
        print('Você na emoção do momento acaba nem percebendo o radar de velocidade logo a frente, mas para sua sorte você estava dentro da velocidade permitida')
    else:
        print('Vocês correm por varios Km...')
        sleep(2)
        print('Você no calor do momento acaba nem percebendo o radar de velocidade logo a frente...')
       # playsound.playsound('somflash.mp3')
        sleep(2)
        print('E acaba passando o limite de velocidade permitido na rodovia.')
        multa = (mclaren - 110) * 7
        sleep(2)
        print(f'No dia seguinte você recebe uma carta com uma multa de velocidade de R${multa} por passar no radar com a velocidade de {mclaren}Km/h')
else:
    print('Não temos esse carro, volte outro momento.')