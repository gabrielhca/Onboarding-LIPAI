""" ex05 - calculadora IMC com dicionario """


def calcula_imc(peso, altura):
    """ calcula IMC"""
    return peso / (altura * altura)


def obter_classificacao_imc(x):
    """ retorna o imc de um individuo com base na sua altura e peso"""
    if x < 18.5:
        print('Resultado: abaixo do peso!')
    elif 18.5 <= x <= 24.9:
        print('Resultado: peso normal.')
    elif 25.0 <= x <= 29.9:
        print('Resultado: excesso de peso!')
    elif 30.0 <= x <= 34.9:
        print('Resultado: obesidade de classe 1!')
    elif 35.0 <= x <= 39.9:
        print('Resultado: obesidade de classe 2!')
    elif x >= 40.0:
        print('Resultado: obesidade de classe 3!')


def situacao_individuo(x):
    """ retorna a situação ('normal', 'perde peso', 'ganhar peso') com base no IMC"""
    if x < 18.5:
        print('Situação: ganhar peso')
    elif 18.5 <= x <= 24.9:
        print('Situação: normal')
    elif x >= 25.0:
        print('Situação: perder peso')


individuo = {}
individuo["peso"] = float(input('Informe seu peso: '))
individuo["altura"] = float(input('Informe sua altura: '))

imc = calcula_imc(individuo["peso"], individuo["altura"])
obter_classificacao_imc(imc)
situacao_individuo(imc)
