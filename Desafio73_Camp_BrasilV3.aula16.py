## Crie uma Tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
## na ordem de colocação. Depois:
#A) Mostre conforme solicitado abaixo.

from time import sleep
times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
             'Athético-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG',
	     'Botafogo','Santos', 'Goiás', 'Bragantino', 'Cuiabá', 'Ceará',
	     'Atlético-GO', 'Avaí', 'Juventude', 'Coritiba')

print("="*50)
print("{:^50}".format("DADOS DO BRASILEIRÃO 2022"))
print("="*50)

opcao = 0
while opcao != 8:
    sleep(1.2)

    opcao = int(input('''
[1] O Campeão do Brasileirão 2022
[2] Classificados para fase de grupos da Libertadores 
[3] Classificados para Pré - Libertadores 
[4] Classificados para fase de grupos da Copa Sul-Americana
[5] Rebaixados para serie B
[6] Posição e situação de determinado time
[7] Tabela completa
[8] Sair do programa do brasileirão
Digite uma Opção: '''))
    print("="*50)

    if opcao == 1:
        print(f"O Time campeão foi o {times[0]}!!") # Primeiro colocado
    elif opcao == 2:
        print(f"6 TIMES estão classificados para Libertadores 2023: \n{times[:6]}") # Os 6 primeiros
    elif opcao == 3:
        print(f"2 TIMES estão classificados para Pré - Libertadores 2023: \n{times[6:8]}") # 2 times
    elif opcao == 4:
        print(f"6 TIMES estão classificados para Sul-Americana 2023: \n{times[8:14]}") # 6 times
    elif opcao == 5:
        print(f"4 TIMES estão rebaixados para Segunda Divisão: \n{times[-4:]}") # Os 4 últimos times
    elif opcao == 6:
        time = str(input("Escreva o nome do seu TIME: ")).strip().title() # Obter a posição do Time.

        if time in times:
            print(f"O {time} ficou na {times.index(time)+1}º Posição")
            print("Situação: ",end="")
            if times.index(time) == 0:
                print("Campeão brasileiro e está na Libertadores")
            elif times.index(time) >= 1 and times.index(time) <= 5:
                print("Está na Libertadores")
            elif times.index(time) >= 6 and times.index(time) < 8:
                print("Está na Pré - Libertadores")
            elif times.index(time) >= 8 and times.index(time) <= 13:
                print("Está na Copa Sul-Americana")
            elif times.index(time) >= 16:
                print("Seu TIME está Rebaixado para a Serie B!!!")
            else:
                print("Ficou na Serie A, porém não se classificou para nenhuma outra competição!!")
        else:
            print(f"O {time} não participou do Brasileirão 2022")

    elif opcao == 7:
        cont = 0
        print("="*50)
        print("{:^50}".format("TABELA DO BRASILEIRÃO 2022"))
        print("="*50)

        for tabela in times:
            print(f"{cont + 1}º {tabela}")
            cont += 1
    print("=" * 50)
print("Fim do Programa do Campeonato Brasileiro")