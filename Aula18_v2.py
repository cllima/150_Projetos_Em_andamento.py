'''teste=[]
teste.append('Daniel')
teste.append(20)
galera=[]
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 25
galera.append(teste[:])
print(galera)'''
##################################
'''
galera = [['João', 45],['Pedro',25],['Daniel',10],['Marcio',56]]
print(f'Imprime toda a lista: {galera}')
print(f'Imprime o 1º conjunto: {galera[0]}') # Primeiro conjunto
print(f'Imprime o 1º nome do conjunto: {galera[0][0]}') # Primeiro nome.
print(f'Imprime a Idade do nome Daniel: {galera[2][1]} anos') # Idade do Daniel

print('\nImprime a lista na Vertical:')
for p in galera:
    #print(f'{p}') # Imprime a lista na Vertical Nome e Idade.
    #print(f'{p[0]}') # Imprime somente os nomes.
    #print(f'{p[1]} anos')  # Imprime somente as Idades..
    print(f'O aluno {p[0]} tem {p[1]} anos.')
'''
##################################
galera=[]
dados=[]
tot_maior = tot_menor = 0
for cont in range(1,4):
    dados.append(str(input(f'{cont}º nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear() ### Apaga os dados após fazer o laço.
print(galera)
# Mostrar somente as Pessoas que são maiores e menores de idade.
for pessoa in galera:
    if pessoa[1] >= 21: ## pessoa[1] == Idade é maior ou igual a 21.
        tot_maior+=1
        print(f'{pessoa[0]} é MAIOR de Idade!!')
    else:
        tot_menor+=1
        print(f'{pessoa[0]} é MENOR de Idade!!!')
print(f'Temos {tot_maior} pessoas MAIORES e {tot_menor} MENORES de idade!!')
