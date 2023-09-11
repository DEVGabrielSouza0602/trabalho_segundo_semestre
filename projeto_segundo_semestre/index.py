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
        sexo_do_usuario = input(
            "Informe o sexo (M para masculino, F para feminino): ")
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
        config.usuario_e_seus_dados['sexo'] = sexo_do_usuario
        config.loop_menu_usuario_comum = True
        while config.loop_menu_usuario_comum:
            print('Menu Inicial')
            print('[1] Dicas de academia')
            print('[2] Ficha de treino0')
            print('[3] Taxa De Metabolismo Basal')
            print('[4] Quantidade de Agua diario')
            print('[5] Dieta Basica')
            print('[6] Tabela Nutricional')
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
                            'Digite o numero d dia para treino: ')

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
                    config.limpeza_e_time(2)
                    # Informações do usuário (podemos mudar depois já que o usuario tem tudo)
                    peso = float(peso_do_usuario)
                    altura = altura_do_usuario / \
                        100  # Pra converter os cm em metros
                    idade = int(input("Informe a idade em anos: "))

                    tmb = config.calcular_tmb(config.sexo, config.peso, config.altura,
                                              config.idade)  # Calcular a TMB

                    if tmb != "":
                        print(
                            f"A sua TMB é de aproximadamente {tmb:.2f} calorias por dia.")
                    else:
                        print(
                            "Sexo não reconhecido. Use 'M' para masculino ou 'F' para feminino.")
                elif config.escolha_do_menu_usuario_int == 4:
                    config.limpeza_e_time(2)
                    looping_quantidade_agua = True
                    while looping_quantidade_agua:
                        peso = float(peso_do_usuario)
                        # escolha a fórmula mais adequada para fazer o cálculo
                        print("Escolha a fórmula de cálculo:")
                        print("1 - Fórmula padrão (30 ml/kg)")
                        print("2 - Fórmula para atletas (40 ml/kg)")
                        print("3 - Fórmula personalizada")
                        opcao = int(
                            input("Digite o número da opção desejada: "))

                        # calcula a quantidade recomendada de água com base na escolha do usuário
                        if opcao == 1:
                            quantidade_agua_ml = config.calcular_quantidade_agua(
                                peso, "padrao")
                        elif opcao == 2:
                            quantidade_agua_ml = config.calcular_quantidade_agua(
                                peso, "atleta")
                        elif opcao == 3:
                            quantidade_agua_ml = config.calcular_quantidade_agua(
                                peso, "personalizado")
                        else:
                            print("Opção inválida.")
                            quantidade_agua_ml = 0

                        if quantidade_agua_ml > 0:
                            print(
                                f"Você deve tomar aproximadamente {quantidade_agua_ml:.2f} ml de água por dia.")
                        print('\nDeseja sair [s]')
                        sair_sistema_de_agua = input(
                            'Deseja ver outro treino [ENTER] ').lower().startswith('s')
                        time.sleep(1)
                        os.system('cls')
                        if sair_sistema_de_agua is True:
                            looping_quantidade_agua = False

                elif config.escolha_do_menu_usuario_int == 5:
                    print('escolha 05')
                    permanecer_na_dieta = True

                    while permanecer_na_dieta:
                        print(70*"=") #Cabeçario das Dietas
                        print("                          DIETAS BÁSICAS")
                        print(70*"=")
                        print("Frequência de Exercícios")
                        print(70*"-")
                        print("[1] Pouco ou nenhum (nenhum ou 1 dia na semana)")
                        print("[2] Leve (1 a 3 dias na semana)")
                        print("[3] Moderado (3 a 5 dias na semana)")
                        print("[4] Pesado (6 a 7 dias na semana)")
                        print("[5] Muito pesado (diariamente ou 2X ao dia)")
                        print("[0] Voltar ao menu")
                        print(70*"-")
                        escolha_frequencia = int(input("Digite o indice de acordo com a frequência que você se exercita: "))

                        if escolha_frequencia == 1:
                            frequencia = 1.2
                        elif escolha_frequencia == 2:
                            frequencia = 1.375
                        elif escolha_frequencia == 3:
                            frequencia = 1.55
                        elif escolha_frequencia == 4:
                            frequencia = 1.725
                        elif escolha_frequencia == 5:
                            frequencia = 1.9
                        elif escolha_frequencia == 0:
                            permanecer_na_dieta = False

                        if escolha_frequencia != 0:
                            gasto_energetico = round(config.calcular_tmb * frequencia, 2)
                            consumo_proteinas_diario = round(peso_do_usuario * 3, 2)
                            consumo_calorias_diario_massa = round(gasto_energetico + 750, 2)
                            consumo_calorias_diario_emagrecimento = round(gasto_energetico - 500, 2)
                            quantidade_proteinas_refeicao = round(consumo_proteinas_diario/6, 2)
                            quantida_calorias_refeicao_emagrecimento = round(consumo_calorias_diario_emagrecimento/6, 2)
                            quantida_calorias_refeicao_massa = round(consumo_calorias_diario_massa/6, 2)

                            os.system("cls")
                            print(70*"=") #Cabeçario das Dietas
                            print("                          DIETAS BÁSICAS")
                            print(70*"=")
                            print("[1] Emagrecer")
                            print("[2] Ganhar massa muscular")
                            print(70*"-")
                            escolha_dieta = int(input("Digite o indice para escolher a dieta: "))
                            os.system("cls")
                                
                            if escolha_dieta == 1:
                                print(70*"=") #Cabeçario das Dietas
                                print("                          DIETAS BÁSICAS")
                                print(70*"=")
                                print("OBJETIVO: Emagrecer")
                                print(70*"-")
                                print("CONSUMO IDEAL- 6 refeições\n")
                                print(f"Diário de calorias: {consumo_calorias_diario_emagrecimento}kcal")
                                print(f"Diário de proteínas: {consumo_proteinas_diario}g")
                                print(f"Por refeição de calorias: {quantida_calorias_refeicao_emagrecimento}kcal")
                                print(f"Por refeição de proteínas: {quantidade_proteinas_refeicao}g")
                                print(70*"-")
                                time.sleep(1)
                                input("Pressione ENTER para continuar")
                                os.system("cls")

                            if escolha_dieta == 2:
                                print(70*"=") #Cabeçario das Dietas
                                print("                          DIETAS BÁSICAS")
                                print(70*"=")
                                print("OBJETIVO: ganhar massa muscular")
                                print(70*"-")
                                print("CONSUMO IDEAL - 6 refeições\n")
                                print(f"Diário de calorias: {consumo_calorias_diario_massa:.2f}kcal")
                                print(f"Diário de proteínas: {consumo_proteinas_diario:.2f}g")
                                print(f"Por refeição de calorias: {quantida_calorias_refeicao_massa:.2f}kcal")
                                print(f"Por refeição de proteínas: {quantidade_proteinas_refeicao:.2f}g")
                                print(70*"-")
                                time.sleep(1)
                                input("Pressione ENTER para continuar")
                                os.system("cls")

                #TABELA NUTRICIONAL
                elif config.escolha_do_menu_usuario_int == 6:
                    print('escolha 06')
                    permanecer_tabela = True
                    while permanecer_tabela:
                        os.system("cls")
                        print(50*"=") #Cabeçario da Tabela
                        print("                TABELA NUTRICIONAL")
                        print(50*"-")
                        print("[1] Consultar alimentos")
                        print("[2] Adicionar alimentos")
                        print("[0] Sair para o menu")
                        print(50*"=")

                        escolha_menu = int(input("Digite o indice correspondente ao que deseja: ")) #Escolhe se quer consultar ou adicionar

                        if escolha_menu == 1: #IF da consulta
                            
                            os.system("cls")
                            time.sleep(1)

                            print(70*"=") #Cabeçario da Tabela
                            print("                TABELA NUTRICIONAL")
                            print(50*"-")

                            for i in range(config.size(config.alimento)): #FOR para apresentar alimentos da Tabela
                                print(f"[{i}]", config.alimento[i])
                            
                            print(50*"-")

                            escolha_alimento = int(input("Digite o indice do alimento para consulta: ")) #Escolhe o alimento para consulta

                            if escolha_alimento in range(config.size(config.alimento)): #IF para puxar dados do alimento escolhido
                                os.system("cls")
                                time.sleep(1)
                                print(70*"=") #Cabeçario da Tabela
                                print("                TABELA NUTRICIONAL")
                                print(50*"-")
                                print(f"Em {config.quantidade_teste[escolha_alimento]}g de {config.alimento[escolha_alimento]}:") #Mostra quantidade da consulta
                                print(50*"-")
                                print(f"Valor energético: {config.valor_energético[escolha_alimento]}kcal") #Mostra calorias da consulta
                                print(f"Carboidratos: {config.carboidratos[escolha_alimento]}g") #Mostra carbboidratos da consulta
                                print(f"Proteinas: {config.proteinas[escolha_alimento]}g") #Mostra proteinas da culta
                                print(f"Sódio: {config.sodio[escolha_alimento]}mg") #Mostra sodio da consulta
                                print(50*"=") 

                                time.sleep(1)
                                input("Pressione ENTER para continuar")

                        elif escolha_menu == 2:
                            os.system("cls")

                            print(50*"=") #Cabeçario da Tabela
                            print("                TABELA NUTRICIONAL")
                            print(50*"-")
                            novo_alimeto = input("Digite o nome do alimento: ") #INPUT para nome do alimento
                            time.sleep(0.5)
                            print(50*"-")
                            quantidade_nova = int(input("Digite a quantidade analisada (em gramas): ")) #INPUT para quantidade de consulta
                            time.sleep(0.5)
                            print(50*"-")
                            valor_novo = float(input("Digite o valor energético (em kcal): ")) #INPUT para calorias
                            time.sleep(0.5)
                            print(50*"-")
                            carboidratos_novo = float(input("Digite a quantidade de carboidratos (em gramas): ")) #INPUT para carboidratos
                            time.sleep(0.5)
                            print(50*"-")
                            proteina_nova = float(input("Digite o quantidade de proteina (em gramas): ")) #INPUT para proteina
                            time.sleep(0.5)
                            print(50*"-")
                            sodio_novo = float(input("Digite o quantidade de sódio (em gramas): ")) #INPUT para sodio
                            time.sleep(1)
                            print(50*"=")

                            os.system("cls")
                            time.sleep(1)
                            print(70*"=") #Cabeçario da Tabela
                            print("                TABELA NUTRICIONAL")
                            print(50*"-")
                            #PRINTs para mostrar os dados do novo alimento antes de adição ao sistema
                            print(f"Em {quantidade_nova}g de {novo_alimeto}:")
                            print(50*"-")
                            print(f"Valor energético: {valor_novo}kcal")
                            print(f"Carboidratos: {carboidratos_novo}g") 
                            print(f"Proteinas: {proteina_nova}g")
                            print(f"Sódio: {sodio_novo}mg")
                            print(50*"=")

                            adicionar = input("Confirmar a adição: Sim ou Não? ").lower().startswith('s') #Confirmação antes de adicionar o alimento
                            if adicionar == True: #IF para adicionar os dados do novo alimento, e retornar ao inicio da tabela
                                config.push(config.alimento, novo_alimeto)
                                config.push(config.quantidade_teste, quantidade_nova)
                                config.push(config.valor_energético, valor_novo)
                                config.push(config.carboidratos, carboidratos_novo)
                                config.push(config.proteinas, proteina_nova)
                                config.push(config.sodio, sodio_novo)
                            
                            else: #ELSE caso não confirme a adição, e ver se usuário deseja permanecer na tabela
                                print(50*"=")
                                input("Pressione ENTER para continuar")
                        
                        elif escolha_menu == 0:
                            voltar = input("[S] para sair do sistema").lower().startswith('s') #Retorna para o menu da Tabela, ou volta ao inicio de tudo
                            if voltar == True:
                                permanecer_tabela = False
                                os.system("cls")

                elif config.escolha_do_menu_usuario_int == 7:
                    print('escolha 07')
                else:
                    print('Numero nao esta listado')
            except ValueError:
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
