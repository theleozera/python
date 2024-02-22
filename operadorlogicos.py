trabalho_terca = False
trabalho_quinta = False

tv50= trabalho_quinta and trabalho_terca
tv32= trabalho_terca != trabalho_quinta
sorvete = trabalho_quinta or trabalho_terca
saudavel = not sorvete
print("tv50={} tv32={} sorvete={} saudavel={}".format(tv50,tv32,sorvete,saudavel))