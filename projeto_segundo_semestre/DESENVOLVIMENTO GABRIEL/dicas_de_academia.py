
# CLASSE MÃE / HERANÇA SIMPLES---------------------------------------------------
import time
import os


class Dicas:
    def __init__(self, setor):
        self._setor = setor

    def imprimir(self):
        pass

# CLASSE FILHA ------------------------------------------------------------------


class DicasAlimentação:
    def __init__(self, nome, texto):
        super().__init__(nome, tipo="alimentação")
        self._texto = texto

    def imprimir(self, nome, texto):
        print(
            f'Tema: {self._nome}\n'
            f'{self._texto}'
        )


# CLASSE FILHA ------------------------------------------------------------------
class DicasExercícios:
    def __init__(self, nome, objetivo, texto):
        super().__init__(nome, tipo="exercício")
        self._objetivo = objetivo
        self._texto = texto

    def imprimir(self, nome, obejetivo, texto):
        print(
            f'Tema: {self._nome}\n'
            f'Objetivo: {self._objetivo}\n'
            f'{self._texto}'
        )


# CRIANDO OBJETOS ---------------------------------------------------------------
Hidratação = DicasAlimentação(
    'Hidratação', '"Hidratação é chave. Água mantém seus músculos funcionando adequadamente e ajuda na recuperação pós-treino."')

Suplementos = DicasAlimentação(
    'Suplementos', 'Suplementos podem ajudar, mas não substituem uma dieta equilibrada. Consulte um nutricionista para orientações específicas.')


dicas_de_treino = ['abc', 'fed', 'ghi']
loop_dicas_De_treino = True

while loop_dicas_De_treino:
    for i in dicas_de_treino:
        print('SISTEMA DE DICAS:'
              )
        time.sleep(1)
        print(i)
        time.sleep(2)
        print('Pressione [ENTER] para proxima dica...')
        pular_ou_sair = input(
            '[S] para sair do sistema... ').lower().startswith('s')
        time.sleep(1)
        os.system('cls')
        if pular_ou_sair is True:
            loop_dicas_De_treino = False
            break
