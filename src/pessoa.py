class Pessoa:

    def __init__(self, nome, idade, gosta_futebol):
        self.nome = nome
        self.idade = idade
        self.gosta_futebol = gosta_futebol

    def mensagem(self):
        return f'Olá! Meu nome é {self.nome} e eu tenho {self.idade} anos.'

    def gosta_futebol(self):
        if self.gosta_futebol:
            return "Sim! Eu gosto de futebol!"
        return "Não. Não gosto de futebol"

