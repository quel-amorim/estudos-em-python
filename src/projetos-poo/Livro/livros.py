import json
class Livros:
    def __init__(self):
        self.livros = []

    def registrandoLivro(self,nomeLivro,qtsDisponivel):
        livro = {
            "nome" : nomeLivro,
            "qtsdis" : qtsDisponivel
        }
        self.livros.append(livro)
        with open("livrosListados.json",'w') as arquivoLivro:
            json.dump(self.livros,arquivoLivro)