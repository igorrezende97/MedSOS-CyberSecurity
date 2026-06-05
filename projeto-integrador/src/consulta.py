import sqlite3
import os

DB_PATH = os.path.join('..','database','medsos.db')

def consultar_estoque():
    """Busca e exibe todos os medicamentos cadastrados."""
    if not os.path.exists(DB_PATH):
        print("Erro: O banco de dados não foi encontrado. Verifique o caminho.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("\n--- Relatório de Estoque de Medicamentos ---")
    cursor.execute("SELECT id, nome, quantidade, validade FROM Medicamentos")
    medicamentos = cursor.fetchall()

    if not medicamentos:
        print("Nenhum medicamento encontrado no estoque.")
    else:
        for m in medicamentos:
            print(f"ID: {m[0]} | Nome: {m[1]} | Qtd: {m[2]} | Validade: {m[3]}")
    
    conn.close()
    print("--------------------------------------------\n")

if __name__ == '__main__':
    consultar_estoque()