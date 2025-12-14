""" ex03 - somatorio com tupla """


def somatorio(x):
    """ somatorio """
    soma = 0
    for valor in x:
        soma += valor
    return soma


tupla = (1, 8, 9, 5)
print('Esse programa imprime apenas o numero', somatorio(tupla))
