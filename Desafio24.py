## Crie um programa que leia o nome de uma cidade e diga se ela
# começa ou não com o nome "SANTO".
# True ou False

cid=str(input('Em qual cidade você nasceu: ')).strip()
print(cid[0:5].upper() == 'SANTO')  ## indica se tem a palavra Santo no inicio do nome da cidade.
print('SANTO' in cid.upper()) ## indica se tem a palavra santo no nome da cidade.
