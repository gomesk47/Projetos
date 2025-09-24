# Nota do aluno nas quatro provas

Nota_1 = int(input("Digite a primeira nota: "))
Nota_2 = int(input("Digite a segunda nota: "))
Nota_3 = int(input("Digite a terceira nota: "))
Nota_4 = int(input("Digite a quarta nota: "))

# Condições para aprovação do aluno.

Média = (Nota_1+Nota_2+Nota_3+Nota_4)/4

if Média >= 5:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

# Dadas as notas mostramos a média final e a situação do aluno.

print(f"A média das notas é: {Média}")
print(f"Situação do aluno: {situacao}")


