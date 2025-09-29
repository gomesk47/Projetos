# nome completo do aluno

nome_completo_do_aluno = str(input("Digite o nome completo do aluno: "))

# nota do aluno nas provas

atividade_1 = int(input("Digite a primeira nota da atividade: "))
atividade_2 = int(input("Digite a segunda nota da atividade: "))
atividade_3 = int(input("Digite a terceira nota da atividade: "))

# requisitos para aprovação

Média = (atividade_1+atividade_2+atividade_3)/3

if Média >= 5:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

# Resultado final das atividades

print(f"O aluno: {nome_completo_do_aluno}")
print(f"A média das notas é: {Média}")
print(f"Situação do aluno: {situacao}")
