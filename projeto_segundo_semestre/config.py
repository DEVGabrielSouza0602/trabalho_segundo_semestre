import time
import os


def limpeza_e_time(segundos):
    time.sleep(segundos)
    os.system('cls')


usuarios_permitidos = {
    'Usuarios': ['Gabriel', 'Felipe', 'Emanuel'],
    'Senhas': ['1223', '2334', '5546']
}

usuario_e_seus_dados = {
    'Nome': '',
    'Idade': 0,
    'Peso': 0.0,
    'Altura': '',
    'atividade fisica': None,
    'sexo': ''

}

usuario_master = {
    'Responsavel': 'admin',
    'Senha': '123456'
}

login_usuario_master = usuario_master['Responsavel']
senha_usuario_master = usuario_master['Senha']

loop_menu_usuario_comum = False
login_usuario_comum_efetuado = False
login_usuario_master_efetuado = False

escolha_do_menu_usuario = ''
escolha_do_menu_usuario_int = 0

dicionario_de_treinos = {
    'Segunda': ('Peito', 'Triceps'),
    'Terça': ('Costas', 'Biceps'),
    'Quarta': ('Pernas', 'Panturilha'),
    'Quinta': ('Peito', 'Triceps'),
    'Sexta': ('Ombro', 'Abdomem')
}


def apresentacao_dos_dias_da_semana(chaves_de_treinos):
    for numero, nome in enumerate(chaves_de_treinos):
        print(f'| [{numero}] {nome} ')
        time.sleep(0.5)


loop_ficha_de_treino = True
dias_da_semana_ficha_de_treino = dicionario_de_treinos.keys()
dia_digitado_corretamente = None

dicas_de_treino = ['Treine com progressão de carga🏋️‍♀️',
                   'Não Pule o treino de pernas🦵', 'Beba agua o dia todo.🥃💉']
loop_dicas_De_treino = True

# CALCULO TMB


def calcular_tmb(sexo_tmb, peso_tmb, altura_tmb, idade_tmb):
    if sexo_tmb == "M":
        tmb = float(66 + (13.8 * peso_tmb) +
                    (5 * altura_tmb) - (6.8 * idade_tmb))
        return tmb

    elif sexo_tmb == "F":
        tmb = float(665 + (9.6 * peso_tmb) +
                    (1.8 * altura_tmb) - (4.7 * idade_tmb))
        return tmb


# QUANTIDADE ÁGUA

def calcular_quantidade_agua(peso, formula):
    if formula == "padrao":
        return peso * 30
    elif formula == "atleta":
        return peso * 40
    elif formula == "personalizado":
        personalizacao = float(
            input("Informe a quantidade personalizada de água (ml/kg): "))
        return peso * personalizacao
    else:
        raise ValueError("Fórmula de cálculo não reconhecida")


# TABELA NUTRICIONAL

def verificar_vazio(lista):
    return len(lista) == 0


def push(lista, item):
    lista.append(item)


def size(lista):
    return len(lista)


alimento = ['Frango', 'Arroz branco', 'Feijão preto',
            'Batata doce', 'Banana', 'Maça', 'Pão integral']
quantidade_teste = [100, 100, 100, 100, 100, 100, 100]
valor_energético = [139, 130, 76, 100, 89, 52, 247]
carboidratos = [0.3, 28.2, 14, 24, 23, 14, 41]
proteinas = [26, 2.7, 4.3, 2, 1.1, 0.3, 13]
sodio = [153, 1, 99, 36, 1, 1, 400]

# Leitura e escrita de Arquivos
