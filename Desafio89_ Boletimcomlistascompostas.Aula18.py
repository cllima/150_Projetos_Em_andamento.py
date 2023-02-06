## Crie um programa que leia o Nome e 3 notas de vários alunos e guarde tudo
## em uma lista composta. No final, mostre um boletim contendo a média de cada um
## e permita que o usuário possa mostrar as NOTAS de cada aluno Individualmente.
### São 3 niveis de LISTA.

print('=' * 48)
print(f'{"Boletim com listas compostas":^48}'.upper())
print('=' * 48)

ficha=[]
while True:
    aluno=(str(input('Nome: '))).upper()
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    nota3 = float(input('3ª Nota: '))
    media=(nota1 + nota2 + nota3)/3
    ficha.append([aluno,[nota1,nota2,nota3],media]) ## Lista composta
              ##aluno 0        aluno1       aluno2
    resp=' '
    while resp not in 'SN':
        resp=str(input('Deseja continuar [S/N]: ')).strip().upper()
    if resp in 'N':
        break
print('='*48)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*48)

for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('=' * 48)
    opc=int(input('NOTA Individual do Aluno [999 INTERROMPE]: '))
    if opc == 999:
        print('<<< \nPROGRAMA FINALIZANDO >>>')
        break
    if opc <= len(ficha)-1:
        print(f'As notas do(a) Aluno(a) \33[1;32m{ficha[opc][0]}\33[m são \33[1;35m{ficha[opc][1]}\33[m')

print('<<<< VOLTE SEMPRE >>>>'.center(48))


