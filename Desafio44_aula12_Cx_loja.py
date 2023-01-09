## Elabore uma programa que calcule o valor a ser pago por um produto, considerando
# o seu preço normal e condições de pagamento:
# Á vista dinheiro/Pix: 10% de desconto
# Á vista no cartão: 5% de desconto
# Em até 2x no cartão: Preço normal
# Em 3x ou mais no cartão: 20% de juros.
## Tabela de cores:
cores={'limpa':'\033[m',
       'branco':'\033[40m',
       'vermelho':'\033[31m',
       'verde':'\033[32m',
       'verde_bold':'\033[1:32m',
       'amarelo': '\033[33m',
       'azul':'\033[34m',
       'lilas':'\033[35m',
       'cinza':'\033[37m',
       'pretobranco':'\033[7;30m',
       'underline':'\033[4m'}

print('=' * 40)
print('{}Bem vindo(a) a LOJAS CLLIMA{}'.center(40).format(cores['verde'],cores['limpa']))
print('=' * 40)

valor = {'1':100,'2':150,'3':200,'4':250,'5':300}
produtos = {'1':"calça",'2':"blusa",'3':"tênis",'4':"sapato",'5':"camisa"}

print('''
1 - calça    R$ 100.00
2 - blusa    R$ 150.00
3 - tênis    R$ 200.00
4 - sapato   R$ 250.00
5 - camisa   R$ 300.00\n''')
c1=str(input('Escolha o produto:  ')).lower().strip()
var = valor[c1]
var = produtos[c1]

preço=str(input('O produto comprado foi um(a): {}{}{} ao preço de {}R$ {:.2f}{}.'
                .format(cores['azul'],produtos[c1].upper(),cores['limpa'],
                        cores['verde_bold'],valor[c1],cores['limpa'])))

print('''FORMA DE PAGAMENTO 
[ 1 ] À vista dinheiro / PIX (-10% desconto)
[ 2 ] À vista Cartão Débito (-5% desconto)
[ 3 ] 2x Cartão de Crédito 
[ 4 ] 3x ou mais no Cartão de Crédito (+20% acrescimo)\n''')
opção=str(input('Qual é a Opção: '))

if opção == '1':
   print('Pagamento À VISTA em DINHEIRO ou PIX:')
   print('Desconto: 10%.')
   desconto = valor[c1] * 0.10
   total = valor[c1] - desconto
   print('Preço do produto:  R$ {:.2f}'.format(valor[c1]))
   print('Valor do desconto: R$ {:.2f}'.format(desconto))
   print('Valor a PAGAR:     {}R$ {:.2f}{}'.format(cores['verde_bold'],total,cores['limpa']))


elif opção == '2':
    print('PAGAMENTO Á VISTA NO CARTÃO:')
    print('Desconto: 5%')
    desconto = valor[c1] * 0.05
    total= valor[c1] - desconto
    print('Preço do Produto:  R$ {:.2f}'.format(valor[c1]))
    print('Valor do desconto: R$ {:.2f}'.format(desconto))
    print('Valor a PAGAR:     {}R$ {:.2f}{}'.format(cores['verde_bold'],total,cores['verde_bold']))

elif opção == '3':
    print('PAGAMENTO EM ATÉ 2X SEM JUROS:')
    print('Preço normal')
    print('Preço do Produto:  R$ {:.2f}'.format(valor[c1]))
    print('Valor a PAGAR:     {}R$ {:.2f}{}'.format(cores['verde_bold'],valor[c1], cores['verde_bold']))

elif opção == '4':
    total_parcelas = int(input('Quantas parcelas: '))

    if total_parcelas < 3: ## Regra para digitar 3 ou mais parcelas.
        print('{}NÚMERO DE PARCELAS INVÁLIDO, digite 3 ou mais parcelas.{}'.format(cores['vermelho'],cores['limpa']))

    elif total_parcelas >= 3:
        print('PAGAMENTO EM 3X ou MAIS no CARTÃO:')
        print('Acrescimo: 20% de juros.')
        acrescimo = valor[c1] * 0.20
        total = valor[c1] + acrescimo
        print('Preço do Produto:   R$ {:.2f}'.format(valor[c1]))
        print('Valor do acrescimo: R$ {:.2f}'.format(acrescimo))
        print('Valor a PAGAR:      {}R$ {:.2f}{}'.format(cores['verde_bold'], total, cores['verde_bold']))
else:
    total = preço
    print('{}OPÇÃO INVÁLIDA DE PAGAMENTO, \nEscolha entre as opões 1 a 4!!!{}'.format(cores['vermelho'],cores['limpa']))

f=' FIM DO PROGRAMA '
print('{}{:=^40}'.format(cores['verde_bold'],f))
print('-'*40)