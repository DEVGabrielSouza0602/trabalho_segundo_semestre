import time
import os


def limpeza_e_time(segundos):
    time.sleep(segundos)
    os.system('clear')


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
