caloria_total = 1500
calorias_incluidas = [120, 320, 430, 234]
tamanho_da_lista_dos_alimentos_incluidos = len(calorias_incluidas)


def recursividade_calorias(lista_das_calorias, tamanho_da_lista):
    indice=len(calorias_incluidas)

    return caloria_total - recursividade_calorias(calorias_incluidas[indice])


recursividade_calorias(caloria_total,
                       calorias_incluidas, tamanho_da_lista_dos_alimentos_incluidos)

print(caloria_total)
