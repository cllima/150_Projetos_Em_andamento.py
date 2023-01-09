## Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição aparece a primeira vez a letra "A".
# Em que posição aparece a última vez a letra "A".

frase=str(input('Digite uma frase: ')).upper().strip()
print('Na frase aparece {} vezes a letra (A).'.format(frase.count('A'))) ## conta o qtd de letra (A).
print('Na frase a 1º letra (A) aparece na posição {}. '.format(frase.find('A')+1)) # find=achar => Encontra a letra (A)
print('Na frase a ultima letra (A) aparece na posição {} dos caracteres. '.format(frase.rfind('A')+1))
print('Na frase a ultima letra (A) aparece na posição {}. '.format(frase.rfind('A')+1-frase.count(' ')))