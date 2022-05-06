from pessoa import Pessoa
from gato import Gato
from galinha import Galinha

qtd_pessoas = int(input('Quantas pessoas devem ser cadastradas?'))
pessoas = []

for i in range(qtd_pessoas): 
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    p = Pessoa(nome, idade)
    pessoas.append(p)

g1 = Gato('Bola', 1)

for i in range(qtd_pessoas): 
    print(pessoas[i].mensagem())

print(g1.mensagem())

