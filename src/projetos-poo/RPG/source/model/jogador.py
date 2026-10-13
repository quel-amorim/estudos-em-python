class Jogador:
    def __init__(self,nomeJogador):
        self.nomeJogador = nomeJogador

    def __repr__(self):
        return f"Olá {self.nomeJogador} bem-vindo ao RPG DO TERMINAL !"


teste = Jogador(nomeJogador="quel-Amorim")