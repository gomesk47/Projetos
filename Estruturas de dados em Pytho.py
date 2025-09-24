# Função filter;
# Filtra os elementos de uma sequencia com base em uma função de teste (retorna true or false)
# filter(funcao_teste, sequencia)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)