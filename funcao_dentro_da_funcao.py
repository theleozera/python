def soma(a,b): # aqui uma funcao
    def soma_c(c): # essa funcao por estar dentro da funcao principal tem acessos aos paramretros dela mesmo e da funcao principal
        return a+b+c ##aqui ela ta retornando a e b que sao da funcao principal e da sua mesmo que é a c
    return soma_c # e a funcao principal consegue retornar a funcao que esta dentro dela


variavel_com_uma_funcao = soma(2,3)
print(variavel_com_uma_funcao(1))
print(soma(1,1)(4))



def log(function):
    def decorator(*args, **kwargs):
        print(f'inicio da chamada da funcão: {function}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'resultado da chamada:{resultado}')
        return resultado
    return decorator

        
@log
def soma(x , y):
    a = x + y
    return a

print(soma(1,2))