## Um produto custa (x) valor, o preço deste produto com pagamento a vista, tem desconto de 10% (y) valor
# e parcelado tem acrescimento 13% (XY) valor.

produto=float(input('Qual o valor do produto R$ '))
avista= produto-(produto*10/100)         #produto*0.10
parcelado= produto+(produto*13/100)      #produto*0.13
###################################
print('O valor do produto é R$ {:.2f}: \ncom pagamento avista (PIX ou Dinheiro) tem 10% de desconto e ficará R$ {:.2f},'
      ' \ne caso seja parcelado em 2x terá um reajuste de 13% e ficará R$ {:.2f}.'.format(produto,avista,parcelado))
print('-/-'*25)