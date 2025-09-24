#Lista de nota dos estudantes
notas = [7.5, 8.0, 1.5, 2.4, 9.0]

#Função regular para calcular a média
def calcular_medida(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

#Função lambda para arredondar a média para as duas casa decimais
arredondar_media = lambda media: round(media, 2)

#calcular a media
media = calcular_medida(notas)
media_arredondada = arredondar_media(media)

#Verificar se os estudantes foram aprovados
situacao = 'aprovado' if media_arredondada >= 7 else "reprovado"

#Resultados
print ('Notas dos estudante:', notas)
print ('Média das notas:', media_arredondada)
print ('Situação do estudante:', situacao)