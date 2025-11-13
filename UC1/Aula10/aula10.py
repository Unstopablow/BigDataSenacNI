import sys # Usaremos o sys para ver a versão do Python
# A convenção é "import pandas as pd"
try:
    print("Tentando importar a biblioteca Pandas...")
    import pandas as pd
    print("Pandas importado com sucesso!")

# É uma boa prática verificar a versão
    print(f"Versão do Pandas instalada: {pd.__version__}")
    print(f"Versão do Python: {sys.version.split()[0]}")

except ImportError:
    print("\n--- ERRO ---")
    print("A biblioteca Pandas não foi encontrada.")
    print("Por favor, instale-a usando o comando no seu terminal:")
    print("pip install pandas")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
finally:
    print("Verificação de setup concluída.\n")
