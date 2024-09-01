import subprocess
import os

def printar_menu():
    print('\n')
    print("####################################")
    print("#  Bem-vindo ao portal dos games!  #")
    print("####################################")

def obter_caminho_relativo(arquivo):
    return os.path.join(os.path.dirname(__file__), arquivo)

def jogar_da_velha():
    caminho = obter_caminho_relativo("Jogo da velha/main.py")
    subprocess.run(["python", caminho])

def jogar_xadrez():
    caminho = obter_caminho_relativo("Xadrez/main.py")
    subprocess.run(["python", caminho])

def jogar_forca():
    caminho = obter_caminho_relativo("Forca/main.py")
    subprocess.run(["python", caminho])


def selecionar_game():
    try:
        op = int(input('\nDigite o número do game que deseja iniciar:\n1. Jogo da Velha\n2. Xadrez\n3. Jogo da Forca\n4. Sair\nEscolha: '))
        
        if op == 1:
            jogar_da_velha()
        elif op == 2:
            jogar_xadrez()
        elif op == 3:
            jogar_forca()
        elif op == 4:
            print("Saindo...")
            exit()  # Encerra o programa
        else:
            print("Opção inválida. Por favor, escolha um número entre 1 e 4.")
    except ValueError:
        print("Erro: Entrada inválida. Digite um número inteiro.")

def menu():
    while True:
        printar_menu() 
        selecionar_game()

# Iniciar o menu
if __name__ == "__main__":
    menu()
