""" ex01 - somatorio com parametro"""


def somatorio(n1, n2, n3):
    """soma tres numeros"""
    soma = n1 + n2 + n3
    print('O somatorio é:', soma)


numero1 = int(input('Digite um numero:'))
numero2 = int(input('Digite outro numero:'))
numero3 = int(input('Digita so mais um:'))

somatorio(numero1, numero2, numero3)
