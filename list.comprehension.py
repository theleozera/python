## jeito normal
lista = []
for i in range(1,10):
    if i % 2==0:
        a = i*2 
        lista.append(a)
print(lista)

# mais pratico
dobros= [i*2 for i in range(1,10) if i % 2==0]
print(dobros)

# ele gera só se vc ficar usando next
generator = (i**2 for i in range(1,10) if i % 2==0)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator)) #erro

##usando for em vez de next
generator = (i**2 for i in range(1,10) if i % 2==0)
for numero in generator:
    print(numero)

# dicionario com comprehensions
dicionario = {f'item {i}': i*2 for i in range(10)if i % 2== 0}
print(dicionario)

for numero,dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')

# usando comprehension no switch para saber se é fim de semana ou semana
def tipo_dia(dia):
    dias = {
        (1,7): 'fim de semana', ## aqui uma tupla com os dias do find
        tuple(range(2,7)): 'dia de semana', # aqui e uma tupla com range q vai de 2 a 6
    }
    dia_escolhido = ( tipo for numeros,tipo in dias.items()if dia in numeros)
    return next(dia_escolhido, '** invalido **')

for dia in range(10):
    print(f'{dia}: {tipo_dia(dia)}') 

    