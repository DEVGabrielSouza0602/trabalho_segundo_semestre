from Alimentos import Alimentos

#CLASSE FILHA
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