""" Aula 02 - Atributos de Classe e de Instância """


# classe pessoa possui
# atributos de instância: nome e email
# atributos de class: especie
class Pessoa:
    """ Representa uma pessoa com nome e email """
    especie = "Humano"

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


pessoa1 = Pessoa("Ana Roberta", "ana.roberta@example.com")
pessoa2 = Pessoa("Tiago Moreira", "tiago.moreira@example.com")
pessoa3 = Pessoa("Carla Dias", "carla.dias@example.com")

# alterar um atrbuto de classe em uma instância
# alterará apenas para aquela instância
pessoa1.especie = "Alienígena Marinho"

# alterando um atributo de classe na classe
# altera todos os objetos e na classe tambem
Pessoa.especie = "Alienígena Gasoso"

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)
print(pessoa3.nome, pessoa3.email, pessoa3.especie)

print(Pessoa.especie)
