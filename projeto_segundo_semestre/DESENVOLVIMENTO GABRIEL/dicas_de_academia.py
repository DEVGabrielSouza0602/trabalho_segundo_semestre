import os
import time

dicas_de_treino = ['abc', 'fed', 'ghi']
loop_dicas_De_treino = True

while loop_dicas_De_treino:
    for i in dicas_de_treino:
        print('SISTEMA DE DICAS:'
              )
        time.sleep(1)
        print(i)
        time.sleep(2)
        print('Pressione [ENTER] para proxima dica...')
        pular_ou_sair = input(
            '[S] para sair do sistema... ').lower().startswith('s')
        time.sleep(1)
        os.system('cls')
        if pular_ou_sair is True:
            loop_dicas_De_treino = False
            break
