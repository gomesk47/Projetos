from collections import defaultdict
import matplotlib.pyplot as plt

print("SEJA BEM VINDO A BIBLIOTECA CODEX")

class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Gênero: {self.genero}, Quantidade: {self.quantidade}"


# Lista de livros já cadastrados

livros = [
    Livro("Dom Casmurro", "Machado de Assis", "Romance", 5),
    Livro("Python Fluente", "Luciano Ramalho", "Programação", 3),
    Livro("Clean Code", "Robert C. Martin", "Programação", 2),
    Livro("Pai Rico, Pai Pobre", "Robert Kiyosaki", "Finanças Pessoais", 4),
    Livro("It", "Stephen King", "Terror", 6),
    Livro("O Poder do Hábito", "Charles Duhigg", "Autoajuda", 3)
]


# cadastro de livros na biblioteca

def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o gênero do livro: ")
    try:
        quantidade = int(input("Digite a quantidade disponível: "))
    except ValueError:
        print("Quantidade inválida! Deve ser um número inteiro.")
        return
    novo_livro = Livro(titulo, autor, genero, quantidade)
    livros.append(novo_livro)
    print("Livro cadastrado com sucesso!")

# listar livros

def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    for livro in livros:
        print(livro)

# buscar livros

def buscar_livro_por_titulo():
    titulo = input("Digite o título do livro que deseja buscar: ").lower()
    encontrados = [livro for livro in livros if livro.titulo.lower() == titulo]

    if encontrados:
        for livro in encontrados:
            print(livro)
    else:
        print("Livro não encontrado.")

# gerar grafico

def gerar_grafico_por_genero():
    if not livros:
        print("Nenhum livro cadastrado para gerar gráfico.")
        return

    genero_dict = defaultdict(int)

    for livro in livros:
        genero_dict[livro.genero] += livro.quantidade

    generos = list(genero_dict.keys())
    quantidades = list(genero_dict.values())

    plt.figure(figsize=(10, 6))
    plt.bar(generos, quantidades, color='skyblue')
    plt.title("BIBLIOTECA CODEX")
    plt.xlabel("Quantidade de Livros por Gênero")
    plt.ylabel("Quantidades disponíveis")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# mini grafico com sistema de gerenciamento de biblioteca

def menu():
    while True:
        print("\n=== Selecione a opção desejada ===")
        print("1. Cadastrar novo livro")
        print("2. Listar todos os livros")
        print("3. Buscar livro por título")
        print("4. Gerar gráfico de livros por gênero")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_livro()
        elif escolha == "2":
            listar_livros()
        elif escolha == "3":
            buscar_livro_por_titulo()
        elif escolha == "4":
            gerar_grafico_por_genero()
        elif escolha == "5":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()