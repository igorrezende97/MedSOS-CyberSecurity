import sqlite3
import os

# Ajuste o caminho para onde o seu banco realmente está
db_path = os.path.join('..', 'database', 'medsos.db')

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Deleta a linha que tem o 'a' na validade
    cursor.execute("DELETE FROM Medicamentos WHERE validade = 'a'")
    
    conn.commit()
    print("Sucesso: Linhas com erro foram removidas!")
    conn.close()
except Exception as e:
    print(f"Erro ao limpar: {e}")