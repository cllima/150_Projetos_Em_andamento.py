n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota '))
n3=float(input('Digite a terceira nota: '))
m=(n1+n2+n3)/3
if m>=8:
    print('Sua média foi {:.1f}, PARABÉNS você foi Aprovado!!'.format(m))
else:
    print('Sua média foi {:.1f}, REPROVADO, estude mais!!'.format(m))
print('')
print('**** FIM ****')


