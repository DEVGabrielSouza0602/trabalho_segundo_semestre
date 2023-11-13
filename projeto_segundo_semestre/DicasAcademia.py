
# CLASSE MÃE / HERANÇA SIMPLES---------------------------------------------------
import time
import os


class DicasAcademia:
    def __init__(self, titulo, tipo):
        self._titulo = titulo
        self._tipo = tipo

    def imprimir(self):
        pass

# CLASSE FILHA ------------------------------------------------------------------


class DicasAlimentação (DicasAcademia):
    def __init__(self, titulo, texto):
        super().__init__(titulo, tipo="alimentação")
        self._texto = texto

    def imprimir(self, titulo):
        print(
            f'Tema: {self._titulo}\n'
            f'Dica: {self._texto}'
        )


# CLASSE FILHA ------------------------------------------------------------------
class DicasExercícios (DicasAcademia):
    def __init__(self, titulo, objetivo, texto):
        super().__init__(titulo, tipo="exercício")
        self._objetivo = objetivo
        self._texto = texto

    def imprimir(self, titulo, objetivo):
        print(
            f'Tema: {self._titulo}\n'
            f'Objetivo: {self._objetivo}\n'
            f'Dica: {self._texto}'
        )


# CRIANDO OBJETOS ---------------------------------------------------------------
Hidratação = DicasAlimentação(
    'Hidratação', '"Hidratação é chave. Água mantém seus músculos funcionando adequadamente e ajuda na recuperação pós-treino."')

Suplementos = DicasAlimentação(
    'Suplementos', 'Suplementos podem ajudar, mas não substituem uma dieta equilibrada. Consulte um nutricionista para orientações específicas.')

Intervalos = DicasExercícios(
    'Intervalos', 'Intensidade', 'Intervalos de alta intensidade: alternar entre períodos de alta e baixa intensidade pode acelerar a queima de gordura.')

Cardio = DicasExercícios(
    'Cardio', 'Queima de calorias', 'Combine treinos de cardio e musculação para maximizar a queima de calorias e tonificar o corpo.')

#LISTA PARA ARMAZENAR OS TEMAS DE DICAS-----------------------------------------
listaDicasAlimentação = []
listaDicasExercícios = []
listaDicasAlimentação.append(Hidratação._titulo)
listaDicasAlimentação.append(Suplementos._titulo)
listaDicasExercícios.append(Intervalos._titulo)
listaDicasExercícios.append(Cardio._titulo)
