# primeira versao de fibonacci com while infinito
def fibonacci():
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end = ',')
    while True:
        proximo = penultimo + ultimo
        print(proximo, end = ',')
        penultimo = ultimo
        ultimo = proximo
fibonacci()

# fibonacci com while com limite agora
def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end = ',')
    while ultimo<limite:
        proximo = penultimo + ultimo
        print(proximo, end = ',')
        penultimo = ultimo
        ultimo = proximo
fibonacci(10000)

# aqui usamos a troca de valores nas variaveis para nao precisar utilizar a variavel proximo
def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end = ',')
    while ultimo<limite:
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo, end = ',')
fibonacci(10000)

# usando lista agora e percorrendo com for
def fibonacci(limite):
    resultado = [0,1]
    while resultado[-1]< limite: #este menos um é para mostrar o ultimo valor que esta contigo em lista da direita para esquerda
        resultado.append(resultado[-2] + resultado[-1]) #somando o ultimo com o penultimo
    return resultado

for fib in fibonacci(10000):
    print(fib)
    
#usando a funcao soma agora em vez de somar manualmente
def fibonacci(limite):
    resultado = [0,1]
    while resultado[-1]< limite: #este menos um é para mostrar o ultimo valor que esta contigo em lista da direita para esquerda
        resultado.append(sum(resultado[-2:]) ) #somando o ultimo com o penultimo
    return resultado

for fib in fibonacci(10000):
    print(fib)

# definindo quantos numeros vao ser listado, nesse caso 20
def fibonacci(quantidade):
    resultado = [0,1]
    while True:
        resultado.append(sum(resultado[-2:]) ) #somando o ultimo com o penultimo
        if len(resultado)==quantidade:
             break
    return resultado

for fib in fibonacci(20):
    print(fib)

#  substituindo while pelo for
def fibonacci(quantidade):
    resultado = [0,1]
    for i in range(2, quantidade):
        resultado.append(sum(resultado[-2:]) ) #somando o ultimo com o penultimo      
    return resultado

for fib in fibonacci(20):
    print(fib)

# fazendo um laõ com funcao conhecido como chaamda recursiva
def imprimir(maximo, atual):
    if maximo > atual:
        print(atual)
        imprimir(maximo, atual+1)

imprimir(10,1)

# usando a recursiva em fibonacci
def fibonacci(quantidade, sequencia = (0,1)):
    if len(sequencia)==quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))
for fib in fibonacci(20):
    print(fib)
    
    