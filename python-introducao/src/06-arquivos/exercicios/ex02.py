""" ex02 - carregar dados de projetos """


def carregar_dados_projetos(nome_arquivo):
    """ retorna uma tupla de dicionarios com dados de projetos"""

    with open(f"python-introducao/src/06-arquivos/exercicios/{nome_arquivo}", 'r') as arquivo:
        dados_projetos = []
        partes = []
        for linha in arquivo:
            partes = linha.split(",")
            temp = {}
            temp["codigo"] = int(partes[0].strip())
            temp["titulo"] = partes[1].strip()
            temp["responsavel"] = partes[2].strip()
            dados_projetos.append(temp)

    return tuple(dados_projetos)


registro_projetos = carregar_dados_projetos("dados_do_projeto.txt")
print(registro_projetos)
