""" ex06 - informações sobre aquarios """


def volume_aquario(comprimento, altura, largura):
    """ calcula o volume """
    return (comprimento * altura * largura) / 1000


def potencia_termostato(volume, temperatura_desejada, temperatura_ambiente):
    """calcula potencia do termostato"""
    return volume * 0.05 * (temperatura_desejada - temperatura_ambiente)


def filtragem_hora(volume):
    """calcula a friltragem"""
    print(f'A filtragem recomendada fica entre {volume * 2} e {volume * 3}')


aquario = {}

aquario["comprimento"] = float(input("Informe o comprimento do aquario: "))
aquario["altura"] = float(input("Informe a altura do aquario: "))
aquario["largura"] = float(input("Informe a largura do aquario: "))
aquario["temperatura_desejada"] = float(
    input("Informe a temperatura desejada: "))
aquario["temperatura_ambiente"] = float(
    input("Informe a temperatura_ambiente: "))

volume_litros = volume_aquario(
    aquario["comprimento"], aquario["altura"], aquario["largura"])
potencia = potencia_termostato(
    volume_litros, aquario["temperatura_desejada"], aquario["temperatura_ambiente"])
print('Relatorio:')
print(f'Volume do seu aquario é {volume_litros} L')
print(f'A potencia do termostado recomendada é {potencia}')
filtragem_hora(volume_litros)
