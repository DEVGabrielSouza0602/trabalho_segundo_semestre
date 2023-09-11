alimento = ['Frango', 'Arroz branco', 'Feijão preto', 'Batata doce', 'Banana','Maça', 'Pão integral']
quantidade_teste = [100, 100, 100, 100, 100, 100, 100]
valor_energético = [139, 130, 76, 100 ,89, 52, 247]
carboidratos = [0.3, 28.2, 14, 24, 23, 14, 41]
proteinas = [26, 2.7, 4.3, 2, 1.1, 0.3, 13]
sodio = [153, 1, 99 , 36, 1, 1, 400]

alimento_consumido=int(input('Qual o alimento'))

for i,valor in enumerate(alimento):
    if alimento_consumido == i :
        print(alimento[alimento_consumido]) 
        print(quantidade_teste[alimento_consumido]) 
        print(valor_energético[alimento_consumido]) 
        print(carboidratos[alimento_consumido]) 
        print(proteinas[alimento_consumido]) 
        print(sodio[alimento_consumido]) 