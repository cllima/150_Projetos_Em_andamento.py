## Faça um programa que leia a largura e a altura de uma parede em metros,
# e calcule a sua área e a quantidade de tinta necessária para pintar,
# sabendo que cada litro de tinta, pinta uma área de 2m2.

##print('Área da Metragem da parade + quantidade de tinta que será utilizada na Pintura.')
alt=float(input('Digite a Altura da parede em m2: '))
larg=float(input('Digite a Largura da parede em m2: '))
área=alt*larg
tinta=(área)/2

print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m2. \nPara pintar essa parede, você precisará de {:.1f}lts. de tinta.'
      .format(alt,larg,área,tinta))

print('#-#'*6)
print('A área total da parede é de {:.2f}m2, e a quantidade de tinta para pintura {:.1f}lts. '.format(área,tinta))



