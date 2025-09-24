#Função map!
#aplica a uma função em toda a sequencia
#map(funcao, sequencia)
precos_em_dolares = [100, 50, 75, 120]
taxa_de_cambio = 5.25
precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))
print(precos_em_reais)