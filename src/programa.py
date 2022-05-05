from pessoa import Pessoa
from gato import Gato
from galinha import Galinha

p1 = Pessoa('João', 42)
p2 = Pessoa('Maria', 18)

g1 = Gato('Bola', 1)


print(p1.mensagem())
print(p2.mensagem())
print(g1.mensagem())

ga1 = Galinha()
print(ga1.mensagem())