import json
class Agenda:
    def __init__(self):
        self.contatos = []

    def salvamento_contato(self):
        with open("contatos.json",'w') as arquivo_contato:
            json.dump(self.contatos,arquivo_contato)

    