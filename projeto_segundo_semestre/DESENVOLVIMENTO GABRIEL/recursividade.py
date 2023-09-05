dicionario_de_alimentos = {
    'alimento a': 120,
    'alimento b': 220,
    'alimento c': 320,
    'alimento d': 420,
    'alimento e': 520,
}
caloria_total = 0
nome_dos_alimentos = dicionario_de_alimentos.keys()
calorias_dos_alimentos = list(dicionario_de_alimentos.values())
tamanho_da_lista_dos_alimentos = len(nome_dos_alimentos)
contagem_de_alimentos = 0
loop_contagem_de_calorias = True
Alimento_valido = None
calorias_incluidas = []
tamanho_da_lista_dos_alimentos_incluidos = len(calorias_incluidas)


def recursividade_calorias(contagem_de_calorias, lista_das_calorias, tamanho_da_lista):
    if tamanho_da_lista == 1:
        return contagem_de_calorias + lista_das_calorias[tamanho_da_lista]

    return contagem_de_calorias + recursividade_calorias(lista_das_calorias[tamanho_da_lista - 1])


def apresentacao_dos_alimentos(chaves_de_alimentos):
    for posicao, valor in enumerate(chaves_de_alimentos):
        print(f'[{posicao}] = {valor}')


def contador_de_alimentos_funcao(chaves_de_alimentos):
    contador_de_alimentos = -1
    for i in chaves_de_alimentos:
        contador_de_alimentos += 1
    return contador_de_alimentos


'''
DIVISAO DA PAGINA
'''
contagem_de_alimentos = contador_de_alimentos_funcao(
    nome_dos_alimentos)

apresentacao_dos_alimentos(nome_dos_alimentos)
while loop_contagem_de_calorias:

    alimento = input("\nDigite a posição do seu alimento: ")
    try:
        alimento = int(alimento)
        if alimento >= 0:
            if alimento <= contagem_de_alimentos:
                Alimento_valido = True
            else:
                print('Alimento não esta na sua dieta...')
        else:
            print('Digite um alimento valido...')
    except ValueError:
        print('Digite um numero...')

    if Alimento_valido is True:
        if alimento <= contagem_de_alimentos:
            calorias_incluidas.append(calorias_dos_alimentos[alimento])
            print(calorias_dos_alimentos[alimento])

            print(calorias_incluidas)

    sair_da_inclusao_de_alimento = input(
        'Deseja para de incluir: [s]').lower().startswith('s')
    if sair_da_inclusao_de_alimento is True:
        loop_contagem_de_calorias = False

recursividade_calorias(caloria_total, calorias_incluidas,
                       tamanho_da_lista_dos_alimentos_incluidos)
