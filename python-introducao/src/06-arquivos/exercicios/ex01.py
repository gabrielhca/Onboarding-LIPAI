""" ex01 - carregar dados de alunos """


def carregar_dados_alunos(nome_arquivo):
    """ retorna uma tupla de dicionarios com dados de alunos."""

    with open(f"python-introducao/src/06-arquivos/exercicios/{nome_arquivo}", 'r') as arquivo:
        dados_alunos = []
        partes = []
        for linha in arquivo:
            partes = linha.split(",")
            temp = {}
            temp["prontuario"] = partes[0].strip()
            temp["nome"] = partes[1].strip()
            temp["email"] = partes[2].strip()
            dados_alunos.append(temp)
    return tuple(dados_alunos)


registro_alunos = carregar_dados_alunos("dados_alunos.txt")
print(registro_alunos)
