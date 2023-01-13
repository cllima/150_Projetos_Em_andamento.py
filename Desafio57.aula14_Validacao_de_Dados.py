#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valotes "M" e "F".
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
print('VALIDAÇÃO DE DADOS EM PYTHON')
print('='*28)

sexo=str(input('Digite seu Gênero/Sexo [M/F]: ')).upper().strip()[0] #[0] Significa fatiamento pega somente a 1º Letra.
idade=int(input('Informe sua Idade: '))

while sexo not in "MF":
    sexo=str(input('Dados inválidos!! Digite novamente seu Gênero/Sexo [M/F]: ')).upper().strip()[0]
print(f'O sexo {sexo} e a idade {idade} anos, foram digitados com SUCESSO!!!')



