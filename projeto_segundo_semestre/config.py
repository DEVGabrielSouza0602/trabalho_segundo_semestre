import time
import os


def limpeza_e_time(segundos):
    time.sleep(segundos)
    os.system('cls')


usuarios_permitidos = {
    'Usuarios': ['Gabriel', 'DaquiPraFrenteSoParaTras', 'Emanuel'],
    'Senhas': ['1', '2334', '3445']
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


def escrever_treinos_em_arquivo(dicionario_de_treinos, dia_digitado):
    if escolha_menu_ficha == 2:
        if dia_digitado in dicionario_de_treinos:
            treinos_do_dia = dicionario_de_treinos[dia_digitado]
            nome_do_arquivo = "treinos_" + dia_digitado + ".txt"

            with open(nome_do_arquivo, 'w') as arquivo:
                for treino in treinos_do_dia:
                    arquivo.write(treino + "\n")

            print(
                f"Os treinos do dia {dia_digitado} foram salvos em {nome_do_arquivo}")
        else:
            print(f"O dia {dia_digitado} não está no dicionário de treinos.")


def fazer_login(usuario, senha):
    print(70 * "-")
    if usuario in config.usuarios_permitidos['Usuarios'] and senha in config.usuarios_permitidos['Senhas']:
        config.login_usuario_comum_efetuado = True
    elif usuario == config.login_usuario_master and senha == config.senha_usuario_master:
        config.login_usuario_master_efetuado = True
    else:
        print('Usuário ou senha incorretos.')
        config.limpeza_e_time(1)


def ler_nome_e_senha(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            if len(linhas) >= 2:
                return linhas[0].strip(), linhas[1].strip()
            else:
                print(
                    f"O arquivo '{nome_arquivo}' não contém informações suficientes.")
                return None, None
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None, None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None, None
