""" Aula 01 - Tipos de Dados - Listas"""

# lista
# ordenadas
# mutáveis
# indexaveis

nomes = ['Ana', 'Bia', 'Carlos']
print(nomes, type(nomes))

# acessar elementos
print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

# modificar elementos
nomes[0] = 'Alice'
nomes[1:] = ['Beatriz', 'Clara']
print(nomes)

# tamanho da lista
tamanho = len(nomes)
print(tamanho)

# adicionar elementos
nomes.append('Marta')
print(nomes)

# metodo insert
nomes.insert(0, 'Guilherme')
print(nomes)

nomes.insert(2, 'Nicole')
print(nomes)

# metodo extend
nomes2 = ['Monica', 'Fernando']
print(len(nomes))
nomes.extend(nomes2)
print(len(nomes))
print(nomes)

# remover elementos

# remove
nomes.remove('Nicole')
print(nomes)

# del
del nomes[0]
print(nomes)

# remove da memoria
# del nomes
# print(nomes)

# limpa a lista, mas não deleta da memoria
# nomes.clear()
# print(nomes)

# iteração em listas
for nome in nomes:
    print(nome)

print("-----")

for i in range(len(nomes)):
    print(nomes[i])