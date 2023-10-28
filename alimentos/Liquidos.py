from Alimentos import Alimentos

#CLASSE FILHA
class Liquidos (Alimentos):
    def __init__ (self, nome, quantidade, calorias, carboidratos, proteinas, sodio, gordurasTotais):
        super().__init__(nome, tipo = "Fruta")
        self._quantidade = quantidade
        self._calorias = calorias
        self._carboidratos = carboidratos
        self._proteinas = proteinas
        self._sodio = sodio
        self._gordurasTotais = gordurasTotais

#MÉTODO com OVERRIDE
    def descreverAlimento (self):
        print(70*("="),
            f'\nTipo: {self._tipo}\n'
            f'Nome: {self._nome}\n'
            f'Quantidade Teste: {self._quantidade}ml\n'
            f'Valor Energético: {self._calorias}Kcal\n'
            f'Carboidratos: {self._carboidratos}g\n'
            f'Proteinas: {self._proteinas}g\n'
            f'Sodio: {self._sodio}mg\n'
            f'Gorduras Totais: {self._gordurasTotais}\n',
            70*("=")
        )