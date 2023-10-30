if dia_digitado in dicionario_de_treinos:
    treinos_do_dia = dicionario_de_treinos[dia_digitado]

    # Nome do arquivo onde você deseja salvar os treinos
    nome_do_arquivo = "treinos_" + dia_digitado + ".txt"

    # Abrir o arquivo em modo de escrita ('w' para escrita)
    with open(nome_do_arquivo, 'w') as arquivo:
        # Escrever os treinos no arquivo
        for treino in treinos_do_dia:
            arquivo.write(treino + "\n")
    print(
        f"Os treinos do dia {dia_digitado} foram salvos em {nome_do_arquivo}")
else:
    print(f"O dia {dia_digitado} não está no dicionário de treinos.")
