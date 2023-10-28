from Alimentos import Alimentos

#CLASSE FILHA
class Carnes (Alimentos):
    def __init__ (self, nome, quantidade, calorias, carboidratos, proteinas, fibras, sodio):
        super().__init__(nome, tipo = "Fruta")
        self._quantidade = quantidade
        self._calorias = calorias
        self._carboidratos = carboidratos
        self._proteinas = proteinas
        self._sodio = sodio
        self._fibras = fibras

#MÉTODO com OVERRIDE
    def descreverAlimento (self):
        print(70*("="),
            f'\nTipo: {self._tipo}\n'
            f'Nome: {self._nome}\n'
            f'Quantidade Teste: {self._quantidade}g\n'
            f'Valor Energético: {self._calorias}Kcal\n'
            f'Carboidratos: {self._carboidratos}g\n'
            f'Proteinas: {self._proteinas}g\n'
            f'Fibras: {self._fibras}'
            f'Sodio: {self._sodio}mg\n',
            70*("=")
        )