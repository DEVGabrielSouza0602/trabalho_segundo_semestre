import os
import time

def verificar_vazio(lista):
    return len(lista) == 0


def push(lista, item):
    lista.append(item)

def size(lista):
    return len(lista)


alimento = ['a', 'b', 'c', 'd', 'e',]
quantidade_teste = [1, 2, 3, 4, 5]
valor_energético = [10, 20, 30, 40 ,50]
carboidratos = [5, 10, 15, 20, 25]
proteinas = [3, 6, 9, 12, 15]
sodio = [10, 20, 30 ,40 ,50]

permanecer_tabela = True

while permanecer_tabela:

    os.system("cls")
    print(50*"=")
    print("                TABELA NUTRICIONAL")
    print(50*"-")
    print("[0] Consultar alimentos")
    print("[1] Adicionar alimentos (apenas usuários master)")
    print(50*"=")

    escolha_menu = int(input("Digite o indice correspondente ao que deseja: "))


    if escolha_menu == 0:
        
        os.system("cls")
        time.sleep(1)

        for i in range(size(alimento)):
            print(f"[{i}]", alimento[i])

        escolha_alimento = int(input("Digite o indice do alimento para consulta: "))

        if escolha_alimento in range(size(alimento)):
            os.system("cls")
            time.sleep(1)
            print(70*"=")
            print("                TABELA NUTRICIONAL")
            print(50*"-")
            print(f"Em {quantidade_teste[escolha_alimento]}g de", alimento[escolha_alimento], "existe:")
            print(50*"-")
            print(f"Valor energético: {valor_energético[escolha_alimento]}kcal")
            print(f"Carboidratos: {carboidratos[escolha_alimento]}g") 
            print(f"Proteinas: {proteinas[escolha_alimento]}g")
            print(f"Sódio: {sodio[escolha_alimento]}g")
            print(50*"=")

            time.sleep(1)
            voltar = input("Deseja permanecer em Tabela Nutricional? Sim ou Não? ").lower().startswith('n')
            if voltar == True:
                permanecer_tabela = False

    elif escolha_menu == 1:
        os.system("cls")

        print(50*"=")
        print("                TABELA NUTRICIONAL")
        print(50*"-")
        novo_alimeto = input("Digite o nome do alimento: ")
        time.sleep(0.5)
        print(50*"-")
        quantidade_nova = int(input("Digite a quantidade analisada (em gramas): "))
        time.sleep(0.5)
        print(50*"-")
        valor_novo = float(input("Digite o valor energético (em kcal): "))
        time.sleep(0.5)
        print(50*"-")
        carboidratos_novo = float(input("Digite a quantidade de carboidratos (em gramas): "))
        time.sleep(0.5)
        print(50*"-")
        proteina_nova = float(input("Digite o quantidade de proteina (em gramas): "))
        time.sleep(0.5)
        print(50*"-")
        sodio_novo = float(input("Digite o quantidade de sódio (em gramas): "))
        time.sleep(1)

        push(alimento, novo_alimeto)
        push(quantidade_teste, quantidade_nova)
        push(valor_energético, valor_novo)
        push(carboidratos, carboidratos_novo)
        push(proteinas, proteina_nova)
        push(sodio, sodio_novo)
        
        print(50*"=")
        voltar = input("Deseja permanecer em Tabela Nutricional? Sim ou Não? ").lower().startswith('n')
        if voltar == True:
            permanecer_tabela = False