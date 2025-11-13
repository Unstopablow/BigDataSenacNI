import pandas as pd

try:
    print("--- Criando uma Série (1D) com Cargos e Salários ---")

    dados_salarios = {
    'Analista de Dados': 7000.50,
    'Cientista de Dados': 12000.00,
    'Engenheiro de Dados': 11000.00,
    'Analista de BI': 6500.00
    }

# Criamos a Série a partir do dicionário
    serie_salarios = pd.Series(dados_salarios)

    print("\n--- Série Criada ---")
    print(serie_salarios)
    
    # Explorando a estrutura
    print("\n--- Explorando a Estrutura da Série ---")
    print(f"Índice (Chaves): {list(serie_salarios.index)}")
    print(f"Valores: {list(serie_salarios.values)}")
    
    # Acessando um valor pelo índice (chave)
    print("\n--- Acessando um Valor ---")
    print(f"Salário do Cientista de Dados: R$ {serie_salarios['Cientista de Dados']:.2f}")
except NameError:
    print("\nERRO: O pandas (pd) não foi importado corretamente.")
except Exception as e:
    print(f"Ocorreu um erro ao criar a Série: {e}")
finally:
    print("Exploração de Séries concluída.\n")
