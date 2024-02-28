#soma dois numeros
def soma_2(a,b):
    return a+b

#soma 3 numeros
def soma_3(a,b,c):
    return a+b+c

#nao ha limite de numeros aqui
def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma = soma + n
    return soma 

print(soma_2(2,3))
print(soma_n(3,4,6,6,7,5,54,4)) #isso é o packing

#o unpacking eu vou mandar uma tupla como arumento e usando asterisco ele ira desempacotar e somar por exemplo
# em soma 3 recebe 3 argumentos, voou mandar uma tupla com 3 valores
tupla_nums = (1,2,3)
print(soma_3(*tupla_nums)) #funciona com lista tbm

lista_nums = [1,2,3] #aqui com lista
print(soma_3(*lista_nums))

# **kwargs -> campos nomeados
def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} {piloto}')

resultado_f1(primeiro = 'leo',
             segundo = 'evandro',
             terceiro = 'mario')
# misturando posicionais com nomeados
def todos_parametros(*args,**kwargs): #args sao posicionais e kwargs nomeados
    print(f'args :{args} kwargs: {kwargs}')

todos_parametros(1,2,3,ola =5)