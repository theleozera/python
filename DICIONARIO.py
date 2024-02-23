#criando dicionario
pessoa = {'nome': ['leo','lucas'] , 'idade' : 26, 'altura' : 1.70, 'salario': 2050}
#vendo tamanho do dicionario
print(len(pessoa))
# vendo idade do cara no dicionario
print(pessoa['idade'])
# vendo campos
print(pessoa.keys())
# vendo valores
print(pessoa.values())
# vendo campos e valores
print(pessoa.items())
# pegando o valor dentro do campo idade
print(pessoa.get('idade'))
# vendo os nomes, ja que nome é uma lista no dicionario neste caso
print(pessoa['nome'])
# aqui eu estou adicionando mais um nome para lista dentro do dicionario
pessoa['nome'].append('cesar')
# novamente imprimindo os nomes
print(pessoa['nome'])
# deletei salario do dicionario
del pessoa['salario']
print(pessoa)
# pop tambem deleta o dado do dicionario
pessoa.pop('idade')
print(pessoa)
# aqui fiz um update deixando o nome leo
pessoa.update({"nome" : 'leo' })
print(pessoa)
# limpei o dicionario
pessoa.clear()
print(pessoa)