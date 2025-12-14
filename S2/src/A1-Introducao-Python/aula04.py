""" Aula 04 - Variaveis, Constantes e Literais"""

# Variaveis são containers para guarda dados

# Inferencia de tipo
numero = 10
print(numero, type(numero))

# Alterar o valor da variavel
numero = 20
print(numero)

# multiplas atribuições
nome, idade, endereco = "Caio", 25, "Rua Doce, 123"
print(nome, idade, endereco)

nome = "Cintia"
idade = 30
endereco = "Avenida Salgada, 456"
print(nome, idade, endereco)

# atribui o mesmo valor para varias variaveis
nome1 = nome2 = nome3 = "Ana"
print(nome1, nome2, nome3)

nome2 = "Beatriz"
print(nome1, nome2, nome3)

# variaveis
# snake_case
id_funcionario = 200
salario_mensal = 400.50
print(id_funcionario, salario_mensal)

# constantes
# UPPER_SNAKE_CASE
PI = 3.14
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18
print(PI, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

# literais
idade = 27
print(idade)
print(27)  # 27 é um literal de inteiro

# numericos
print(10, type(10))
print(10, type(-10))
print(3.14, type(3.14))

# string
print('Maria', type('Maria'))
print("João", type("João"))
print("Jhon's house")
print('Ele disse "Olá!"')

# booleano
print(True, type(True))
print(False, type(False))

# None
print(None, type(None))

# Coleções

# lista (list)
numeros = [1, 2, 3]
print(numeros, type(numeros))

# tupla (tuple)
emails = ('joao@mail.com', 'maria@mail.com')
print(emails, type(emails))

# conjunto (set)
# nomes repetidos são ignorados, conjunto não tem ordem
nomes = {'Ana', 'Maria', 'Carla', 'Maria'}
print(nomes, type(nomes))

# dicionario (dictionary)
aluno = {
    'prontuario': 12345,
    'nome': 'João Silva',
    'idade': 25
}

print(aluno, type(aluno))
