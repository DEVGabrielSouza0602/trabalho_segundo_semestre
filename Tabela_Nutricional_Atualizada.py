from Carnes import Carnes
from Frutas import Frutas
from Graos import Graos
from Liquidos import Liquidos
from Verduras import Verduras

import os
import time

Frango = Carnes("Frango", 100, 159, 0, 32, 0, 50)
ArrozBranco = Graos("ArrozBranco", 100, 32, 7.03, 0.63, 0.40, 0.25)
FeijãoPreto = Graos("FeijãoPreto", 100, 77, 14, 4.5, 8.4, 1.9)
BatataDoce = Verduras("BatataDoce", 100, 53.90, 12.88, 0.42, 2.10)
Banana = Frutas("Banana", 100, 39.60, 10.32, 0.52, 0)
Maça = Frutas("Maça", 100, 67.60, 17.95, 0.34, 1.30)


listaAlimentos = []
listaNomesAlimentos = []

listaAlimentos.append(Frango)
listaAlimentos.append(ArrozBranco)
listaAlimentos.append(FeijãoPreto)
listaAlimentos.append(BatataDoce)
listaAlimentos.append(Banana)
listaAlimentos.append(Maça)

listaNomesAlimentos.append("Frango")
listaNomesAlimentos.append("ArrozBranco")
listaNomesAlimentos.append("FeijãoPreto")
listaNomesAlimentos.append("BatataDoce")
listaNomesAlimentos.append("Banana")
listaNomesAlimentos.append("Maça")

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
        for i in range(len(listaNomesAlimentos)): #FOR para apresentar alimentos da Tabela
            print(f"[{i}]", listaNomesAlimentos[i])  
        print(50*"-")
        escolha_alimento = int(input("Digite o nome do alimento para consulta: ")) #Escolhe o alimento para consulta
        
        if escolha_alimento in range(len(listaAlimentos)): #IF para puxar dados do alimento escolhido
            os.system("cls")
            time.sleep(1)
            print(70*"=") #Cabeçario da Tabela
            print("                TABELA NUTRICIONAL")
            print(70*"-")
            alimento_selecionado = listaNomesAlimentos[escolha_alimento]
            eval(alimento_selecionado).descreverAlimento() 
            print(70*"=")
            time.sleep(1)
            input("Pressione ENTER para continuar")








    elif escolha_menu == 2:
        os.system("cls")

        print(50*"=") #Cabeçario da Tabela
        print("                TABELA NUTRICIONAL")
        print(50*"-")
        tipo_alimento = input("Digite o tipo do alimento: ") #INPUT para nome do alimento
        time.sleep(0.5)
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
        print(70*"-")
        #PRINTs para mostrar os dados do novo alimento antes de adição ao sistema
        print(f"Tipo: {tipo_alimento}")
        print(f"Em {quantidade_nova}g de {novo_alimeto}:")
        print(70*"-")
        print(f"Valor energético: {valor_novo}kcal")
        print(f"Carboidratos: {carboidratos_novo}g") 
        print(f"Proteinas: {proteina_nova}g")
        print(f"Sódio: {sodio_novo}mg")
        print(70*"=")

        adicionar = input(f"Confirmar a adição: Sim ou Não? ").lower().startswith('s') #Confirmação antes de adicionar o alimento
        if adicionar == True: #IF para adicionar os dados do novo alimento, e retornar ao inicio da tabela
            
        
        else: #ELSE caso não confirme a adição, e ver se usuário deseja permanecer na tabela
            os.system("cls")
            time.sleep(1)
            print(50*"=")
            input("Pressione ENTER para continuar")
    
    elif escolha_menu == 0:
        voltar = input("[[S] para sair do sistema ").lower().startswith('s') #Retorna para o menu da Tabela, ou volta ao inicio de tudo
        if voltar == True:
            permanecer_tabela = False
            