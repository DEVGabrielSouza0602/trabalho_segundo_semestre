import dicas
import config
import time
import os

import Alimentos
from Alimentos import Carnes, Frutas, Graos, Liquidos, Verduras
from Alimentos import Frango, ArrozBranco, FeijãoPreto,BatataDoce, Banana, Maça, Leite

controle_principal = True

while controle_principal:
    print(70*"=")  # Cabeçario Tela de Login
    print("                     TELA DE LOGIN DO USUÁRIO")
    print(70*"-")
    usuario_inserido = input('Digite o seu Usuario: ').capitalize()
    senha_inserida = input('Digite a sua senha: ')
    print(70*"-")
    if usuario_inserido in config.usuarios_permitidos['Usuarios']:
        if senha_inserida in config.usuarios_permitidos['Senhas']:
            config.login_usuario_comum_efetuado = True
    elif usuario_inserido == config.login_usuario_master and senha_inserida == config.senha_usuario_master:
        config.login_usuario_master_efetuado = True
    else:
        print('Usuario ou senha incorreto.')
        config.limpeza_e_time(3)

    while config.login_usuario_comum_efetuado:
        config.loop_ficha_de_treino = True
        config.limpeza_e_time(1)
        print(70*"=")  # Cabeçario Login efetuado
        print("                      LOGIN FEITO COM SUCESSO")
        print(70*"=")
        print(f'OLÁ {usuario_inserido}, seja bem vindo!')
        config.limpeza_e_time(3)
        print(70*"=")  # Cabeçario de solicitação de informações
        print("                       INFORMAÇÕES CADASTRAIS")
        print(70*"-")
        print("Qual o seu sexo: ")
        sexo_do_usuario = input("(M) Masculino ou (F) para feminino: ").upper()
        nome_do_usuario = input('Digite seu nome: ')
        idade_do_usuario = int(input('Digite sua idade: '))
        peso_do_usuario = float(input('Digite seu peso: '))
        altura_do_usuario = int(input('Digite sua altura: '))
        print(70*"=")

        print('Armazenado seus dados, só um momento...')
        print(70*"=")
        config.limpeza_e_time(3)
        config.usuario_e_seus_dados['Nome'] = nome_do_usuario
        config.usuario_e_seus_dados['Idade'] = idade_do_usuario
        config.usuario_e_seus_dados['Peso'] = peso_do_usuario
        config.usuario_e_seus_dados['Altura'] = altura_do_usuario
        config.usuario_e_seus_dados['sexo'] = sexo_do_usuario
        peso = float(peso_do_usuario)
        altura = altura_do_usuario / 100  # Pra converter os cm em metros
        idade = idade_do_usuario
        tmb = config.calcular_tmb(sexo_do_usuario, peso, altura, idade)
        config.loop_menu_usuario_comum = True

#MENU INICIAL ------------------------------------------------------------------------------------------------------
        while config.loop_menu_usuario_comum:
            print(70*"=")  # Cabeçario do Menu Inicial
            print("                             MENU INICIAL")
            print(70*"-")
            print('[1] Dicas de academia')
            print('[2] Ficha de treino')
            print('[3] Taxa De Metabolismo Basal')
            print('[4] Quantidade de Agua diario')
            print('[5] Dieta Basica')

            print('[6] Tabela Nutricional')
            print('[0] Deslogar')
            print(70*"=")
            config.escolha_do_menu_usuario = input(  # INPUT para escolha do item do menu
                'Qual sua escolha de acordo com os indices: ')
            try:
                config.escolha_do_menu_usuario_int = int(
                    config.escolha_do_menu_usuario)
                if config.escolha_do_menu_usuario_int == 0:
                    config.limpeza_e_time(2)
                    print(70*"=")
                    print("        OBRIGADO PELA PREFERÊNCIA, ATÉ LOGO! ", {
                          nome_do_usuario})
                    print(70*"-")
                    print('Desconectando do sistema...')
                    print(70*"=")
                    config.limpeza_e_time(3)
                    config.loop_menu_usuario_comum = False
                    config.login_usuario_comum_efetuado = False
                elif config.escolha_do_menu_usuario_int == 1:
                    config.loop_dicas_De_treino = True
                    config.limpeza_e_time(2)
                    while config.loop_dicas_De_treino:
                        for i in config.dicas_de_treino:
                            print(70*"=")
                            print('                         SISTEMA DE DICAS:')
                            print(70*"-")
                            time.sleep(1)
                            print(i)
                            time.sleep(2)
                            print(70*"=")
                            print('Pressione [ENTER] para proxima dica...')
                            pular_ou_sair = input(
                                '[S] para sair do sistema... ').lower().startswith('s')
                            time.sleep(1)
                            os.system('cls')
                            if pular_ou_sair is True:
                                config.loop_dicas_De_treino = False
                                break

