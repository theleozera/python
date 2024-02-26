
import random
for i in range(1, 11):
    print('i = {}'.format(i))

for j in range(1,11):
    print(f'j={j}')

##tabuada
for x in range (1,11):
    for y in range(1,11):
        print(f' {x} * {y} = {x*y} ')

#percorrendo uma palavra
palavra = 'paralelepipedo'
for letra in palavra:
    print(letra)  

#percorrrendo uma lista
aprovado = ['leo', 'deson', 'robs']
for nome in aprovado:
    print (nome)

#dizendo a posição de cada um na lista
for posicao, nome in enumerate(aprovado):
    print(posicao + 1, nome)

#percorrendo umma dupla
dias = ('domingo', 'segunda' , 'terca', 'quarta', 'quinta', 'sexta', 'sabado')
for semana in dias:
    print('hoje e dia', semana)

#percorrendo dicionario
produto = {'nome': 'caneta', 'preco':10.50, 'importada':True, 'estoque': 435}
for chave in produto:
    print(chave)

#percorrendo valores
for valores in produto.values():
    print(valores)

#percorrendo valores e produtos
for chave, valor in produto.items():
    print(chave , '=', valor)

#imprimindo numeros impares com continue e if
for x in range(1,11):
    if x % 2 == 0:
        continue
    print(x)

#for com break
for x in range(1,11):
    if x ==5:
        break
    print(x)
# continue para aquela execução e vai para proxima, o break para e sai do laço
    
#for com else
for i in range(1,11):
        print(i)
else:
        print('fimm')
    
dado = random(1,6)
print(dado)
for valor in range(dado):
    if valor % 2 ==1:
        continue
    elif valor == dado:
            print('acertou') 
            break
    else: 
        print('nao acertou')