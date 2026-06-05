import os

def exibir_menu():
    print("\n--- MedSOS - Sistema de Gerenciamento ---")
    print("1 - Cadastrar Medicamento")
    print("2 - Consultar Estoque")
    print("3 - Sair")
    return input("Escolha uma opção: ")

def main():
    while True:
        opcao = exibir_menu()

        if opcao == '1':
            # Chama o script de cadastro
            os.system('python cadastro.py')
        elif opcao == '2':
            # Chama o script de consulta
            os.system('python consulta.py')
        elif opcao == '3':
            print("Encerrando o MedSOS. Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == '__main__':
    main()