#FICHA DE TREINO ------------------------------------------------------------------------------------------------------
                elif config.escolha_do_menu_usuario_int == 2:
                    config.loop_ficha_de_treino = True
                    while config.loop_ficha_de_treino:
                        time.sleep(2)
                        os.system('cls')
                        print(70*"=")
                        print('                       FICHA DE TREINO!')
                        print(70*"-")
                        config.apresentacao_dos_dias_da_semana(
                            config.dias_da_semana_ficha_de_treino)
                        print(70*"=")

                        dia_digitado = input(
                            'Digite o indice do dia para treino: ')

                        try:
                            dia_digitado = int(dia_digitado)
                            if dia_digitado < 0 or dia_digitado > 4:
                                print(70*"-")
                                print('Dia não disponivel para treino..')
                                time.sleep(1.5)
                                os.system('cls')
                            else:
                                print(70*"-")
                                print('Dia disponivel para treino..')
                                time.sleep(1.5)
                                os.system('cls')
                                config.dia_digitado_corretamente = True
                        except ValueError:
                            print(70*"-")
                            print('Insira apenas numeros...')
                            time.sleep(1.5)
                            os.system('cls')

                        for numero, nome in enumerate(config.dias_da_semana_ficha_de_treino):
                            if numero == dia_digitado:
                                dia = nome
                                if nome in config.dicionario_de_treinos.keys():
                                    print(70*"=")
                                    print('                     FICHA DE TREINO!')
                                    print(70*"-")
                                    for i in config.dicionario_de_treinos[nome]:
                                        print(i, end=" | ")
                                        time.sleep(1)

                        print("\n", 69*"=")
                        print('\n[1]Deseja sair')

                        sair_sistema_de_treino = input(
                            '[3]Deseja ver outro treino [ENTER] ').lower().startswith('1')
                        time.sleep(1)
                        os.system('cls')

                        imprimir_ficha = input(
                            '\n[2]Deseja imprimir o texto').lower().startswith('2')
                        time.sleep(1)
                        os.system('cls')

                        if sair_sistema_de_treino == True:
                            config.loop_ficha_de_treino = False
                        elif imprimir_ficha == True:
                            config.loop_ficha_de_treino = False

                elif config.escolha_do_menu_usuario_int == 3: #Taxa de Metabolismo Basal
                    config.limpeza_e_time(2)
                    os.system('cls')
                    print(70*"=")
                    print("                     TAXA DE METABOLISMO BASAL")
                    print(70*"-")
                    if tmb != "":
                        print(
                            f"A sua TMB é de aproximadamente {tmb:.2f} calorias por dia.")
                        print(70*"=")
                    else:
                        print(
                            "Sexo não reconhecido. Use 'M' para masculino ou 'F' para feminino.")
                        print(70*"=")
                    input("Pressione ENTER para continuar")
                    os.system("cls")
                elif config.escolha_do_menu_usuario_int == 4:
                    config.limpeza_e_time(2)
                    looping_quantidade_agua = True
                    while looping_quantidade_agua:
                        peso = float(peso_do_usuario)
                        # escolha a fórmula mais adequada para fazer o cálculo
                        print(70*"=")
                        print("                  CÁLCULO DE ÁGUA")
                        print(70*"-")
                        print("Escolha a fórmula de cálculo:")
                        print("1 - Fórmula padrão (30 ml/kg)")
                        print("2 - Fórmula para atletas (40 ml/kg)")
                        print("3 - Fórmula personalizada")
                        print(70*"=")
                        opcao = int(
                            input("Digite o número da opção desejada: "))

                        # calcula a quantidade recomendada de água com base na escolha do usuário
                        config.limpeza_e_time(2)
                        print(70*"=")
                        print("                  CÁLCULO DE ÁGUA")
                        print(70*"-")

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
                                f"\nVocê deve tomar aproximadamente {quantidade_agua_ml:.2f} ml de água por dia.")
                            print(70*"=")
                        print('\nDeseja sair [s]')
                        sair_sistema_de_agua = input(
                            'Para fazer outro cálculo pressione [ENTER] ').lower().startswith('s')
                        time.sleep(1)
                        os.system('cls')
                        if sair_sistema_de_agua is True:
                            looping_quantidade_agua = False

