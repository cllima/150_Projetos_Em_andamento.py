## Desenvolva uma programa que leia o comprimento de três retas e diga ao usuário,
# se elas podem ou não formar um triângulo.

print('-=-'*12)
print("      ANALIZADOR DE TRIÂNGULO")
print('-=-'*12)
r1=float(input('Primeiro segmento: '))
r2=float(input('Segundo segmento: '))
r3=float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos ACIMA PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!!')