""" ex02 - definindo o mes com tuplas"""

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

numero_mes = int(input("Digite o numero do mes do seu aniversario (1-12): "))

if 1 <= numero_mes <= 12:
    mes_aniversario = meses[numero_mes - 1]
    print(f'Seu aniversario é em {mes_aniversario}.')
else:
    print("Numero errado! ('._.)")
