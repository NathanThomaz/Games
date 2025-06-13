import tkinter as tk
from app.interface import iniciar_jogo

def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = int((largura_tela / 2) - (largura / 2))
    y = int((altura_tela / 2) - (altura / 2))
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def exibir_tela_inicial():
    janela = tk.Tk()
    janela.title("Jogo da Velha - Início")
    centralizar_janela(janela, 370, 520)
    janela.resizable(False, False)
    janela.configure(bg="#f4f4f4")

    tk.Label(janela, text="🎮 Bem-vindo ao Jogo da Velha!", font=("Arial", 16, "bold"), bg="#f4f4f4").pack(pady=20)
    tk.Label(janela, text="Escolha o modo de jogo:", font=("Arial", 12), bg="#f4f4f4").pack(pady=10)

    def iniciar_multiplayer():
        janela.destroy()
        iniciar_jogo(modo="multiplayer")

    def iniciar_ia(nivel):
        janela.destroy()
        iniciar_jogo(modo="ia", dificuldade=nivel)

    tk.Button(janela, text="👥 2 Jogadores", width=20, font=("Arial", 12), command=iniciar_multiplayer).pack(pady=5)
    tk.Button(janela, text="🤖 Contra IA (Fácil)", width=20, font=("Arial", 12), command=lambda: iniciar_ia("facil")).pack(pady=5)
    tk.Button(janela, text="🤖 Contra IA (Médio)", width=20, font=("Arial", 12), command=lambda: iniciar_ia("medio")).pack(pady=5)
    tk.Button(janela, text="🤖 Contra IA (Dificil)", width=20, font=("Arial", 12), command=lambda: iniciar_ia("dificil")).pack(pady=5)

    janela.mainloop()
