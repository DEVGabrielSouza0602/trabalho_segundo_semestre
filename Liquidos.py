from Alimentos import Alimentos

#CLASSE FILHA
class Liquidos (Alimentos):
    def __init__ (self, nome, quantidade, calorias, carboidratos, proteinas, sodio, gordurasTotais):
        super().__init__(nome, tipo = "Líquido")
        self._quantidade = quantidade
        self._calorias = calorias
        self._carboidratos = carboidratos
        self._proteinas = proteinas
        self._sodio = sodio
        self._gordurasTotais = gordurasTotais

#MÉTODO com OVERLOAD
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
