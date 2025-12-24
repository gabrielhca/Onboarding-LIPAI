""" Aula 01 - Introdução a funções"""

# função é um bloco que realiza uma tarefa específica
# dividir o programa em pequenas partes
# evita duplicação de código

# 1. Standard Library (funções prontas do python)
# ex: print(, len(), input()

print("Ola", 123, True)
nomes = ['Ana', 'Bia', 'Carlos']
tamanho_lista = len(nomes)
print(nomes, tamanho_lista)

# 2. User Defined Functions
# definidas pelo desenvolvedor(a)
# fazerem parte da solução do problema
# declara


def saudacoes():
    """saudação"""
    print("Olá!")


# chamada
saudacoes()
saudacoes()
saudacoes()

# declaração
# nome: saudacoes
# parâmetros: nome
# retorno: nenhum


def saudacoes_versao2(nome):
    """saudação"""
    print(f"Olá, {nome}")


# chamada
# valores, variaveis, expressoes => argumentos
# " Ana" é um argumento passado para o parâmetro nome
saudacoes_versao2("Ana")
saudacoes_versao2("Carlos")
nome = "Gabriel"
saudacoes_versao2(nome)

# declaração
# nome: calcular_media
# parâmetros: nota1, nota2, nota3
# retorno: nenhum


def calcular_media(nota1, nota2, nota3):
    """calcula a media"""
    media = (nota1 + nota2 + nota3) / 3
    print(media)


# chamada
# argumentos literais
calcular_media(8.0, 7.5, 6.0)

n1 = 9.0
n2 = 8.5
n3 = 7.0

# chamada
# argumentos variaveis
calcular_media(n1, n2, n3)

# declaração
# nome: calcular_media
# parâmetros: nota1, nota2, nota3
# retorno: media


def calcular_media_versao2(nota1, nota2, nota3):
    """calcula a media"""
    media = (nota1 + nota2 + nota3) / 3
    return media


# o uso é mais flexível
media = calcular_media_versao2(8.0, 7.5, 6.0)
print("Valor da média:", media)
# enviar no email
# salvar no banco de dados
# salvar em arquivo
