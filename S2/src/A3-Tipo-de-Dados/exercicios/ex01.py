""" ex01 - maior e menor da lista"""

numeros = []
quantidade = 3

for i in range(quantidade):
    n = int(input("Digite um número inteiro: "))
    numeros.append(n)

maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("O maior numero é:", maior)
print("O menor numero é:", menor)
