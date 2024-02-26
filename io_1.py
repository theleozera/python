# lendo arquivo
arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    print('nome: {} , idade: {}'.format(*registro.split(',')))

# outro modo de leer
arquivo = open('pessoas.csv')
for registro in arquivo:
    print('nome: {} , idade: {}'.format(*registro.split(',')))
arquivo.close()

# o strip tira os espaços nas bordas, ou podemos passar por parametro oq quiseremos tirar, ja o split ele pega duas palavras e estamos botando uma virgula no meio
arquivo = open('pessoas.csv')
for registro in arquivo:
    print('nome: {} , idade: {}'.format(*registro.strip().split(',')))
arquivo.close()



# o finaly sera executado mesmo se o try der erro, porem o codigo depois do bloco finally nao sera executado
# a nao ser que usamos um tramaneto de excessao que por exmplo pode ser o index error
try: 
    arquivo = open('pessoas.csv')
    for registro in arquivo:
             print('nome: {} , idade: {}'.format(*registro.strip().split(',')))
except IndexError: ##aqui o bloco nao pode estar vazio entao a palavra pass serve pra isso, só pra ele entrar e sair
    pass

finally:
    arquivo.close()

# usando with
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
             print('nome: {} , idade: {}'.format(*registro.strip().split(',')))
if arquivo.closed:
    print('fechou o arquivo')


# usando with para gerar arquivo
with open('pessoas.csv') as arquivo:
    with open ('pessoas.txt' , 'w') as saida: # aqui eu estou usando o modo write do with que usada letra W
        for registro in arquivo:
             pessoa= registro.strip().split(',')
             print('nome: {} , idade: {}'.format(*pessoa), file=saida) #esse file signica que o arquivo irra abrir em outro lugar nao no terminal como de costume
if arquivo.closed:
    print('fechou o arquivo')

# usando o leitor csv
import csv
with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('nome : {}, idade : {}'.format(*pessoa))    

#lendo um arquivo da net por url  
import csv
from urllib import request
def read(url):
    with request.urlopen(url) as entrada:
        print('baixando csv')
        dados= entrada.read().decode('latin1') #regula os acentos esse decode
        print('dowload completo')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}:{cidade[3]}')

read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv') #o r é só para interpretar a url sem erros ou sumir com algo