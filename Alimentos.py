from abc import abstractmethod, ABC


#CLASSE ABSTRATA / INTERFACE

class Alimentos (ABC):

    def __init__(self, nome, tipo):
        self._nome = nome
        self._tipo = tipo

#MÉTODO ABSTRATO
    @abstractmethod
    def descreverAlimento (self):
        pass

    