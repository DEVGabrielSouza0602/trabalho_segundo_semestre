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

gasto_energetico = 2000 * frequencia
consumo_proteinas_diario = 70 * 3
consumo_calorias_diario_massa = gasto_energetico + 750
consumo_calorias_diario_emagrecimento = gasto_energetico - 500
quantidade_proteinas_refeicao = consumo_proteinas_diario/6
quantida_calorias_refeicao_emagrecimento = consumo_calorias_diario_emagrecimento/6
quantida_calorias_refeicao_massa = consumo_calorias_diario_massa/6

os.system("cls")
print(70*"=") #Cabeçario das Dietas
print("                          DIETAS BÁSICAS")
print(70*"=")
print("[1] Emagrecer")
print("[2] Ganhar massa muscular")
print(70*"-")
escolha_dieta = input("Digite o indice para escolher a dieta: ")
os.system("cls")
    
if escolha_dieta == 1:
    print(70*"=") #Cabeçario das Dietas
    print("                          DIETAS BÁSICAS")
    print(70*"=")
    print("OBJETIVO: Emagrecer")
    print(70*"-")
    print(f"Consumo diário de calorias: {consumo_calorias_diario_emagrecimento}kcal")
    print(f"Consumo diário de proteínas: {consumo_proteinas_diario}g")
    print(70*"-")
    print(f"Consumo estimado por refeição de calorias: {quantida_calorias_refeicao_emagrecimento}kcal")
    print(f"Consumo estimado por refeição de proteínas: {quantidade_proteinas_refeicao}g")

