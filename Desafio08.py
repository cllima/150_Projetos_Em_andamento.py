## Escreva um programa que leia um valor em metros e o exiba convertido
## em centimetros e milímetros.

print('Vamos realizar a transformação métricas dos valores!!')
m=float(input('Qual a distância em metros: '))
km=m/1000
hm=m/100
dam=m/10
dm=m*10
cm=m*100
mm=m*1000

print('A medida de {}m corresponde a {}km, {}hm, {}dam, {:.0f}dm, {:.0f}cm, {:.0f}mm'.format(m,km,hm,dam,dm,cm,mm))





