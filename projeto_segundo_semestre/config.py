import time
import os


def limpeza_e_time(segundos):
    time.sleep(segundos)
    os.system('cls')


usuarios_permitidos = {
    'Usuarios': ['abc', 'def', 'ghi'],
    'Senhas': ['1223', '2334', '5546']
}

usuario_e_seus_dados = {
    'Nome': '',
    'Idade': 0,
    'Peso': 0.0,
    'Altura': '',
    'atividade fisica': None,

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
    'Segunda': ('a', 'b', 'c'),
    'Terça': ('e', '2', '3'),
    'Quarta': ('b', '5', 'f'),
    'Quinta': ('8', 'o', 'v'),
    'Sexta': ('1', '0', 's')
}


def apresentacao_dos_dias_da_semana(chaves_de_treinos):
    for numero, nome in enumerate(chaves_de_treinos):
        print(f'| [{numero}] {nome} ')
        time.sleep(0.5)


loop_ficha_de_treino = True
dias_da_semana_ficha_de_treino = dicionario_de_treinos.keys()
dia_digitado_corretamente = None
