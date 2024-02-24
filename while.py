from random import randint

numero_informado = -1
numero_secreto = randint(0,9)

while numero_secreto != numero_informado :
    numero_informado = int(input('diga o numero'))
print("boa acertou o numero era ", numero_informado)
print('numero {} foi encontrado'.format(numero_secreto))
