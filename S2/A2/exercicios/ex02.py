""" ex02 - Média Aritmética e Situação do Aluno"""

notas = input('Digite as notas (separe por espaço): ').split()
soma = 0.0
for nota in notas:
    soma += float(nota)
media = soma / len(notas)

print(f'A media aritimetica é: {media}')

SITUACAO_APROVADO = media >= 6.0
SITUACAO_RECUPERACAO = 4.0 <= media < 6.0

if SITUACAO_APROVADO:
    print('Situação: Aprovado')
elif SITUACAO_RECUPERACAO:
    print('Situação: Recuperação')
else:
    print('Situação: Reprovado')
