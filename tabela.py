import pandas as pd
import sqlite3

# Ler o arquivo XLS
xls_file = 'bancos.xls'
data = pd.read_excel(xls_file)

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('banco.db')

# Salvar os dados do DataFrame para o banco de dados
data.to_sql('bancos', conn, if_exists='replace', index=False)


cursor = conn.cursor()
# Fechar a conexão com o banco de dados
conn.close()
