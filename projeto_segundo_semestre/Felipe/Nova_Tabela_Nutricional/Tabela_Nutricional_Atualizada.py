from Carnes import Carnes
from Frutas import Frutas
from Graos import Graos
from Liquidos import Liquidos
from Verduras import Verduras

import os
import time

#CRIANDO OS ALIMENTOS
Frango = Carnes("Frango", 100, 159, 0, 32, 0, 50)
ArrozBranco = Graos("ArrozBranco", 100, 32, 7.03, 0.63, 0.40, 0.25)
FeijãoPreto = Graos("FeijãoPreto", 100, 77, 14, 4.5, 8.4, 1.9)
BatataDoce = Verduras("BatataDoce", 100, 53.90, 12.88, 0.42, 2.10)
Banana = Frutas("Banana", 100, 39.60, 10.32, 0.52, 0)
Maça = Frutas("Maça", 100, 67.60, 17.95, 0.34, 1.30)

#LISTA PARA ARMAZENAR OS NOMES DOS ALIMENTOS
listaNomesAlimentos = []
listaNomesAlimentos.append(Frango._nome)
listaNomesAlimentos.append(ArrozBranco._nome)
listaNomesAlimentos.append(FeijãoPreto._nome)
listaNomesAlimentos.append(BatataDoce._nome)
listaNomesAlimentos.append(Banana._nome)
listaNomesAlimentos.append(Maça._nome)

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
        escolha_alimento = int(input("Digite o indice do alimento para consulta: ")) #Escolhe o alimento para consulta
        
        if escolha_alimento in range(len(listaNomesAlimentos)): #IF para puxar dados do alimento escolhido
            os.system("cls")
            time.sleep(1)
            print(70*"=") #Cabeçario da Tabela
            print("                TABELA NUTRICIONAL")
            print(70*"-")
            alimento_selecionado = listaNomesAlimentos[escolha_alimento]
            eval(alimento_selecionado).descreverAlimento() #EVAL para tranforma str em nome de variavel e descreve-lo 
            print(70*"=")
            time.sleep(1)
            input("Pressione ENTER para continuar")


    elif escolha_menu == 2:
        print()
    
    elif escolha_menu == 0:
        voltar = input("[[S] para sair do sistema ").lower().startswith('s') #Retorna para o menu da Tabela, ou volta ao inicio de tudo
        if voltar == True:
            permanecer_tabela = False