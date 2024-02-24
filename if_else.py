
# nota = input('qual sua nota?')
# nota=float(nota)
# if nota >=9.1 and nota<=10:
#     print('nota A')
# elif nota >=7.1 and nota<=8: 
#     print('nota A-')
# elif nota >=6.1 and nota<=7: 
#     print('nota B')
# elif nota >=7.1 and nota<=8: 
#     print('nota B-')


def faixa_etaria(idade):
    if  0 < idade <18:
        return 'menor de idade'
    elif  idade in range(18,64):
         return 'adulto'
    elif  idade in range(65,100):
         return 'melhor idade'
    elif idade>=100:
         return 'centenario'
    else:
         return 'idade invalida'

for idade in (17,34,5,89,101):
     print(f'{idade}:{faixa_etaria(idade)}')

while True:
     print("vai")

