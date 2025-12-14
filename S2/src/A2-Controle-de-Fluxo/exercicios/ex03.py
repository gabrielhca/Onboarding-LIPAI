""" ex03 - identifica codigo do usuario"""


# o codigo identificador contem 7 caracteres
# começa com BR
# seguido de um numero inteiro entre 0001 e 9999
# por fim, terminacom o caractere X

codigo = input('Digite o codigo de usuario: ')

TAMANHO_CODIGO = 7
INICIO_CODIGO = 'BR'
FIM_CODIGO = 'X'
numero_codigo = codigo[2:6]

if len(codigo) == TAMANHO_CODIGO and codigo[0:2] == INICIO_CODIGO and codigo[-1:] == FIM_CODIGO and (numero_codigo.isdigit() and 1 <= int(numero_codigo) <= 9999):
    print("Codigo valido! Acesso permitido. :)")
else:
    print("Codigo invalido! Acesso negado. :(")
