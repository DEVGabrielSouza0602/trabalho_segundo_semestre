# Pedir pro usuario o nome do arq
nome_do_arquivo = input("Digite o nome do arquivo que deseja ler: ")

try:
    # Abrindo o arquivo em modo de leitura(r)
    with open(nome_do_arquivo, 'r') as arquivo:
        # Lendo e imprimindo cada linha do arquivo
        for linha in arquivo:
            print(linha)
except FileNotFoundError:
    print(f"O arquivo '{nome_do_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")
# Tenho que pensar como colocar isso certinho na dieta

# Preciso colocar a lista aqui
lista_de_treino = []

# Nomeando o arquivo
nome_do_arquivo = "lista_de_treino.txt"

# Abrindo em escrita(w)
with open(nome_do_arquivo, 'w') as arquivo:
    # Convertendo a lista em uma string pra escrever no arquivo
    for item in lista_de_treino:
        arquivo.write(item + "\n")
