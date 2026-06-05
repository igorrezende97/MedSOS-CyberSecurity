import sqlite3
import os
import re

# Caminho para o banco de dados
DB_PATH = os.path.join('..', 'medsos.db')

def validar_input_numerico(pergunta):
    """Garante que o usuário digite apenas números."""
    while True:
        valor = input(pergunta)
        if valor.isdigit():
            return int(valor)
        print("Erro: Por favor, digite apenas números.")

def cadastrar_medicamento():
    print("\n--- Cadastro Seguro de Medicamento ---")
    
    # Validação do nome
    nome = input("Nome do medicamento: ").strip()
    if not nome:
        print("Erro: O nome não pode estar vazio.")
        return

    # Validação da quantidade
    quantidade = validar_input_numerico("Quantidade em estoque: ")

    # Validação da data via Regex
    while True:
        validade = input("Data de validade (AAAA-MM-DD): ").strip()
        if re.match(r'^\d{4}-\d{2}-\d{2}$', validade):
            break
        else:
            print("Erro: Formato inválido! Use AAAA-MM-DD (ex: 2026-12-31).")

    # Inserção segura no banco de dados
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Medicamentos (nome, quantidade, validade) VALUES (?, ?, ?)", 
                       (nome, quantidade, validade))
        conn.commit()
        print(f"Sucesso: {nome} cadastrado com segurança!")
        conn.close()
    except Exception as e:
        print(f"Erro crítico no banco de dados: {e}")

if __name__ == '__main__':
    cadastrar_medicamento()