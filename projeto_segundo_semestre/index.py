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
    elif usuario_inserido == config.login_usuario_master and senha_inserida == config.senha_usuario_master:
        config.login_usuario_master_efetuado = True
    else:
        print('Usuario ou senha incorreto.')
        config.limpeza_e_time(3)

    while config.login_usuario_comum_efetuado:
        print(f'Ola {usuario_inserido}, seja bem vindo')
        config.limpeza_e_time(2)
        print('Inicialmente vamos inserir seu dados: ')
        nome_do_usuario = input('Digite seu nome: ')
        idade_do_usuario = input('Digite sua idade: ')
        peso_do_usuario = input('Digite seu peso: ')
        altura_do_usuario = input('Digite sua altura: ')

        print('Armazenado seus dados...')
        config.limpeza_e_time(2)
        config.usuario_e_seus_dados['Nome'] = nome_do_usuario
        config.usuario_e_seus_dados['Idade'] = idade_do_usuario
        config.usuario_e_seus_dados['Peso'] = peso_do_usuario
        config.usuario_e_seus_dados['Altura'] = altura_do_usuario
        config.loop_menu_usuario_comum = True
        while config.loop_menu_usuario_comum:
            print('Menu Inicial')
            print('[1] Dicas de academia')
            print('[2] Ficha de treino')
            print('[3] Taxa De Metabolismo Basal')
            print('[4] Quantidade de Agua diario')
            print('[5] Dieta Basica')
            print('[6] Tabela Nutricional')
            print('[7] Visualizar seu dados')
            print('[0] Deslogar')
            config.escolha_do_menu_usuario = input(
                'Qual sua escolha com o numero indicado: ')
            try:
                config.escolha_do_menu_usuario_int = int(
                    config.escolha_do_menu_usuario)
                if config.escolha_do_menu_usuario_int == 0:
                    config.limpeza_e_time(2)
                    print(
                        f'Obrigado por utilizar, {nome_do_usuario}. Até mais. ')
                    print('Deslogando...')
                    config.limpeza_e_time(2)
                    config.loop_menu_usuario_comum = False
                    config.login_usuario_comum_efetuado = False
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
        config.limpeza_e_time(2)

    sair_tela_de_login = input(
        'Deseja sair do sistema: [S] ').lower().startswith('s')
    if sair_tela_de_login:
        time.sleep(1)
        print('Saindo do sistema. Até logo.')
        config.limpeza_e_time(2)
        controle_principal = False
    else:
        print('Reiniciando o sistema...')
        config.limpeza_e_time(2)
