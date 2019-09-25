

class Programa:
    metodo_classe_texto = "Estude como usar classmethod."

    def __init__(self, nome, ano):
        self.__nome = nome
        self.__ano = ano
        self.__likes = 0

    @classmethod
    def metodo_classe(cls):
        return cls.metodo_classe_texto

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def dar_likes(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas


vingadores = Filme("vingadores - guerra infinita", 2017, '136')
mr_robot = Serie("mr. Robot", 2017, 3)

print(vingadores.nome)
print(f"{mr_robot.nome}")

for _ in range(0, 100):
    vingadores.dar_likes()

print(vingadores.likes)