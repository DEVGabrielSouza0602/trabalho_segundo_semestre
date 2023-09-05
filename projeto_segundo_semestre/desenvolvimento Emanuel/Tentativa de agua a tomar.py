'''Quant de agua a tomar'''


def calcular_quantidade_agua(peso, formula="padrao"):
    if formula == "padrao":
        return peso * 30
    elif formula == "atleta":
        return peso * 40
    elif formula == "personalizado":
        personalizacao = float(
            input("Informe a quantidade personalizada de água (ml/kg): "))
        return peso * personalizacao
    else:
        return ("Fórmula de cálculo não reconhecida")


peso = float(input("Informe o seu peso em Kg: "))

# escolher uma fórmula de cálculo
print("Escolha a fórmula mais adequada para o cálculo:")
print("1 - Fórmula padrão (30 ml/kg)")
print("2 - Fórmula para atletas (40 ml/kg)")
print("3 - Fórmula personalizada")
formula_escolhida = int(input("Digite o número da opção desejada: "))

# calcula a quantidade recomendada de água com base na escolha da fórmula
if formula_escolhida == 1:
    quantidade_agua_ml = calcular_quantidade_agua(peso, "padrao")
elif formula_escolhida == 2:
    quantidade_agua_ml = calcular_quantidade_agua(peso, "atleta")
elif formula_escolhida == 3:
    quantidade_agua_ml = calcular_quantidade_agua(peso, "personalizado")
else:
    print("Opção inválida.")
    quantidade_agua_ml = 0

if quantidade_agua_ml > 0:
    print(
        f"Você deve tomar aproximadamente {quantidade_agua_ml:.2f} ml de água por dia.")
