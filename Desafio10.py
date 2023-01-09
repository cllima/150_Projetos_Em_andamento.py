## Crie uma programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
## quantos Dólares ela pode comprar.
### Cotação: $ 1.00 = R$ 5.27 em 09/12/2022.

print('Vamos realizar a conversão de reais para dólares!')
################===============######################
nome=input('Digite o nome do Investidor: ')
real=float(input('Digite a quantidade de Dinheiro em carteira R$ '))
dolar=real/5.27
euro=real/5.52
peso=real/0.031

print('O cliente {}, tem em carteira R$ {:.2f}, desta forma, ele pode comprar: \nUS$ {:.2f} Dolares \nEUR {:.2f} Euro '
      '\npeso {:.2f} Peso Argentino'.format(nome,real,dolar,euro,peso))












