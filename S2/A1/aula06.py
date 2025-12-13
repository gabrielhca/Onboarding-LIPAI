""" Aula 06 - Conversão de Tipos """

# conversão de tipo implicita

leitura = 5.53
peso = 3

total = leitura + peso
print(total, type(total))

# conversão de tipo explicita
soma = 13.4 + float('3.5')

idade = int('27')
print(idade, type(idade))

nome = 'Maira'
altura = 1.70

# mensagem = nome + ' Tem a altura de ' + str(altura) + ' metros.'
mensagem = f'{nome} Tem a altura de {altura} metros.'
print(mensagem)
