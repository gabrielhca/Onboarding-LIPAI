""" Aula 02 - instrução if"""

# if condicao:
#     instrucao
#     instrucao
#     instrucao

codigo_cliente = 32
valor_desconto = 30.0
DESCONTO_ESPECIAL = valor_desconto >= 20.0

if DESCONTO_ESPECIAL:
    print("Desconto Especial")
    print(codigo_cliente)
else:
    print("Sem desconto especial")


# nome tem que ser maior que 3 caracteres
nome = "Ma"
print(len(nome), type(len(nome)))

NOME_INVALIDO = len(nome) < 3

if NOME_INVALIDO:
    print("Nome deve conter mais que 3 caracteres")
else:
    print("Nome valido")

NOME_VALIDO = len(nome) >= 3

if NOME_VALIDO:
    print("Nome valido")
else:
    print("Nome deve conter mais que 3 caracteres")

if not NOME_INVALIDO:
    print("Nome valido")
else:
    print("Nome deve conter mais que 3 caracteres")

# nome tem que ser maior que 3 caracteres
# idade tem que ser maior que 18 anos
# exerbir todos os erros no final apenas
nome = "Ma"
idade = 17
erros = []

NOME_INVALIDO = len(nome) < 3
if NOME_INVALIDO:
    erros.append("Nome deve conter mais que 3 caracteres")

IDADE_INVALIDA = idade < 18
if IDADE_INVALIDA:
    erros.append("Idade deve ser maior que 18 anos")

# False: False, None,0, 0.0, "", [], {}, ()
# True: todo o resto

if len(erros) != 0:
    print(erros)
else:
    print("Dados validos")

# verifica se um numero é positivo ou negativo
numero = -10

if numero > 0:
    print("Numero positivo")
elif numero == 0:
    print("zero")
else:
    print("Numero negativo")

# calcule a media e verifique se as duas notas
# são validas antes do calculo

n1 = 8.0
n2 = 7.5

if (n1 >= 0 and n1 <= 10) and (n2 >= 0 and n2 <= 10):
    media = (n1 + n2) / 2
    if media >= 6.0:
        print("Aprovado")
    elif media >= 4.0:
        print("Recuperação")
    else:
        print("Reprovado")
    print("Notas validas")
else:
    print("Notas invalidas")

NOTA1_VALIDA = not (0 <= n1 <= 10)
NOTA2_VALIDA = not (0 <= n2 <= 10)

if NOTA1_VALIDA and NOTA2_VALIDA:
    media = (n1 + n2) / 2
    if media >= 6.0:
        print("Aprovado")
    elif media >= 4.0:
        print("Recuperação")
    else:
        print("Reprovado")
else:
    print("Notas invalidas")
