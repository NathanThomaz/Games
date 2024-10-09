tabuleiro = [[" " for _ in range(8)] for _ in range(8)]

def imprimir_tabuleiro(tabuleiro):
    for i in range(1):
        print(f"{tabuleiro[i]}\n")
        for j in range(8):
            print(f"{tabuleiro[j]}")

imprimir_tabuleiro(tabuleiro)



def imprimir_tabuleiro(tabuleiro):
    for i in range(8):
        print(" ".join(tabuleiro[i]))

imprimir_tabuleiro(tabuleiro)
