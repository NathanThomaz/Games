# Jogo da Velha - Versão 2.0 🎮

Bem-vindo ao **Jogo da Velha** desenvolvido em Python com Tkinter! Esta versão traz uma interface moderna, modos de jogo variados e diferentes níveis de dificuldade para desafiar amigos ou jogar contra uma IA estratégica.

---

## 🧩 Funcionalidades

- ✅ Interface gráfica intuitiva (Tkinter)
- 👥 Modo multiplayer (2 jogadores)
- 🤖 Modo contra IA:
    - Fácil: movimentos aleatórios
    - Médio: vence/bloqueia quando possível
    - Difícil: estratégia ideal com Minimax
- 🔄 Botão para reiniciar a partida
- ⬅️ Retorno ao menu inicial
- 🔁 Alternância automática de quem inicia em caso de empate
- 📊 Placar de vitórias para X e O

---

## 📁 Estrutura de Pastas

```
versao2.0/
│
├── app/
│   ├── interface.py          # Interface principal do jogo
│   ├── logica_jogo.py        # Lógica de verificação de vencedor
│   └── tela_inicial.py       # Tela de boas-vindas e seleção de modo
│
├── main.py                   # Arquivo principal para execução
└── README.md                 # Documentação do projeto
```

---

## ▶️ Como executar

### 1. Clone o repositório e navegue até a versão 1.0

```bash
git clone https://github.com/seu-usuario/jogo-da-velha.git
cd jogo-da-velha/versao1.0
```

### 2. (Opcional) Crie um ambiente virtual

```bash
python -m venv venv
# Ative o ambiente virtual:
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Execute o jogo

```bash
python main.py
```

---

## 💡 Requisitos

- Python 3.7 ou superior
- Tkinter (incluso na maioria das instalações Python)

---

## 🧠 Créditos

Desenvolvido por **Nathan Thomaz** com foco em lógica de programação, design de interface e aplicação de IA com Minimax.

---

Sinta-se à vontade para usar, modificar e compartilhar. Divirta-se jogando! 🎉