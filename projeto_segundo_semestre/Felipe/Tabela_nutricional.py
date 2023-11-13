import os
import time

def verificar_vazio(lista):
    return len(lista) == 0

def push(lista, item):
    lista.append(item)

def size(lista):
    return len(lista)

alimento = ['Frango', 'Arroz branco', 'Feijão preto', 'Batata doce', 'Banana','Maça', 'Pão integral']
quantidade_teste = [100, 100, 100, 100, 100, 100, 100]
valor_energético = [139, 130, 76, 100 ,89, 52, 247]
carboidratos = [0.3, 28.2, 14, 24, 23, 14, 41]
proteinas = [26, 2.7, 4.3, 2, 1.1, 0.3, 13]
sodio = [153, 1, 99 , 36, 1, 1, 400]

permanecer_tabela = True

while permanecer_tabela:

    os.system("cls")
    print(50*"=") #Cabeçario da Tabela
    print("                TABELA NUTRICIONAL")
    print(50*"-")
    print("[1] Consultar alimentos")
    print("[2] Adicionar alimentos (apenas usuários master)")
    print("[0] Sair para o menu")
    print(50*"=")

    escolha_menu = int(input("Digite o indice correspondente ao que deseja: ")) #Escolhe se quer consultar ou adicionar


    if escolha_menu == 1: #IF da consulta
        
        os.system("cls")
        time.sleep(1)

        print(70*"=") #Cabeçario da Tabela
        print("                TABELA NUTRICIONAL")
        print(50*"-")

        for i in range(size(alimento)): #FOR para apresentar alimentos da Tabela
            print(f"[{i}]", alimento[i])
        
        print(50*"-")

        escolha_alimento = int(input("Digite o indice do alimento para consulta: ")) #Escolhe o alimento para consulta

        if escolha_alimento in range(size(alimento)): #IF para puxar dados do alimento escolhido
            os.system("cls")
            time.sleep(1)
            print(70*"=") #Cabeçario da Tabela
            print("                TABELA NUTRICIONAL")
            print(50*"-")
            print(f"Em {quantidade_teste[escolha_alimento]}g de {alimento[escolha_alimento]}:") #Mostra quantidade da consulta
            print(50*"-")
            print(f"Valor energético: {valor_energético[escolha_alimento]}kcal") #Mostra calorias da consulta
            print(f"Carboidratos: {carboidratos[escolha_alimento]}g") #Mostra carbboidratos da consulta
            print(f"Proteinas: {proteinas[escolha_alimento]}g") #Mostra proteinas da culta
            print(f"Sódio: {sodio[escolha_alimento]}mg") #Mostra sodio da consulta
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

        adicionar = input(f"Confirmar a adição: Sim ou Não? ").lower().startswith('s') #Confirmação antes de adicionar o alimento
        if adicionar == True: #IF para adicionar os dados do novo alimento, e retornar ao inicio da tabela
            push(alimento, novo_alimeto)
            push(quantidade_teste, quantidade_nova)
            push(valor_energético, valor_novo)
            push(carboidratos, carboidratos_novo)
            push(proteinas, proteina_nova)
            push(sodio, sodio_novo)
        
        else: #ELSE caso não confirme a adição, e ver se usuário deseja permanecer na tabela
            os.system("cls")
            time.sleep(1)
            print(50*"=")
            input("Pressione ENTER para continuar")
    
    elif escolha_menu == 0:
        voltar = input("[[S] para sair do sistema ").lower().startswith('s') #Retorna para o menu da Tabela, ou volta ao inicio de tudo
        if voltar == True:
            permanecer_tabela = False