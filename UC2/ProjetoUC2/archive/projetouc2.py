import pandas as pd
import mysql.connector

def obter_dados_do_banco(query):
    try:
        conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="vendas_online"
    )

        cursor = conexao.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()
# Usando a função
query_clientes = "SELECT * FROM clientes"
df_clientes = pd.DataFrame(obter_dados_do_banco(query_clientes), columns=['id_cliente','nome', 'email'])
print(df_clientes)
df_pedidos = pd.read_csv('vendas_pedidos.csv')
print(df_pedidos)
df_relacionado = pd.merge(df_clientes, df_pedidos, on='id_cliente', how='inner')
print(df_relacionado)
