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
                    config.limpeza_e_time(2)
                    while config.loop_dicas_De_treino:
                        for i in config.dicas_de_treino:
                            print('SISTEMA DE DICAS:')
                            time.sleep(1)
                            print(i)
                            time.sleep(2)
                            print('Pressione [ENTER] para proxima dica...')
                            pular_ou_sair = input(
                                '[S] para sair do sistema... ').lower().startswith('s')
                            time.sleep(1)
                            os.system('cls')
                            if pular_ou_sair is True:
                                config.loop_dicas_De_treino = False
                                break

                elif config.escolha_do_menu_usuario_int == 2:
                    while config.loop_ficha_de_treino:
                        time.sleep(2)
                        os.system('cls')
                        print('Seja bem vindo a sua ficha de treino')
                        config.apresentacao_dos_dias_da_semana(
                            config.dias_da_semana_ficha_de_treino)

                        dia_digitado = input(
                            'Digite o numero do dia para treino: ')

                        try:
                            dia_digitado = int(dia_digitado)
                            if dia_digitado < 0 or dia_digitado > 4:
                                print('Dia não disponivel para treino..')
                                time.sleep(1.5)
                                os.system('cls')
                            else:
                                print('Dia disponivel para treino..')
                                time.sleep(1.5)
                                os.system('cls')
                                config.dia_digitado_corretamente = True
                        except ValueError:
                            print('Insira apenas numeros...')
                            time.sleep(1.5)
                            os.system('cls')

                        for numero, nome in enumerate(config.dias_da_semana_ficha_de_treino):
                            if numero == dia_digitado:
                                dia = nome
                                if nome in config.dicionario_de_treinos.keys():
                                    for i in config.dicionario_de_treinos[nome]:
                                        print(i, end=" | ")
                                        time.sleep(1)

                        print('\nDeseja sair [s]')
                        sair_sistema_de_treino = input(
                            'Deseja ver outro treino [ENTER] ').lower().startswith('s')
                        time.sleep(1)
                        os.system('cls')
                        if sair_sistema_de_treino is True:
                            config.loop_ficha_de_treino = False

                elif config.escolha_do_menu_usuario_int == 3:
                    print('escolha 03')
                    # Informações do usuário (podemos mudar depois já que o usuario tem tudo)
                    sexo = input(
                        "Informe o sexo (M para masculino, F para feminino): ").upper()
                    peso = float(input("Informe o peso em kg: "))
                    altura = float(input("Informe a altura em cm: ")) / \
                        100  # Pra converter os cm em metros
                    idade = int(input("Informe a idade em anos: "))

                    tmb = config.calcular_tmb(sexo, peso, altura,
                                              idade)  # Calcular a TMB

                    if tmb != "":
                        print(
                            f"A sua TMB é de aproximadamente {tmb:.2f} calorias por dia.")
                    else:
                        print(
                            "Sexo não reconhecido. Use 'M' para masculino ou 'F' para feminino.")
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
