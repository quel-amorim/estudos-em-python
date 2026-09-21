from random import choice, randint
import json


class Loja:
    def __init__(self):
        self.itens_da_loja = []

    def raridades(self):
        niveis_raridades = ['Normal', 'Raro', 'Lendario']
        raridade = choice(niveis_raridades)
        return raridade

    def calculo_item_dano(self, nome_item):

        raridade = self.raridades()

        print(f'Essas são as informações do {nome_item}')

        if raridade == 'Normal':
            valor_moeda = randint(1, 5)
            multiplicador = 0.85

        elif raridade == 'Raro':
            valor_moeda = randint(5,15)
            multiplicador = 0.85

        elif raridade == 'Lendario':
            valor_moeda = randint(15,50)
            multiplicador = 2.5

        dano = valor_moeda * multiplicador

        item = {
            'nome': nome_item,
            'raridade': raridade,
            'valor': valor_moeda,
            'dano': dano
        }

        self.itens_da_loja.append(item)
        self.salvar_item()

    def salvar_item(self):
        with open('itensloja.json', 'w') as arquivo_json:
            json.dump(self.itens_da_loja, arquivo_json, indent=4)

    def carregar_informacoes_itens(self):
        try:
            with open('itensloja.json', 'r') as arquivo_json:
                self.itens_da_loja = json.load(arquivo_json)

        except FileNotFoundError:
            self.itens_da_loja = []

    def exibir(self):
        self.carregar_informacoes_itens()

        for equipamento in self.itens_da_loja:
            print(
                f"{equipamento['nome']} "
                f"${equipamento['valor']} "
                f"{equipamento['raridade']} "
                f"Dano: {equipamento['dano']}"
            )


loja = Loja()

loja.calculo_item_dano('Machado')
loja.calculo_item_dano('Espada')
loja.calculo_item_dano('Arco')

loja.exibir()