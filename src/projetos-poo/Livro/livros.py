
class Livro:
    def __init__(self, nomeLivro, numeroPaginas, pagAtual=1):
        self.nome = nomeLivro
        self.nPag = numeroPaginas
        self.pagAtual = pagAtual

    def lendoP(self, qts):
        for _ in range(qts):

            # Verifica se o livro já chegou ao fim
            if self.pagAtual > self.nPag:
                print("\nVocê já terminou de ler o livro!")
                return

            print(f"{self.pagAtual}° Página", end=" ")

            self.pagAtual += 1

        if self.pagAtual <= self.nPag:
            diferenca = self.nPag - self.pagAtual

            print(
                f"\nVocê parou na página {self.pagAtual}, "
                f"faltam {diferenca} páginas."
            )
        else:
            print(f"\nFim do livro: {self.nome}. Parabéns!")


l1 = Livro("Exemplo01", 100)

l1.lendoP(10)
l1.lendoP(110)
