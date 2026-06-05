import sqlite3
import os

# Caminho para o banco (subindo um nível da pasta src)
DB_PATH = os.path.join('..','database','medsos.db')

def cadastrar_medicamento():
    print("\n--- Cadastro de Novo Medicamento ---")
    nome = input("Nome do medicamento: ")
    quantidade = input("Quantidade em estoque: ")
    validade = input("Data de validade (AAAA-MM-DD): ")

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Insere o novo dado na tabela
        cursor.execute("INSERT INTO Medicamentos (nome, quantidade, validade) VALUES (?, ?, ?)", 
                       (nome, quantidade, validade))
        
        conn.commit()
        print(f"Sucesso: {nome} cadastrado com sucesso!")
        conn.close()
    except Exception as e:
        print(f"Erro ao cadastrar: {e}")

if __name__ == '__main__':
    cadastrar_medicamento()