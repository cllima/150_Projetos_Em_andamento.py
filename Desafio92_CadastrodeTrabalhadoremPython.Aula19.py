## Crie um programa que leia o nome, Ano de nascimento e carteira de trabalho e cadastre-os (com idade)
# em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule  e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
print('=' * 40)
print(f'{"Cadastro de Trabalhador em Python":^40}'.upper())
print('=' * 40)
from datetime import date
data_atual=date.today().year

dados={}

dados['nome']=str(input('Nome: '))
nasc=int(input('Ano de Nascimento: '))
dados['ctps']=int(input('Carteira de Trabalho [0 não existe]: '))
dados['gênero']=str(input('Sexo [M/F]: ')).upper()[0]
dados['idade']=date.today().year - nasc
idade = (data_atual-nasc)

if dados['gênero'] == 'M':
    if idade >= 65:
        print(f'<<< {dados["nome"]}, você já tem idade para se Aposentar, tem mais de 65 anos de idade!!')
        if dados['ctps'] != 0: # Se for diferente de ZERO mostra dos Dados abaixo.
            dados['contratação']=int(input('Ano de Contratação: '))
            dados['salário']=float(input('Salário: R$ '))
            #dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
            dados['aposentadoria'] = (dados['contratação'] + 35) - nasc
            print(f'Você tem {dados["aposentadoria"]} de contribuição.')
    else:
        tempo_restante = 65 -idade
        print(f'{dados["nome"]}, ainda falta {tempo_restante} anos para se Aposentar!!!')

else:
    if idade >= 61:
        print(f'{dados["nome"]}, você já tem idade para se Aposentar, tem mais de 61 anos de idade!!')
        if dados['ctps'] != 0:  # Se for diferente de ZERO mostra dos Dados abaixo.
            dados['contratação'] = int(input('Ano de Contratação: '))
            dados['salário'] = float(input('Salário: R$ '))
            # dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
            dados['aposentadoria'] = (dados['contratação'] + 30) - nasc
            print(f'Você tem {dados["aposentadoria"]} de contribuição.')
    else:
        tempo_restante = 61 -idade
        print(f'{dados["nome"]}, ainda falta {tempo_restante} anos para se Aposentar!!!')

print('='*40)
for k,v in dados.items():
    print(f'  ==>{k}: {v}')
print('-'*40)
print(f'<<< FIM DO PROGRAMA >>>'.center(40))
print('*'*40)
print(dados)

