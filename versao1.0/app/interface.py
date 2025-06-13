import tkinter as tk
from tkinter import messagebox
from app.logica_jogo import verificar_vencedor

class JogoDaVelha:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Jogo da Velha")
        self.janela.resizable(False, False)
        self.centralizar_janela(370, 500)

        self.cores = {
            "fundo": "#f4f4f4",
            "botao_bg": "#ffffff",
            "botao_fg": "#333333",
            "realce": "#4CAF50",
            "texto_vez": "#555555",
            "botao_reiniciar": "#e0e0e0"
        }

        self.vitorias = {"X": 0, "O": 0}
        self.jogador_atual = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.botoes = [[None]*3 for _ in range(3)]

        self.janela.configure(bg=self.cores["fundo"])

        self.label_placar = tk.Label(
            self.janela, text=self.obter_placar(), font=('Arial', 12), bg=self.cores["fundo"]
        )
        self.label_placar.pack(pady=(10, 0))

        self.label_vez = tk.Label(
            self.janela, text=f"Vez de: {self.jogador_atual}", font=('Arial', 14),
            bg=self.cores["fundo"], fg=self.cores["texto_vez"]
        )
        self.label_vez.pack(pady=(5, 10))

        self.criar_interface()

    def centralizar_janela(self, largura, altura):
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        x = int((largura_tela / 2) - (largura / 2))
        y = int((altura_tela / 2) - (altura / 2))
        self.janela.geometry(f"{largura}x{altura}+{x}+{y}")

    def obter_placar(self):
        return f"Vitórias - X: {self.vitorias['X']} | O: {self.vitorias['O']}"

    def criar_interface(self):
        frame_tabuleiro = tk.Frame(self.janela, bg=self.cores["fundo"])
        frame_tabuleiro.pack(pady=10)

        for linha in range(3):
            for coluna in range(3):
                botao = tk.Button(
                    frame_tabuleiro, text="", font=('Arial', 20), width=5, height=2,
                    bg=self.cores["botao_bg"], fg=self.cores["botao_fg"],
                    activebackground=self.cores["realce"],
                    command=lambda i=linha, j=coluna: self.jogar(i, j)
                )
                botao.grid(row=linha, column=coluna, padx=4, pady=4)
                self.botoes[linha][coluna] = botao

        self.botao_reiniciar = tk.Button(
            self.janela,
            text="🔁 Reiniciar",
            font=('Arial', 12, 'bold'),
            command=self.reiniciar_jogo,
            bg=self.cores["botao_reiniciar"],
            fg="#000000",
            relief=tk.RAISED,
            bd=2,
            padx=10,
            pady=5
        )
        self.botao_reiniciar.pack(pady=15)

    def jogar(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == "":
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.botoes[linha][coluna].config(text=self.jogador_atual)

            vencedor = verificar_vencedor(self.tabuleiro)
            if vencedor:
                self.vitorias[vencedor] += 1
                self.finalizar_jogo(f"{vencedor} venceu!")
            elif all(all(celula != "" for celula in linha) for linha in self.tabuleiro):
                self.finalizar_jogo("Empate!")
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
                self.label_vez.config(text=f"Vez de: {self.jogador_atual}")

    def finalizar_jogo(self, mensagem):
        for linha in self.botoes:
            for botao in linha:
                botao.config(state=tk.DISABLED)
        messagebox.showinfo("Fim de Jogo", mensagem)
        self.label_vez.config(text=mensagem)
        self.label_placar.config(text=self.obter_placar())

    def reiniciar_jogo(self):
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.jogador_atual = "X"
        self.label_vez.config(text=f"Vez de: {self.jogador_atual}")
        for linha in range(3):
            for coluna in range(3):
                self.botoes[linha][coluna].config(text="", state=tk.NORMAL)

def iniciar_jogo():
    janela = tk.Tk()
    JogoDaVelha(janela)
    janela.mainloop()
