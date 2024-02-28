from pacote1 import modulo_1
from pacote2 import modulo_1 as modulo_sub # aqui tinha dois modulos com mesmo nome por isso renomeei um deles
print(type(modulo_1))
print(modulo_1.soma(2,3))
print(modulo_sub.subtracao(2,3))


from pacote2.modulo_1 import subtracao # aqui eu estoou importando direto a funcao subtracao em vez do modulo inteiro
print(subtracao(2,3)) # dai aqui nao preciso por o nome do modulo, só a funcao