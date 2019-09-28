class Funcionario:
    def __init__(self, nome):
        self.__nome = nome

    def registra_horas(self, horas):
        print("Horas registradas.")

    def mostrar_tarefas(self):
        print("Fez muita coisa...")

    @property
    def nome(self):
        return self.__nome


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print("Fez muita coisa, Caelumer.")

    def busca_curso_do_mes(self, mes=None):
        print(f"Mostra cursos - {mes}" if mes else "Mostrando cursos desse mes.")


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print("Fez muita coisa, Alurete.")

    def busca_perguntas_sem_resposta(self):
        print("Mostrando perguntas não respondidas do forum.")


class Hipster:
    def __str__(self):
        return f"Mr., {self.nome}"

class Junior(Alura):
    pass


class Pleno(Alura, Caelum, Hipster):
    pass

jose = Junior("Jose")
jose.busca_perguntas_sem_resposta()

rogerio = Pleno("Rogerio")
rogerio.busca_perguntas_sem_resposta()
rogerio.busca_curso_do_mes()
rogerio.mostrar_tarefas()

print(rogerio)

