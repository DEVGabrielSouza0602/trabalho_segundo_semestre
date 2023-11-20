def ler_nome_e_senha(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            if len(linhas) >= 2:
                return linhas[0].strip(), linhas[1].strip()
            else:
                print(
                    f"O arquivo '{nome_arquivo}' não contém informações suficientes.")
                return None, None
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None, None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None, None
