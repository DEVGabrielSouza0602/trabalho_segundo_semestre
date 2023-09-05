# TMB
def calcular_tmb(sexo_tmb, peso_tmb, altura_tmb, idade_tmb):
    if sexo == "M":
        tmb = 66 + (13.8 * peso) + (5 * altura) - (6.8 * idade)
    elif sexo == "F":
        tmb = 665 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
    else:
        tmb = ""
    return tmb


# Informações do usuário (podemos mudar depois já que o usuario tem tudo)
sexo = input("Informe o sexo (M para masculino, F para feminino): ").upper()
peso = float(input("Informe o peso em kg: "))
altura = float(input("Informe a altura em cm: ")) / \
    100  # Pra converter os cm em metros
idade = int(input("Informe a idade em anos: "))

tmb = calcular_tmb(sexo, peso, altura, idade)  # Calcular a TMB


if tmb != "":
    print(f"A sua TMB é de aproximadamente {tmb:.2f} calorias por dia.")
else:
    print("Sexo não reconhecido. Use 'M' para masculino ou 'F' para feminino.")
