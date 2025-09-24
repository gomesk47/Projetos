#Criação de um dicionario vazio, seguido de atribuição de chaves e valores
dici_1 = {}
dici_1['none'] = 'Maria'
dici_1['idade'] = 25

#Criação de um dicionario com chaves pares chave: valor
dici_2 = {'none': 'Maria', 'idade': 25}

#Criação de um dicionario com uma lista de tuplas representando pares chave: valor
dici_3 = dict([('none', 'Maria'), ('idade', 25)])

#Criação de um dicionario usando a função build-in zip () e duas listas, uma para as chaves e outra para os valores
dici_4 = dict(zip(['none', 'idade'], ['Maria', 25]))

#Teste se todas as construções resultam em objetos iguais
print(dici_1 == dici_2 == dici_3 == dici_4) #Deve imprimir true
print(dici_1)