import pandas as pd
try:
    print("--- Criando um DataFrame (2D) de Filmes ---")
    
    dados_filmes = {
    'nome_do_filme': ['O Poderoso Chefão', 'Interestelar', 'Parasita', 'Matrix'],
    'ano_de_lancamento': [1972, 2014, 2019, 1999],
    'genero': ['Criminal', 'Ficção Científica', 'Suspense', 'Ficção Científica']
    }
    
    # Criamos o DataFrame a partir do dicionário
    df_filmes = pd.DataFrame(dados_filmes)
    
    print("\n--- DataFrame Criado ---")
    print(df_filmes)
    
    print("\n--- Informações do DataFrame (.info()) ---")
    df_filmes.info()

except NameError:
    print("\nERRO: O pandas (pd) não foi importado corretamente.")
except Exception as e:
    print(f"Ocorreu um erro ao criar o DataFrame: {e}")
finally:
    print("Criação de DataFrame concluída.\n")