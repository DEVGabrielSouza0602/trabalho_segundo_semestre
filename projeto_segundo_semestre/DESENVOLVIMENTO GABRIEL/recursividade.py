caloria_total = 0


def recursividade_calorias(contagem_de_calorias, lista):

    if len(lista) < 1:
        return contagem_de_calorias + 1

    return contagem_de_calorias + recursividade_calorias(len(lista)-1)


dicionario_de_alimentos = {
    'alimento a': 120,
    'alimento b': 220,
    'alimento c': 320,
    'alimento d': 420,
    'alimento e': 520,
}

nome_dos_alimentos = dicionario_de_alimentos.keys()
calorias_dos_alimentos = dicionario_de_alimentos.values()


def apresentacao_dos_alimentos(chaves_de_alimentos):
    for posicao, valor in enumerate(chaves_de_alimentos):
        print(f'[{posicao}] = {valor}')


apresentacao_dos_alimentos(nome_dos_alimentos)
alimento = int(input("\nDigite a caloria do seu alimento"))
quantidade_que_comeu = int(input('digite quantas vezes comeu: '))
