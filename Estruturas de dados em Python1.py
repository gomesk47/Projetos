#Tupla de convidados 
convidados = ('Alice', 'Renato', 'Bob', 'Cleiton', 'Douglas')

#Lista de confirmações
confirmados = ['Renato', 'Douglas']

#Identificar quem ainda não confirmou
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

#Exibir os convidados que ainda não confirmaram
print("convidados que ainda não confirmaram:")
for pessoa in nao_confirmados:
    print(pessoa)

#Enviar lembretes aos não confirmados
print("\nEnviando lembretes para os convidados que ainda não confirmaram.")
