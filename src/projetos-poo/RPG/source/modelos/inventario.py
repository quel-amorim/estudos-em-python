class Inventario:
    def __init__(self):
        self.meus_itens = []

    def buscar_itens(self):
        print('Itens atuais no inventario {}'.format(len(self.meus_itens)))
        