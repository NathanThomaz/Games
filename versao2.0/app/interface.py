import tkinter as tk
from tkinter import messagebox
import random
from app.logica_jogo import verificar_vencedor
import copy

class JogoDaVelha:
    def __init__(self, janela, modo="multiplayer", dificuldade="facil"):
        self.janela = janela
        self.modo = modo
        self.dificuldade = dificuldade

        self.janela.title("Jogo da Velha")
        self.janela.resizable(False, False)
        self.centralizar_janela(370, 520)

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
        self.proximo_iniciador = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.botoes = [[None]*3 for _ in range(3)]
        self.jogo_ativo = True

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

        frame_botoes = tk.Frame(self.janela, bg=self.cores["fundo"])
        frame_botoes.pack(pady=10)

        self.botao_reiniciar = tk.Button(
            frame_botoes,
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
        self.botao_reiniciar.grid(row=0, column=0, padx=10)

        self.botao_inicio = tk.Button(
            frame_botoes,
            text="🔙 Início",
            font=('Arial', 12, 'bold'),
            command=self.voltar_ao_inicio,
            bg=self.cores["botao_reiniciar"],
            fg="#000000",
            relief=tk.RAISED,
            bd=2,
            padx=10,
            pady=5
        )
        self.botao_inicio.grid(row=0, column=1, padx=10)

    def voltar_ao_inicio(self):
        from app.tela_inicial import exibir_tela_inicial
        self.janela.destroy()
        exibir_tela_inicial()

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

    def desativar_botoes(self):
        for linha in self.botoes:
            for botao in linha:
                if botao["state"] == tk.NORMAL:
                    botao.config(state=tk.DISABLED)

    def ativar_botoes(self):
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == "":
                    self.botoes[i][j].config(state=tk.NORMAL)

    def jogar(self, linha, coluna, jogada_ia=False):
        if not self.jogo_ativo or self.tabuleiro[linha][coluna] != "":
            return

        self.tabuleiro[linha][coluna] = self.jogador_atual
        self.botoes[linha][coluna].config(text=self.jogador_atual)

        vencedor = verificar_vencedor(self.tabuleiro)
        if vencedor:
            self.vitorias[vencedor] += 1
            self.proximo_iniciador = vencedor
            self.finalizar_jogo(f"{vencedor} venceu!")
        elif all(all(celula != "" for celula in linha) for linha in self.tabuleiro):
            # Empate: alterna o iniciador
            self.proximo_iniciador = "O" if self.proximo_iniciador == "X" else "X"
            self.finalizar_jogo("Empate!")
        else:
            self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
            self.label_vez.config(text=f"Vez de: {self.jogador_atual}")

            if self.modo == "ia" and self.jogador_atual == "O" and not jogada_ia:
                self.desativar_botoes()
                self.janela.after(100, self.jogada_ia)

    def jogada_ia(self):
        if self.dificuldade == "facil":
            self.jogada_aleatoria()
        elif self.dificuldade == "medio":
            self.jogada_nivel_medio()
        elif self.dificuldade == "dificil":
            self.jogada_nivel_dificil()

    def jogada_aleatoria(self):
        opcoes_livres = [(i, j) for i in range(3) for j in range(3) if self.tabuleiro[i][j] == ""]
        if opcoes_livres:
            linha, coluna = random.choice(opcoes_livres)
            self.jogar(linha, coluna, jogada_ia=True)
            self.ativar_botoes()

    def jogada_nivel_medio(self):
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == "":
                    self.tabuleiro[i][j] = "O"
                    if verificar_vencedor(self.tabuleiro) == "O":
                        self.tabuleiro[i][j] = ""
                        self.jogar(i, j, jogada_ia=True)
                        self.ativar_botoes()
                        return
                    self.tabuleiro[i][j] = ""

        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == "":
                    self.tabuleiro[i][j] = "X"
                    if verificar_vencedor(self.tabuleiro) == "X":
                        self.tabuleiro[i][j] = ""
                        self.jogar(i, j, jogada_ia=True)
                        self.ativar_botoes()
                        return
                    self.tabuleiro[i][j] = ""

        self.jogada_aleatoria()

    def jogada_nivel_dificil(self):
        melhor_valor = -float('inf')
        melhor_jogada = None

        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == "":
                    copia_tabuleiro = copy.deepcopy(self.tabuleiro)
                    copia_tabuleiro[i][j] = "O"
                    valor = self.minimax(copia_tabuleiro, 0, False)
                    if valor > melhor_valor:
                        melhor_valor = valor
                        melhor_jogada = (i, j)

        if melhor_jogada:
            linha, coluna = melhor_jogada
            self.jogar(linha, coluna, jogada_ia=True)
            self.ativar_botoes()

    def minimax(self, tabuleiro, profundidade, eh_maximizador):
        vencedor = verificar_vencedor(tabuleiro)
        if vencedor == "O":
            return 1
        elif vencedor == "X":
            return -1
        elif all(all(celula != "" for celula in linha) for linha in tabuleiro):
            return 0

        if eh_maximizador:
            melhor_valor = -float('inf')
            for i in range(3):
                for j in range(3):
                    if tabuleiro[i][j] == "":
                        tabuleiro[i][j] = "O"
                        valor = self.minimax(tabuleiro, profundidade + 1, False)
                        tabuleiro[i][j] = ""
                        melhor_valor = max(melhor_valor, valor)
            return melhor_valor
        else:
            pior_valor = float('inf')
            for i in range(3):
                for j in range(3):
                    if tabuleiro[i][j] == "":
                        tabuleiro[i][j] = "X"
                        valor = self.minimax(tabuleiro, profundidade + 1, True)
                        tabuleiro[i][j] = ""
                        pior_valor = min(pior_valor, valor)
            return pior_valor

    def finalizar_jogo(self, mensagem):
        self.jogo_ativo = False
        for linha in self.botoes:
            for botao in linha:
                botao.config(state=tk.DISABLED)
        messagebox.showinfo("Fim de Jogo", mensagem)
        self.label_vez.config(text=mensagem)
        self.label_placar.config(text=self.obter_placar())

    def reiniciar_jogo(self):
        self.jogo_ativo = True
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.jogador_atual = self.proximo_iniciador
        self.label_vez.config(text=f"Vez de: {self.jogador_atual}")
        for linha in range(3):
            for coluna in range(3):
                self.botoes[linha][coluna].config(text="", state=tk.NORMAL)
        if self.modo == "ia" and self.jogador_atual == "O":
            self.janela.after(100, self.jogada_ia)

def iniciar_jogo(modo="multiplayer", dificuldade="facil"):
    janela = tk.Tk()
    JogoDaVelha(janela, modo=modo, dificuldade=dificuldade)
    janela.mainloop()
