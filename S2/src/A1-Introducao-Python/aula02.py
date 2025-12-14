""" Aula 02 - Keywords e Identificadores """

# Palavras reservadas não podem ser usadas como identificadores
# Exemplos de palavras reservadas em Python:
# True, False, None, and, import, lambda

# Identificadores
# nome de variáveis, funções, classes, etc.
# case sensitive
# devem iniciar com letra ou _
# não pode ter espaços ou caracteres especiais
# recomenda-se usar letras minúsculas e _ para separar palavras

nome = 'Gabriel'
idade = 30

nome = 'Sofia'
nome_completo = 'Sofia Silva'

# Boas práticas (clean code)
# evitar nomes genéricos e abreviações, usar nomes descritivos
c = 10
contador = 10

s = 10 + 20
soma = 10 + 20

# Constantes
# por convenção, constantes são escritas em maiúsculas
idade = 1
PI = 3.14

idade = 20
MAIOR_IDADE = 18

if idade >= MAIOR_IDADE:
    print('Maior de idade')
else:
    print('Menor de idade')
