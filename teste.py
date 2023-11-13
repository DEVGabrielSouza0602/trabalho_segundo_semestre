dicionario_de_treinos = {
    'Segunda': ('Peito', 'Triceps'),
    'Terça': ('Costas', 'Biceps'),
    'Quarta': ('Pernas', 'Panturilha'),
    'Quinta': ('Peito', 'Triceps'),
    'Sexta': ('Ombro', 'Abdomem')
}

indiceDias = []

for dia in dicionario_de_treinos:
    indiceDias.append(dia)

print(indiceDias)

seletor = int(input("Dia desejado: "))

diaSelecionado = indiceDias[seletor]

print(diaSelecionado, dicionario_de_treinos[diaSelecionado])