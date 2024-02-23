# versao 1
raio = 15.3
pi = 3.14159
area =raio**2 * pi
print('A Area do circulo e:', area)

# versao 2
import math
raio2 = 15.3
pi2 = math.pi
area2 =raio**2 * pi2
print('A Area2 do circulo e:', area2)
# versao 3
# aqui eu forcei que a resposta fosse entendida como float
raio3 = float(input("informe o raio:"))

print('a area do circulo e:' , raio3**2*math.pi)