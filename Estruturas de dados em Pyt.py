#Função.lower e listcomp

linguagens = ['Python', 'Java', 'JavaScript', 'C', 'C#', 'C++', 'Swift', 'Cobalt', 'Kotlin']
print("Antes da listcomp = ", linguagens)
linguagens = [item.lower() for item in linguagens]
print("\nDepos da listcomp = ", linguagens)