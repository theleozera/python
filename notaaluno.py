nota= 2
ERRO = '\033[91m'
if nota>=9:
    print('boa aprovado')
elif nota>=7:
    print('ali ali ein')
elif nota>=5:
    print("recuperação")
else:
    print(ERRO,'ja era')