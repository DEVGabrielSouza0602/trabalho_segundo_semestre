import os
import time

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
print(70*"-")
escolha = int(input("Digite o indice de acordo com a frequência que você se exercita: "))

if escolha == 1:
    frequencia = 1.2
elif escolha == 2:
    frequencia = 1.375
elif escolha == 3:
    frequencia = 1.55
elif escolha == 4:
    frequencia = 1.725
elif escolha == 5:
    frequencia = 1.9

