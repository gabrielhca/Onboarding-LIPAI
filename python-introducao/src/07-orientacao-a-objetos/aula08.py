""" Aula 08 - Herança entre Classes – super()"""


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        print("Entrei no SUPER CONSTRUTOR")

    def obtem_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Cliente(Pessoa):  # SUBCLASSE
    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.compras = []


cliente = Cliente("Gabriel", "Amorim", "12345678900")
print(cliente.obtem_nome_completo())


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, salario):
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario

    def calcula_pagamento(self):
        return self.salario - ((10/100) * self.salario)


class Programador(Funcionario):
    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus

    def calcula_pagamento(self):
        salario_base = super().calcula_pagamento()
        return salario_base + self.bonus


funcionario = Funcionario("Henrique", "Carneiro", "98765432100", 5000)
print(funcionario.obtem_nome_completo())
print(funcionario.calcula_pagamento())

programador = Programador("Gabriel", "Amorim", "12345678900", 7000, 1500)
print(programador.obtem_nome_completo())
print(programador.calcula_pagamento())
