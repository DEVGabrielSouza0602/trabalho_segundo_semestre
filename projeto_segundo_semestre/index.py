import dicas
import config
import time
import os

controle_principal = True

while controle_principal:
    usuario_inserido = input('Digite o seu Usuario: ').lower()
    senha_inserida = input('Digite a sua senha: ')
    if usuario_inserido in config.usuarios_permitidos['Usuarios']:
        if senha_inserida in config.usuarios_permitidos['Senhas']:
            config.login_usuario_comum_efetuado = True
        else:
            print('Usuario ou senha incorreto.')
            time.sleep(3)
            os.system('cls')
    elif usuario_inserido == config.login_usuario_master and senha_inserida == config.senha_usuario_master:
        config.login_usuario_master_efetuado = True
    else:
        print('Usuario ou senha incorreto.')
        time.sleep(3)
        os.system('cls')

    while config.login_usuario_comum_efetuado:
        print(f'Ola {usuario_inserido}, seja bem vindo')
        time.sleep(2)
        os.system('cls')
        print('Inicialmente vamos inserir seu dados: ')
        nome_do_usuario = input('Digite seu nome: ')
        idade_do_usuario = input('Digite sua idade: ')
        peso_do_usuario = input('Digite seu peso: ')
        altura_do_usuario = input('Digite sua altura: ')

        print('Armazenado seus dados...')
        time.sleep(2)
        config.usuario_e_seus_dados['Nome'] = nome_do_usuario
        config.usuario_e_seus_dados['Idade'] = idade_do_usuario
        config.usuario_e_seus_dados['Peso'] = peso_do_usuario
        config.usuario_e_seus_dados['Altura'] = altura_do_usuario
        loop_menu_usuario_comum = True
        while loop_menu_usuario_comum:
            print('Menu Inicial')
            print('[1] Dicas de academia')
            print('[2] Ficha de treino')
            print('[3] Taxa De Metabolismo Basal')
            print('[4] Quantidade de Agua diario')
            print('[5] Dieta Basica')
            print('[6] Tabela Nutricional')
            print('[7] Visualizar seu dados')
            print('[0] Sair')
            config.escolha_do_menu_usuario = input(
                'Qual sua escolha com o numero indicado: ')
            try:
                config.escolha_do_menu_usuario_int = int(
                    config.escolha_do_menu_usuario)
                if config.escolha_do_menu_usuario_int == 0:
                    print('escolha 00')
                elif config.escolha_do_menu_usuario_int == 1:
                    print('escolha 01')
                elif config.escolha_do_menu_usuario_int == 2:
                    print('escolha 02')

                elif config.escolha_do_menu_usuario_int == 3:
                    print('escolha 03')

                elif config.escolha_do_menu_usuario_int == 4:
                    print('escolha 04')

                elif config.escolha_do_menu_usuario_int == 5:
                    print('escolha 05')

                elif config.escolha_do_menu_usuario_int == 6:
                    print('escolha 06')

                elif config.escolha_do_menu_usuario_int == 7:
                    print('escolha 07')
                else:
                    print('Numero nao esta listado')
            except:
                print('Digite um numero disponivel !!!')

    while config.login_usuario_master_efetuado:
        print(f'Ola {usuario_inserido}, seja bem vindo')
        time.sleep(1)
        os.system('cls')

    sair_tela_de_login = input('Deseja sair: [S] ').lower().startswith('s')
    if sair_tela_de_login:
        time.sleep(1)
        print('Saindo do sistema. Até logo.')
        time.sleep(2)
        os.system('cls')
        controle_principal = False
    else:
        time.sleep(2)
        os.system('cls')
