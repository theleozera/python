import sys
# importei circulo do arquivo funcao
from funcao import circulo
#aqui to vendo se eu consigo mandar o arquivo em vez do usuario
if len(sys.argv)<2:
    print('ops')
else:
    raio = sys.argv[1]
    a=circulo(raio)
    print(a)
