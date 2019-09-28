

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

    @property
    def ano(self):
        return self.__ano

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def dar_likes(self):
        self.__likes += 1

    def __str__(self):
        return f"{self.__nome} - {self.__ano} - {self.__likes}"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    @property
    def duracao(self):
        return self.__duracao

    def __str__(self):
        return f"{self.nome} - {self.__duracao} minutos - {self.ano} - {self.likes} likes"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    @property
    def temporadas(self):
        return self.__temporadas

    def __str__(self):
        return f"{self.nome} - {self.__temporadas} temporadas - {self.ano} - {self.likes} likes"


class Playlist():
    def __init__(self, nome, programas):
        self.__nome = nome
        self.__programas = programas

    def __getitem__(self, item):
        return self.__programas[item]

    @property
    def nome(self):
        return self.__nome

    @property
    def listagem(self):
        return self.__programas

    def __len__(self):
        return len(self.__programas)


vingadores = Filme("vingadores - guerra infinita", 2017, '136')
mr_robot = Serie("mr. Robot", 2017, 3)
suits = Serie("Suits", 2017, 3)

for _ in range(0, 75):
    vingadores.dar_likes()

for _ in range(0, 1250):
    mr_robot.dar_likes()

playlist = [vingadores, mr_robot]

my_playlist = Playlist("Roger_Playlist", playlist)

print(f"O tamanho da minha playlist é: {len(my_playlist)}")

for programa in my_playlist:
    print(programa)

my_playlist.listagem.append(suits)

print(f"O tamanho da minha playlist é: {len(my_playlist)}")

for programa in my_playlist:
    print(programa)
