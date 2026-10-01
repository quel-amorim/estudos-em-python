import sqlite3

class Dados:
    def __init__(self,banco="personagens.db"):
        self.banco = banco
        self.conexao = sqlite3.connect(banco)
        self.comentarios = self.conexao.cursor()
        #
        self.comentarios.execute("CREATE TABLE IF NOT EXISTS personagens (ID INTEGER PRIMARY KEY AUTOINCREMENT , NOME TEXT , MAESTRIA TEXT NOT NULL , NIVEL INTEGER NOT NULL)")
        self.conexao.commit()