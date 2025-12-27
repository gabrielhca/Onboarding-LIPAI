""" Ex 01 - Classe Aluno """


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


entrada = "SP0101, João da Silva, joao@email.com"
aluno_teste = Aluno.contruir_com_string(entrada)
print(aluno_teste)

aluno1 = Aluno("SP01", "Ana", "a@a.com")
aluno2 = Aluno("SP01", "Ana Silva", "b@b.com")

conjunto_de_alunos = {aluno1, aluno2}
print(f"Aluno1 == Aluno2? {aluno1 == aluno2}")
print(f"Tamanho do conjunto: {len(conjunto_de_alunos)}")
