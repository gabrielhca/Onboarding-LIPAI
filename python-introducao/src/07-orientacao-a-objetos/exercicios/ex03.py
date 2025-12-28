""" Ex03 - Classe Participação """


# classe participação
class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    # getter
    @property
    def codigo(self):
        return self._codigo

    @property
    def data_inicio(self):
        return self._data_inicio

    @property
    def data_fim(self):
        return self._data_fim

    @property
    def aluno(self):
        return self._aluno

    @property
    def projeto(self):
        return self._projeto

    # setter
    @codigo.setter
    def codigo(self, value):
        if not value or isinstance(value, str) and not value.isdigit():
            raise ValueError("Parametro numerico obrigatorio")
        self._codigo = int(value)

    @data_inicio.setter
    def data_inicio(self, value):
        if not value:
            raise ValueError("Parametro obrigatorio")
        self._data_inicio = value

    @data_fim.setter
    def data_fim(self, value):
        if not value:
            raise ValueError("Parametro obrigatorio")
        self._data_fim = value

    @aluno.setter
    def aluno(self, value):
        if not value:
            raise ValueError("Parametro obrigatorio")
        self._aluno = value

    @projeto.setter
    def projeto(self, value):
        if not value:
            raise ValueError("Parametro obrigatorio")
        self._projeto = value

    def __repr__(self):
        return f"Participação({self.codigo}, {self.data_inicio}, {self.data_fim}, {self.aluno}, {self.projeto})"


# classe projeto
class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    # getter
    @property
    def titulo(self):
        return self._titulo

    @property
    def responsavel(self):
        return self._responsavel

    @property
    def codigo(self):
        return self._codigo

    # setter
    @titulo.setter
    def titulo(self, value):
        if not value:
            raise ValueError("Parametro obrigatorio")
        self._titulo = value

    @responsavel.setter
    def responsavel(self, value):
        if not value:
            raise ValueError("Parametro obrigatorio")
        self._responsavel = value

    @codigo.setter
    def codigo(self, value):
        if not value or isinstance(value, str) and not value.isdigit():
            raise ValueError("Parametro numerico obrigatorio")
        self._codigo = int(value)

    @classmethod
    def contruir_com_string(cls, linha):
        partes = linha.split(",")
        return cls(codigo=partes[0].strip(), titulo=partes[1].strip(), responsavel=partes[2].strip())

    def __eq__(self, value):
        if isinstance(value, Projeto):
            return self.codigo == value.codigo
        return False

    def __hash__(self):
        return hash(self.codigo)

    def __repr__(self):
        return f"Projeto({self.codigo}, {self.titulo}, {self.responsavel})"


# classe aluno
class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    # getter
    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    @property
    def prontuario(self):
        return self._prontuario

    # setter
    @nome.setter
    def nome(self, value):
        if not value:
            raise ValueError("Parametro obrigatorio")
        self._nome = value

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Parametro obrigatorio")
        self._email = value

    @prontuario.setter
    def prontuario(self, value):
        if not value:
            raise ValueError("Parametro obrigatorio")
        self._prontuario = value

    @classmethod
    def contruir_com_string(cls, linha):
        partes = linha.split(",")
        return cls(prontuario=partes[0].strip(), nome=partes[1].strip(), email=partes[2].strip())

    def __eq__(self, value):
        if isinstance(value, Aluno):
            return self.prontuario == value.prontuario
        return False

    def __hash__(self):
        return hash(self.prontuario)

    def __repr__(self):
        return f"Aluno({self.prontuario}, {self.nome}, {self.email})"


# exemplo de uso
projeto1 = Projeto(5, "Laboratório de Analise de Dados", "Gabriel Amorim")
projeto2 = Projeto.contruir_com_string(
    "10, Laboratório de Desenvolvimento de IA, Pedro Gomes")
aluno1 = Aluno.contruir_com_string("SP0101, João da Silva, j@js.com")
aluno2 = Aluno("SP01", "Ana Silva", "b@b.com")

participacao1 = Participacao(1, "2023-01-01", "2023-06-30", aluno1, projeto1)
participacao2 = Participacao(2, "2023-02-01", "2023-07-31", aluno2, projeto2)
participacao3 = Participacao(3, "2023-03-01", "2023-08-31", aluno1, projeto2)
participacao4 = Participacao(4, "2023-04-01", "2023-09-30", aluno2, projeto1)

print(f"\nAluno(a) {participacao1.aluno.nome} participa do projeto {participacao1.projeto.titulo}")
print(f"\nAluno(a) {participacao2.aluno.nome} participa do projeto {participacao2.projeto.titulo}")
print(f"\nAluno(a) {participacao3.aluno.nome} participa do projeto {participacao3.projeto.titulo}")
print(f"\nAluno(a) {participacao4.aluno.nome} participa do projeto {participacao4.projeto.titulo}")