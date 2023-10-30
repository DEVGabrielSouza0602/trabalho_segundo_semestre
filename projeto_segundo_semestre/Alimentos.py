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

#CLASSE FILHA | CARNES -----------------------------------------------------------------------
class Carnes (Alimentos):
    def __init__ (self, nome, quantidade, calorias, carboidratos, proteinas, fibras, sodio):
        super().__init__(nome, tipo = "Carne")
        self._quantidade = quantidade
        self._calorias = calorias
        self._carboidratos = carboidratos
        self._proteinas = proteinas
        self._sodio = sodio
        self._fibras = fibras

#MÉTODO com OVERRIDE
    def descreverAlimento (self):
        print(
            f'\nTipo: {self._tipo}\n'
            f'Nome: {self._nome}\n'
            f'Quantidade Teste: {self._quantidade}g\n'
            f'Valor Energético: {self._calorias}Kcal\n'
            f'Carboidratos: {self._carboidratos}g\n'
            f'Proteinas: {self._proteinas}g\n'
            f'Fibras: {self._fibras}\n'
            f'Sodio: {self._sodio}mg\n',
        )

#CLASSE FILHA | FRUTAS -----------------------------------------------------------------------
class Frutas (Alimentos):
    def __init__ (self, nome, quantidade, calorias, carboidratos, proteinas, sodio):
        super().__init__(nome, tipo = "Fruta")
        self._quantidade = quantidade
        self._calorias = calorias
        self._carboidratos = carboidratos
        self._proteinas = proteinas
        self._sodio = sodio

#MÉTODO com OVERRIDE
    def descreverAlimento (self):
        print(
            f'\nTipo: {self._tipo}\n'
            f'Nome: {self._nome}\n'
            f'Quantidade Teste: {self._quantidade}g\n'
            f'Valor Energético: {self._calorias}Kcal\n'
            f'Carboidratos: {self._carboidratos}g\n'
            f'Proteinas: {self._proteinas}g\n'
            f'Sodio: {self._sodio}mg\n'
        )

#CLASSE FILHA | GRAOS -----------------------------------------------------------------------
class Graos (Alimentos):
    def __init__ (self, nome, quantidade, calorias, carboidratos, proteinas, fibras, sodio):
        super().__init__(nome, tipo = "Grão")
        self._quantidade = quantidade
        self._calorias = calorias
        self._carboidratos = carboidratos
        self._proteinas = proteinas
        self._fibras = fibras
        self._sodio = sodio

#MÉTODO com OVERRIDE
    def descreverAlimento (self):
        print(
            f'\nTipo: {self._tipo}\n'
            f'Nome: {self._nome}\n'
            f'Quantidade Teste: {self._quantidade}ml\n'
            f'Valor Energético: {self._calorias}Kcal\n'
            f'Carboidratos: {self._carboidratos}g\n'
            f'Proteinas: {self._proteinas}g\n'
            f'Fibras: {self._fibras}g\n'
            f'Sodio: {self._sodio}mg\n'
        )

#CLASSE FILHA | LIQUIDOS -----------------------------------------------------------------------
class Liquidos (Alimentos):
    def __init__ (self, nome, quantidade, calorias, carboidratos, proteinas, sodio, gordurasTotais):
        super().__init__(nome, tipo = "Líquido")
        self._quantidade = quantidade
        self._calorias = calorias
        self._carboidratos = carboidratos
        self._proteinas = proteinas
        self._sodio = sodio
        self._gordurasTotais = gordurasTotais

#MÉTODO com OVERRIDE
    def descreverAlimento (self):
        print(
            f'\nTipo: {self._tipo}\n'
            f'Nome: {self._nome}\n'
            f'Quantidade Teste: {self._quantidade}ml\n'
            f'Valor Energético: {self._calorias}Kcal\n'
            f'Carboidratos: {self._carboidratos}g\n'
            f'Proteinas: {self._proteinas}g\n'
            f'Sodio: {self._sodio}mg\n'
            f'Gorduras Totais: {self._gordurasTotais}\n'
        )

#CLASSE FILHA | VERDURAS -----------------------------------------------------------------------
class Verduras (Alimentos):
    def __init__ (self, nome, quantidade, calorias, carboidratos, proteinas, sodio):
        super().__init__(nome, tipo = "Verdura")
        self._quantidade = quantidade
        self._calorias = calorias
        self._carboidratos = carboidratos
        self._proteinas = proteinas
        self._sodio = sodio

#MÉTODO com OVERRIDE
    def descreverAlimento (self):
        print(
            f'\nTipo: {self._tipo}\n'
            f'Nome: {self._nome}\n'
            f'Quantidade Teste: {self._quantidade}g\n'
            f'Valor Energético: {self._calorias}Kcal\n'
            f'Carboidratos: {self._carboidratos}g\n'
            f'Proteinas: {self._proteinas}g\n'
            f'Sodio: {self._sodio}mg\n'
        )

#CRIANDO OS ALIMENTOS
Frango = Carnes("Frango", 100, 159, 0, 32, 0, 50)
ArrozBranco = Graos("ArrozBranco", 100, 32, 7.03, 0.63, 0.40, 0.25)
FeijãoPreto = Graos("FeijãoPreto", 100, 77, 14, 4.5, 8.4, 1.9)
BatataDoce = Verduras("BatataDoce", 100, 53.90, 12.88, 0.42, 2.10)
Banana = Frutas("Banana", 100, 39.60, 10.32, 0.52, 0)
Maça = Frutas("Maça", 100, 67.60, 17.95, 0.34, 1.30)
Leite = Liquidos("Leite", 100, 120, 9.60, 6, 130, 6.40)

#LISTA PARA ARMAZENAR OS NOMES DOS ALIMENTOS
listaNomesAlimentos = []
listaNomesAlimentos.append(Frango._nome)
listaNomesAlimentos.append(ArrozBranco._nome)
listaNomesAlimentos.append(FeijãoPreto._nome)
listaNomesAlimentos.append(BatataDoce._nome)
listaNomesAlimentos.append(Banana._nome)
listaNomesAlimentos.append(Maça._nome)
listaNomesAlimentos.append(Leite._nome)