import os
import time
import config

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

os.system("cls")

print(70*"=") #Cabeçario das Dietas
print("                          DIETAS BÁSICAS")
print(70*"=")
print("[1] Emagrecer")
print("[2] Ganhar de massa muscular")
print(70*"-")
