class Gato:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mensagem(self):
        return f'Miau miau miua... eu sou o {self.nome}'
