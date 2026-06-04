import sqlite3
import os

DB_PATH = os.path.join('database', 'medsos.db')

def populate():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Inserindo dados de teste
    try:
        cursor.execute("INSERT INTO Usuarios (nome, tipo, email) VALUES (?, ?, ?)", 
                       ('Hospital Central', 'Instituicao', 'contato@hospitalcentral.com'))
        cursor.execute("INSERT INTO Usuarios (nome, tipo, email) VALUES (?, ?, ?)", 
                       ('João Doador', 'Doador', 'joao@email.com'))
        
        cursor.execute("INSERT INTO Medicamentos (nome, quantidade, validade, doador_id) VALUES (?, ?, ?, ?)", 
                       ('Amoxicilina', 50, '2027-12-31', 2))
        
        conn.commit()
        print("Dados inseridos com sucesso!")
    except sqlite3.IntegrityError:
        print("Dados já existem no banco.")
    finally:
        conn.close()

if __name__ == '__main__':
    populate()
