from random import uniform,randint,choice
from datetime import datetime , timedelta
import json
class Produto:
    def __init__(self):
        self.meus_produtos = []
        self.categorias = ['Alimentos','Domestica','Eletronicos','Hardware','Software']
        

    def qts_produtos(self):
        while True:
            try:
                qts = int(input('Criar quantos produtos :'))
                
                if qts < 0:
                    print('Não é permitido deixar em valor zero !')
                    continue

                break
            except ValueError:
                print('Erro : apenas número é permitido ,volte ao começo !')
                continue

        return qts

    
    def criacao_produto(self):
        data_atual = datetime.now()
        identificacao = len(self.meus_produtos) + 1

        quantidade = self.qts_produtos()

        for _ in range(quantidade):

            nome_p = f"PRODUTO N#{identificacao}"
            valor = round(uniform(100, 10000), 2)
            categoria = choice(self.categorias)
            datavencimento = data_atual + timedelta(days=randint(1, 30))
            formatando_data = datavencimento.strftime("%d/%m/%Y")

            novo_produto = {
                'id': identificacao,
                'nome': nome_p,
                'valor': valor,
                'categoria' : categoria,
                'data_adicao': formatando_data,
                'data_vencimento': formatando_data
            }

            self.meus_produtos.append(novo_produto)

            identificacao += 1

        self.salvar_produtos()
        print(f"PRODUTOS {quantidade} CRIADOS COM SUCESSO!")

    def salvar_produtos(self):
        with open('produtos.json','w') as arquivo_json:
            json.dump(self.meus_produtos,arquivo_json)


produto = Produto()
produto.criacao_produto()