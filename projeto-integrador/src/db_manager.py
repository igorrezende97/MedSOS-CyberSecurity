import sqlite3
import os

# Define o caminho do banco dentro da pasta database
DB_PATH = os.path.join('database', 'medsos.db')

def connect_db():
    """Estabelece a conexão com o banco de dados SQLite."""
    # Garante que a pasta database existe
    if not os.path.exists('database'):
        os.makedirs('database')
    
    conn = sqlite3.connect(DB_PATH)
    return conn

def initialize_db():
    """Executa o schema SQL para criar as tabelas se elas não existirem."""
    # Ajuste o caminho do schema caso necessário
    schema_path = os.path.join('database', 'schema.sql')
    
    with open(schema_path, 'r') as f:
        schema = f.read()
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso em:", DB_PATH)

if __name__ == '__main__':
    initialize_db()
