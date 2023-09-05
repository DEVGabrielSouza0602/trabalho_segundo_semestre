caloria_total = 0
calorias_incluidas = [120, 320, 430, 234]
tamanho_da_lista_dos_alimentos_incluidos = len(calorias_incluidas)


def recursividade_calorias(lista_das_calorias, tamanho_da_lista):
    if tamanho_da_lista <= 1:
        return (caloria_total + lista_das_calorias[tamanho_da_lista])

    def atribuicao_de_calorias(caloria_total):
        return (caloria_total + lista_das_calorias[tamanho_da_lista])

    return recursividade_calorias(lista_das_calorias, tamanho_da_lista - 1)


recursividade_calorias(caloria_total,
                       calorias_incluidas, tamanho_da_lista_dos_alimentos_incluidos)

print(caloria_total)
