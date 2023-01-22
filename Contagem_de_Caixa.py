print('-='*10)
print('CONTAGEM DO CAIXA')
print('-='*10)
while True:
    caixa = float(input('digite o valor do caixa:'))
    outros = float(input('Digite o valor de outros:'))
    if outros > 0:
        caixa -= outros
    cem = int(input('Notas de 100€: '))
    contcem = 0
    cinquenta = int(input('Notas de 50€: '))
    contcinquenta = 0
    vinte = int(input('Notas de 20€: '))
    contvinte = 0
    dez = int(input('Notas de 10€: '))
    contdez = 0
    cinco = int(input('Notas de 5€: '))
    contcinco = 0
    dois = int(input('Moedas de 2€: '))
    contdois = 0
    um = int(input('Moedas de 1€: '))
    contum = 0
    moedacinquenta = float(input('Moedas de 0.50€: '))
    contmoedacinquenta = 0
    moedavinte = float(input('Moedas de 0.20€: '))
    contmoedavinte = 0
    moedadez = float(input('Moedas de 0.10€: '))
    contmoedadez = 0
    moedacinco = float(input('Moedas de 0.05€: '))
    contmoedacinco = 0
    moedadois = float(input('Moedas de 0.02€: '))
    contmoedadois = 0
    moedaum = float(input('Moedas de 0.01€: '))
    contmoedaum = 0
    while cinquenta != 0 and caixa >= 50:
        caixa -= 50
        cinquenta -= 1
        contcinquenta += 1

    while vinte != 0 and caixa >= 20:
        caixa -= 20
        vinte -= 1
        contvinte += 1

    while dez != 0 and caixa >= 10:
        caixa -= 10
        dez -= 1
        contdez += 1

    while cinco != 0 and caixa >= 5:
        caixa -= 5
        cinco -= 1
        contcinco += 1

    while dois != 0 and caixa >= 2:
        caixa -= 2
        dois -= 1
        contdois += 1

    while um != 0 and caixa >= 1:
        caixa -= 1
        um -= 1
        contum += 1

    while moedacinquenta != 0 and caixa >= 0.50:
        caixa -= 0.50
        moedacinquenta -= 1
        contmoedacinquenta +=1

    while moedavinte != 0 and caixa >= 0.20:
        caixa -= 0.20
        moedavinte -= 1
        contmoedavinte += 1
    while moedadez != 0 and caixa >= 0.099:
        caixa -= 0.10
        moedadez -= 1
        contmoedadez += 1
    while moedacinco != 0 and caixa >= 0.049:
        caixa -= 0.05
        moedacinco -= 1
        contmoedacinco += 1
    while moedadois != 0 and caixa >= 0.019:
        caixa -= 0.02
        moedadois -= 1
        contmoedadois += 1
    while moedaum != 0 and caixa >= 0.001:
        caixa -= 0.01
        moedaum -= 1
        contmoedaum += 1

    print(f' Outros tem o valor total de {outros}€')
    print(f'será depositado {contcinquenta} nota(s) de 50€')
    print(f'será depositado {contvinte} nota(s) de 20€')
    print(f'será depositado {contdez} nota(s) de 10€')
    print(f'será depositado {contcinco} nota(s) de 5€')
    print(f'Será depositado {contdois} moeda(s) de 2€')
    print(f'Será depositado {contum} moeda(s) de 1€')
    print(f'Será depositado {contmoedacinquenta} moeda(s) de 0.50€')
    print(f'Será depositado {contmoedavinte} moeda(s) de 0.20€')
    print(f'Será depositado {contmoedadez} moeda(s) de 0.10€')
    print(f'Será depositado {contmoedacinco} moeda(s) de 0.05€')
    print(f'Será depositado {contmoedadois} moeda(s) de 0.02€')
    print(f'Será depositado {contmoedaum} moeda(s) de 0.01€')
    print('-='*20)
    print(f'Valor restante no caixa é de: {caixa:.2f}€')
    print('-='*20)
    fim = ' '
    while fim not in 'SN':
        fim = input('Gostaria de calcular novamente? [S/N]: ').upper().strip()[0]
    if fim == 'N':
        break