# add (). in e remove ()

#Criando conjunto vazio

meu_conjunto = set ()

#Adicionando elementos ao conjunto
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)

#Imprimindo o conjunto
print("conjunto após adicionar elementos", meu_conjunto.add)

#Verificando se um elemento esta no conjunto
elemento = 20
if elemento in meu_conjunto:
    print(f"{elemento} está no conjunto.")
else:
    print(f"{elemento} não está no conjunto")

#Removendo um elemento do conjunto
meu_conjunto.remove(20)

#imprimindo o conjunto atualizado
print("Conjunto após remover o elemento 20:", meu_conjunto)