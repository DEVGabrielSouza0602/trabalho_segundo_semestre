import os
import time
dicionario_de_treinos = {
    'Segunda': ('a', 'b', 'c'),
    'Terça': ('e', '2', '3'),
    'Quarta': ('b', '5', 'f'),
    'Quinta': ('8', 'o', 'v'),
    'Sexta': ('1', '0', 's')
}


def apresentacao_dos_dias_da_semana(chaves_de_treinos):
    for numero, nome in enumerate(chaves_de_treinos):
        print(f'| [{numero}] {nome} ')
        time.sleep(0.5)


loop_ficha_de_treino = True
dias_da_semana_ficha_de_treino = dicionario_de_treinos.keys()
dia_digitado_corretamente = None

'''
------------------------
'''

while loop_ficha_de_treino:
    print('Seja bem vindo a sua ficha de treino')
    apresentacao_dos_dias_da_semana(dias_da_semana_ficha_de_treino)

    dia_digitado = input('Digite o numero do dia para treino: ')

    try:
        dia_digitado = int(dia_digitado)
        if dia_digitado < 0 or dia_digitado > 4:
            print('Dia não disponivel para treino..')
            time.sleep(1.5)
            os.system('cls')
        else:
            print('Dia disponivel para treino..')
            time.sleep(1.5)
            os.system('cls')
            dia_digitado_corretamente = True
    except ValueError:
        print('Insira apenas numeros...')
        time.sleep(1.5)
        os.system('cls')

    for numero, nome in enumerate(dias_da_semana_ficha_de_treino):
        if numero == dia_digitado:
            dia = nome
            if nome in dicionario_de_treinos.keys():
                for i in dicionario_de_treinos[nome]:
                    print(i, end=" | ")
                    time.sleep(1)

    print('\nDeseja sair [s]')
    sair_sistema_de_treino = input(
        'Deseja ver outro treino [ENTER] ').lower().startswith('s')
    time.sleep(1)
    os.system('cls')
    if sair_sistema_de_treino is True:
        loop_ficha_de_treino = False
