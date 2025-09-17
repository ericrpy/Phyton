class Pessoa:
    def __init__(self, nome, sobrenome): # função com inicializador da instância, self é para se referir a instÂncia atual
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Luiz', 'Otávio')
p2 = Pessoa('Maria', 'Joana')

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
