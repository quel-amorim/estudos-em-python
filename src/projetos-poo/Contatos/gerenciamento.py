import json
class Armazenamento:
    def __init__(self):
        self.listaContatos = []

    def salvamentoContato(self):
        with open("dadosContatos.json",'w') as arquivoDados:
            json.dump(self.listaContatos,arquivoDados)

    def carregamentoContato(self):
        with open("dadosContatos.json",'r') as arquivoSalvos:
            json.load(arquivoSalvos)
        