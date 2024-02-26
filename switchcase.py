### o switch nao temos nativo no python porem podemos usar uma funcao comm dicionario para simular ele

def dias_semana(dia):
    dias = {
        1: 'domingo',
        2: 'segunda',
        3: 'terca',
        4: 'quarta',
        5: 'quinta',
        6: 'sexta',
        7: 'sabado'
    }
    return dias.get(dia, '** invalido **')

for dia in range(0,9):
    print(f'{dia}: {dias_semana(dia)}')

def find(dias):
     semana = {
        1: 'domingo find',
        2: 'segunda',
        3: 'terca',
        4: 'quarta',
        5: 'quinta',
        6: 'sexta',
        7: 'sabado find'
    }
     return semana.get(dias)
 # meu for    
for dias in range(1,8):
    if dias == 1 or dias ==7:
        print('e find')
        
def ver_se_e_find(dia):
    match dia:
        case 6 |  2 | 3 | 4 | 5:
            return 'dia de semmana'
        case 1 | 7:
            return 'find'
for dia in range(8):
    print(f'{dia}:{ver_se_e_find(dia)}')