#DIETA ------------------------------------------------------------------------------------------------------
                elif config.escolha_do_menu_usuario_int == 5:

                    permanecer_na_dieta = True
                    config.limpeza_e_time(2)

                    while permanecer_na_dieta:
                        print(70*"=")  # Cabeçario das Dietas
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
                        escolha_frequencia = int(
                            input("Digite o indice de acordo com a frequência que você se exercita: "))

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
                            os.system("cls")

                        if escolha_frequencia != 0:

                            gasto_energetico = round(tmb * frequencia, 2)
                            consumo_proteinas_diario = round(
                                peso_do_usuario * 3, 2)
                            consumo_calorias_diario_massa = round(
                                gasto_energetico + 600, 2)
                            consumo_calorias_diario_emagrecimento = round(
                                gasto_energetico - 300, 2)
                            quantidade_proteinas_refeicao = round(
                                consumo_proteinas_diario/6, 2)
                            quantida_calorias_refeicao_emagrecimento = round(
                                consumo_calorias_diario_emagrecimento/6, 2)
                            quantida_calorias_refeicao_massa = round(
                                consumo_calorias_diario_massa/6, 2)

                            os.system("cls")
                            print(70*"=")  # Cabeçario das Dietas
                            print("                          DIETAS BÁSICAS")
                            print(70*"=")
                            print("[1] Emagrecer")
                            print("[2] Ganhar massa muscular")
                            print(70*"-")
                            escolha_dieta = int(
                                input("Digite o indice para escolher a dieta: "))
                            os.system("cls")

                            if escolha_dieta == 1:
                                print(70*"=")  # Cabeçario das Dietas
                                print("                          DIETAS BÁSICAS")
                                print(70*"=")
                                print("OBJETIVO: Emagrecer")
                                print(70*"-")
                                print("CONSUMO IDEAL- 6 refeições\n")
                                print(
                                    f"Diário de calorias: {consumo_calorias_diario_emagrecimento}kcal")
                                print(
                                    f"Diário de proteínas: {consumo_proteinas_diario}g")
                                print(
                                    f"Por refeição de calorias: {quantida_calorias_refeicao_emagrecimento}kcal")
                                print(
                                    f"Por refeição de proteínas: {quantidade_proteinas_refeicao}g")
                                print(70*"-")
                                time.sleep(1)
                                input("Pressione ENTER para continuar")
                                os.system("cls")

                            if escolha_dieta == 2:
                                print(70*"=")  # Cabeçario das Dietas
                                print("                          DIETAS BÁSICAS")
                                print(70*"=")
                                print("OBJETIVO: ganhar massa muscular")
                                print(70*"-")
                                print("CONSUMO IDEAL - 6 refeições\n")
                                print(
                                    f"Diário de calorias: {consumo_calorias_diario_massa:.2f}kcal")
                                print(
                                    f"Diário de proteínas: {consumo_proteinas_diario:.2f}g")
                                print(
                                    f"Por refeição de calorias: {quantida_calorias_refeicao_massa:.2f}kcal")
                                print(
                                    f"Por refeição de proteínas: {quantidade_proteinas_refeicao:.2f}g")
                                print(70*"-")
                                time.sleep(1)
                                input("Pressione ENTER para continuar")
                                os.system("cls")

                #TABELA NUTRICIONAL
                elif config.escolha_do_menu_usuario_int == 6:

                    permanecer_tabela = True

                    while permanecer_tabela:

                        os.system("cls")
                        print(50*"=") #Cabeçario da Tabela
                        print("                TABELA NUTRICIONAL")
                        print(50*"-")
                        print("[1] Consultar alimentos")
                        print("[0] Sair para o menu")
                        print(50*"=")

                        escolha_menu = int(input("Digite o indice correspondente ao que deseja: ")) #Escolhe se quer consultar ou adicionar

                        if escolha_menu == 1: #IF da consulta
                            os.system("cls")
                            time.sleep(1)

                            print(70*"=") #Cabeçario da Tabela
                            print("                TABELA NUTRICIONAL")
                            print(50*"-")
                            for i in range(len(Alimentos.listaNomesAlimentos)): #FOR para apresentar alimentos da Tabela
                                print(f"[{i}]", Alimentos.listaNomesAlimentos[i])  
                            print(50*"-")
                            escolha_alimento = int(input("Digite o indice do alimento para consulta: ")) #Escolhe o alimento para consulta
                            
                            if escolha_alimento in range(len(Alimentos.listaNomesAlimentos)): #IF para puxar dados do alimento escolhido
                                os.system("cls")
                                time.sleep(1)
                                print(70*"=") #Cabeçario da Tabela
                                print("                TABELA NUTRICIONAL")
                                print(70*"-")
                                alimento_selecionado = Alimentos.listaNomesAlimentos[escolha_alimento]
                                eval(alimento_selecionado).descreverAlimento() #EVAL para tranforma str em nome de variavel e descreve-lo 
                                print(70*"=")
                                time.sleep(1)
                                input("Pressione ENTER para continuar")
                        
                        elif escolha_menu == 0:
                            voltar = input("[S] para sair do sistema ").lower().startswith('s') #Retorna para o menu da Tabela, ou volta ao inicio de tudo
                            if voltar == True:
                                os.system("cls")
                                permanecer_tabela = False
                        
                        

                elif config.escolha_do_menu_usuario_int == 7:
                    print('escolha 07')
                else:
                    print('Numero nao esta listado')
                    config.limpeza_e_time(2)
            except ValueError:
                print('Digite um numero disponivel !!!')
                config.limpeza_e_time(2)

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
