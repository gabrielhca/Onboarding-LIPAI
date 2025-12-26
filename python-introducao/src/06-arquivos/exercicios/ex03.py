""" ex 03 - Convertendo uma linha em dicionario genérico """


def linha_para_dict(linha, chaves):
    """Recebe uma linha e uma lista de chaves e retorna um dicionário"""

    partes = linha.split(",")
    result = {}
    if len(partes) < len(chaves):
        return None

    for i in range(len(chaves)):
        result[chaves[i]] = partes[i].strip()
    return result


def carregar_dados_alunos(nome_arquivo):
    """ retorna uma tupla de dicionarios com dados de alunos."""

    with open(f"python-introducao/src/06-arquivos/exercicios/{nome_arquivo}", 'r') as arquivo:
        dados_alunos = []
        for linha in arquivo:
            temp = linha_para_dict(linha, ["prontuario", "nome", "email"])
            dados_alunos.append(temp)
    return tuple(dados_alunos)


def carregar_dados_projetos(nome_arquivo):
    """ retorna uma tupla de dicionarios com dados de projetos"""

    with open(f"python-introducao/src/06-arquivos/exercicios/{nome_arquivo}", 'r') as arquivo:
        dados_projetos = []
        partes = []
        for linha in arquivo:
            partes = linha.split(",")
            temp = linha_para_dict(linha, ["codigo", "titulo", "responsavel"])
            dados_projetos.append(temp)

    return tuple(dados_projetos)


registro_alunos = carregar_dados_alunos("dados_alunos.txt")
registro_projetos = carregar_dados_projetos("dados_do_projeto.txt")
print(registro_alunos)
print(registro_projetos)
