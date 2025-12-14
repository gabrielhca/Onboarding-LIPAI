""" ex04 - somatorio usando * args """


def soma_args(*x):
    """ somatorio """
    soma = 0
    for valores in x:
        soma += int(valores)
    return soma


valor = input('Digite os valores separados por espaço:').split()
print('Somatorio:', soma_args(*valor))
