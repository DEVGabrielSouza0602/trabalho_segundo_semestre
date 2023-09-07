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
fibras = [1, 2, 3, 4, 5]
sodio = [10, 20, 30 ,40 ,50]

print("[0] Consultar alimentos")
print("[1] Adicionar alimentos (apenas usuário master)")

escolha_menu = int(input("Digite o indice correspondente ao que deseja: "))



for i in range(size(alimento)):
    print(f"[{i}]", alimento[i])


escolha_alimento = int(input("Digite o indice do alimento para consulta: "))

if escolha_alimento in range(size(alimento)):
    print(quantidade_teste[escolha_alimento])
    print(valor_energético[escolha_alimento])
    print(carboidratos[escolha_alimento])
    print(proteinas[escolha_alimento])
    print(fibras[escolha_alimento])
    print(sodio[escolha_alimento])

