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


def recursividade_calorias(contagem_de_calorias, lista):

    return contagem_de_calorias + recursividade_calorias(len(lista)-1)


def apresentacao_dos_alimentos(chaves_de_alimentos):
    for posicao, valor in enumerate(chaves_de_alimentos):
        print(f'[{posicao}] = {valor}')


def contador_de_alimentos_funcao(chaves_de_alimentos, contador_de_alimentos):
    for i in chaves_de_alimentos:
        contador_de_alimentos += 1


contagem_de_alimentos = contador_de_alimentos_funcao(
    nome_dos_alimentos, contagem_de_alimentos)

apresentacao_dos_alimentos(nome_dos_alimentos)

alimento = int(input("\nDigite a posição do seu alimento: "))
if alimento <= contagem_de_alimentos:
    print(calorias_dos_alimentos[alimento])
else:
    print('O alimento não esta incluso a sua dieta.')
