""" Ex03 - Classe Participação """

from ex01 import Aluno
from ex02 import Projeto


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