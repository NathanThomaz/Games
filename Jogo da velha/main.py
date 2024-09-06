# Inicializa o tabuleiro
tabuleiro = [" " for _ in range(9)]
pos_livre = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_inicio():
    print('\n')
    print("#################")
    print("# Jogo da velha #")
    print("#################")
    print('\n Os jogadores são X e O, preste atenção na sua rodada!\n')

def imprimir_tabuleiro():
    print(f"       {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("       --+---+--")
    print(f"       {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("       --+---+--")
    print(f"       {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}\n")

def verificar_vencedor():
    # Possíveis combinações vencedoras
    combinacoes = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Linhas
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Colunas
        (0, 4, 8), (2, 4, 6)  # Diagonais
    ]
    
    for a, b, c in combinacoes:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] and tabuleiro[a] != " ":
            return tabuleiro[a]
    return None

def jogar(jogador):
    while True:
        try:
            pos = int(input(f"Jogador {jogador}, escolha uma posição (1-9): ")) - 1
            
            if pos < 0 or pos > 8:
                print("Posição inválida. Tente novamente.")
            elif (pos + 1) not in pos_livre:
                print(f"Posição já ocupada. Posições livres: {pos_livre}")
            else:
                tabuleiro[pos] = jogador
                pos_livre.remove(pos + 1)  # Remove a posição da lista de posições livres
                break
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 9.")

def jogo_da_velha():
    jogadores = ["X", "O"]
    vencedor = None
    jogadas = 0
    
    while vencedor is None and jogadas < 9:
        imprimir_tabuleiro()
        jogador_atual = jogadores[jogadas % 2]
        jogar(jogador_atual)
        vencedor = verificar_vencedor()
        jogadas += 1
    
    imprimir_tabuleiro()
    if vencedor:
        print(f"Jogador {vencedor} ganhou!")
    else:
        print("Empate!")

# Iniciar o jogo
if __name__ == "__main__":
    print_inicio()
    jogo_da_velha()
