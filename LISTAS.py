
# criei a lista
lista=[]      
# inseri alguns dados com a funcão append                    
lista.append(7)
lista.append(34)
lista.append(18)
lista.append('teste')
# imprimi a lista usando a função len() que diz o tamanho da lista
print(len(lista))
# aqui criei uma segunda lista e atribui mais 3 valores
lista2= lista + ['leo', 13, 71]
print(lista2)
#  aqui estou fazendo um insert o numero 4 siginica a posição 
# de onde estou ponto o valor, e o 2 sim é o valor que 
# entrara na lista
lista2.insert(4,2)
print(lista2)
# removi o dois da lista
lista2.remove(2)
print(lista2)
# aqui estou verificando em que posição esta o nome leo usando index
print(lista2.index('leo'))
# aqui estou vendo se ele esta na lista como sim, resposta true
print('leo' in lista2)
# aqui estou vendo que esta na posição 3 da lista
print(lista[3])
# aqui estou vendo que esta do inicio ate a posição 2
# obs: posisao 2 nao entra na resposta, apenas a 0 e 1
print(lista2[:2])
# aqui estou vendo de posisao 1 pra frente
print(lista2[1:])
# aqui eu estou vendo de 2 em 2 casas
print(lista2[::2])
# aqui eu deletei que esta da posicao um para frente
del lista[1:]
print(lista)
