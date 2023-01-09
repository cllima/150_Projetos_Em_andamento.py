## Refaça o Desafio 35 dos Triângulos, acrescentando o recurso de mostrar
## que tipo de Triângulo será informado:
# Equilátero: Todos os lados iguais.
# Escaleno: Todos os lados diferentes.
# Isósceles: Dois lados iguas.

print('-=-'*12)
print("      ANALIZADOR DE TRIÂNGULO")
print('-=-'*12)
r1=float(input('Primeiro segmento: '))
r2=float(input('Segundo segmento: '))
r3=float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos ACIMA, FORMAM UM TRIÂNGULO: ', end=(''))
    if r1 == r2 == r3:
        print('EQUILÁTERO, pois todos os lados são iguais!!')
    elif r1 != r2 != r3 != r1: #!= diferente.
        print('ESCALENO, pois todos os lados são diferentes!!')
    else:
        print('ISÓSCELES, pois tem dois lados iguas')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!!')