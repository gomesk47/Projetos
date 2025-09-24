# Lista de filme para classificação:
filmes = ["filme 1", "filme 2", "filme_3", "filme 4", "filme 5"]

# Mensagens de boas - vindas
print("Seja Bem vindo a noite de filmes")
print("Você tem cinco filmes para classificar")
print("Digite '0' a qualquer momento para parar. \n")

# loop para iterar sobre cada filme na lista
for filme in filmes:
    # solicita a classificação ao usuario
    classificacao = input(
        f"Como você classificaria o '{filme}' de 1 a 5 ? (ou 0 para parar): ")

    # Verficar se o usuario deseja parar
    if classificacao == '0':
        print("Que pena que você não irá classificar os filmes!")
        break  # Encerra o loop principal

# Converte a classificação para ver os números inteiros
classificacao = int(classificacao)

# Verificar se a classifição esta dentro do intervalo válido
if classificacao < 1 or classificacao > 5:
    print("Por favor, digite uma classificação valida de 1 a 5.")
else:
    # exibe a classificação e passa para o proximo filme
    print(f"Você classificou '{filme}' com '{classificacao}' estrelas. \n")

# Mensagens de agradecimento ao finalizar
print("Obrigado por classificar os filmes<3")
