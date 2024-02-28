#funcao dentro de uma funcao

def executar(funcao): #aqui criei a funcao executar e ela chama a funcao como parametro
    if callable(funcao):# aqui é só pra validar se o parametro é uma funcao mesmo 
        funcao()

def bomdia(): # aqui temos uma funcao bom dia
    print('bom dia')

def boatarde(): # aqui temos uma funcao boa tarde
    print('bom tarde')

executar(bomdia) #aqui estou chamando a funcao executar e a funcao de paarmetro é a bom dia ou seja a funcao executar vai executar a funcao bom dia
executar(boatarde)# aqui a mesma coisa porem com a funcao tarde