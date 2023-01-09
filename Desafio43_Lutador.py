'''Escreva um programa que leia o nome de um lutador e seu peso. Em seguida,
informe a categoria a que pertence o lutador, conforme a Tabela a seguir (note que a tabela
foi criada para efeito deste exercício e não condiz com qualquer categoria de luta). A saída
do programa deve exibir na tela uma frase com o padrão descrito a seguir:
Nome fornecido: Pepe Jordão
Peso fornecido: 73.4
Frase a ser exibida: O lutador Pepe Jordão pesa 73,4 kg e se enquadra na categoria Ligeiro

Programação como ficaria nesta pergunta?
Coloque todo o seu programa dentro de um laço de repetição e faça-o se encerrar
quando uma determinada condição for satisfeita.
peso < 65: Categoria Pena')
peso (= 65 or < 72): Categoria Leve
peso (= 72 or < 79): Categoria Ligeiro
peso (= 79 or < 86): Categoria Meio Médio
peso (= 86 or < 93): Categoria Médio
peso (= 93 or < 100): Categoria Meio Pesado
peso (>= 100): Categoria Pesado '''

print('Vamos calcular o valor final considerando juros e descontos')

valor = input('Qual o valor do produto? R$ ').upper()

if valor.isalpha():
    print('Você digitou letras. Da proxima vez, digite apenas numeros. (ex: 100.00)')

else:
    valor = float(valor)
    print('''\nQual a forma de pagamento?
    [0] - À vista em dinheiro (-10%)
    [1] - À vista no cartão (-5%)
    [2] - Em até 2x no cartão 
    [3] - 3x ou mais no cartão (+20%)\n''')

    selecao = str(input('Qual a forma de pagamento escolhida? '))
    print('\n')

    if selecao == '0':
        print('Pagamento À VISTA em DINHEIRO selecionado')
        print('Desconto: 10%')
        desconto = valor - (valor * (10 / 100))
        print(f'Valor do produto: R${valor:.2f}')
        print(f'Valor do desconto: R${valor - desconto:.2f}')
        print(f'Valor a ser pago: \033[4;32mR${desconto:.2f}\033[m')