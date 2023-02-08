'''dados = {}
dados = {'nome': 'Pedro', 'idade': 25}
dados['sexo']='M' ## Adiciona o elemento Sexo em Dados, não usa-se (.append).
#del dados['idade'] ## Remove elemento.
print(dados)
print(dados['nome'])
print(dados['idade'])
print(dados['sexo'])'''
#########################################################################

filme={'titulo':'Star Wars','ano':1977,'diretor':'George Lucas'}
printfilme.values()) # Nomes = valores == Star Wars
print(filme.keys()) # Chaves == titulo
print(filme.items()) # Pega todos
print(f'O nome do filme é {filme["titulo"]}, do Ano {filme["ano"]} e o Diretor {filme["diretor"]}.')
print('')
for k,v in filme.items(): ## O for faz um loop ou laço dos 3 elementos da chave.
    print(f'O {k} é {v}.')