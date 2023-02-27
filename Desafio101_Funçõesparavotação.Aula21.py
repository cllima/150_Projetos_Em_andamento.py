## Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o
# ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
# tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
print('Funções para votação'.center(30).upper())
print('='*30)

def voto(ano):
    from datetime import date  ## Data atual
    atual=date.today().year
    idade=atual-ano
    if idade <16:
        return f'Com {idade} anos: NÂO VOTA!'
    elif 16 <= idade <18 or idade > 65: ## Entre 16 e 18 e acima de 65 anos
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!!'

#Programa Principal
nasc=int(input('Em que anos você nasceu: '))
print(voto(nasc))