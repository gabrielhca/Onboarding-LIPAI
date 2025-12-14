""" ex02 - somatorio com return"""


def somatorio(n1, n2, n3):
    """soma tres numeros"""
    soma = n1 + n2 + n3
    return soma


numero1 = int(input('Digite um numero:'))
numero2 = int(input('Digite outro numero:'))
numero3 = int(input('Digita so mais um:'))

print('O somatorio é:', somatorio(numero1, numero2, numero3))
