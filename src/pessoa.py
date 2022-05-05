class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mensagem(self):
        return f'Olá! Meu nome é {self.nome} e eu tenho {self.idade} anos.'



