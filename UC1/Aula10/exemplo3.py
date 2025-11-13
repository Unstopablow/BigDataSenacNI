import pandas as pd

nome_do_arquivo_csv = 'ClassicDisco.csv'
df_disco = None # Inicializamos o DataFrame como None
try:
    print(f"--- Lendo o arquivo '{nome_do_arquivo_csv}' ---")
    
    # O comando mágico para ler CSV!
    df_disco = pd.read_csv(nome_do_arquivo_csv)
    
    print("Arquivo lido com sucesso!")
    
    # Vamos espiar os dados. .head() mostra as 5 primeiras linhas
    print("\n--- As 5 primeiras linhas do DataFrame (.head()) ---")
    print(df_disco.head())
    
    # .info() nos dá um resumo das colunas e tipos de dados
    print("\n--- Informações do DataFrame (.info()) ---")
    df_disco.info()
except FileNotFoundError:
    print(f"\n--- ERRO: Arquivo não encontrado ---")
    print(f"O arquivo '{nome_do_arquivo_csv}' não foi encontrado no diretório.")
    print("Por favor, baixe o CSV do Kaggle e coloque-o na mesma pasta do script.")
except NameError:
    print("\nERRO: O pandas (pd) não foi importado corretamente.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")
finally:
    print("Leitura de CSV concluída.\n")
