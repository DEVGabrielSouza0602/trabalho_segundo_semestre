if dia_digitado in dicionario_de_treinos:
    treinos_do_dia = dicionario_de_treinos[dia_digitado]

    nome_do_arquivo = "treinos_" + dia_digitado + ".txt"

    with open(nome_do_arquivo, 'w') as arquivo:

        for treino in treinos_do_dia:
            arquivo.write(treino + "\n")
    print(
        f"Os treinos do dia {dia_digitado} foram salvos em {nome_do_arquivo}")
else:
    print(f"O dia {dia_digitado} não está no dicionário de treinos.")
