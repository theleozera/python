conjunto = set()
# se tiver valor repetido ele nao liga, só imprime os diferentes
conjunto = {1,2,3,7,2,4,4,456,23,46,45,6534,4,3}
print(conjunto)
## apenas teste logicos para verr quem esta no conjunto
print(1 in conjunto, 5  not in conjunto and 6534 in conjunto)
conjunto2 = {1,2,3}
conjunto3 = {5,4,2}
# unindo os conjuntos
print(conjunto2.union(conjunto3))
# interseçacao dos conjuntos
print(conjunto2.intersection(conjunto3))
conjunto.update(conjunto2)
print(conjunto)
print(conjunto2)

from string import Template
a= "dhyullya"
b= "cunha"

##interpolação
print(f'nome: {a} {b}')