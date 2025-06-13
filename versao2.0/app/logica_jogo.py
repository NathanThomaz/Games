def verificar_vencedor(tabuleiro):
    # Linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != "":
            return linha[0]

    # Colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != "":
            return tabuleiro[0][i]

    # Diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "":
        return tabuleiro[0][2]

    return None
