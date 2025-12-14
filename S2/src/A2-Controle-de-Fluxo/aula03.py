""" Aula 03 - loop for"""

# 1. repetir instruções
# 2. iteração em coleção de dados (listas, tuplas, dicionários, conjuntos)

linguagens = ['Python', 'Java', 'C#', 'JavaScript']

print(linguagens[0])
print(linguagens[1])
print(linguagens[2])

# for valor in colecao:
#     instrução
#     instrução
#     instrução

for linguagem in linguagens:
    print(linguagem.upper())

# comportamento do operador in
# é diferente com base no contexto
print('java' in linguagens)

nota1 = 8.0
nota2 = 7.5
nota3 = 6.0

media = (nota1 + nota2 + nota3) / 3
print(media)

notas = [8.0, 7.5, 6.0]

soma = 0.0
for nota in notas:
    soma += nota

media = soma / len(notas)
print(media)

# range
# valores = range(10)
# valores = range(0, 10)
# valores = range(0,10,2)
valores = range(10, -1, -1)
for valor in valores:
    print(valor)


for i in range(len(linguagens)):
    print(linguagens[i])