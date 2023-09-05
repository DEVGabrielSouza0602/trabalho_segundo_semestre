'''Quant de agua a tomar'''
Peso = float(input("Insira seu peso em Kg: "))
# 35 é a quantidade de Ml que precisa por peso (isso é uma média)
quant_agua = Peso * 35
print(f'Você precisa tomar cerca de {quant_agua: .2f}Ml de água por dia')
