from abc import ABC # Abstract Base Classes
from collections.abc import MutableSequence
from collections.abc import Sized


class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao

    def __len__(self):
        return len(self.descricao)


lista = MinhaListagem("Rogerio")

print(len(lista))