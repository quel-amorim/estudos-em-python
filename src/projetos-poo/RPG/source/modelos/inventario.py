from gerenciamento import Gerenciamento
class Inventario(Gerenciamento):
    def __init__(self):
        super().__init__()

    def buscar_itens(self):
        print('Itens atuais no inventario {}'.format(len(self.itens_loja)))
        