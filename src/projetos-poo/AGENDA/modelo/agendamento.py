import json
class Agenda:
    def __init__(self):
        self.contatos = []

    def salvamento_contato(self):
        with open("contatos.json",'w') as arquivo_contato:
            json.dump(self.contatos,arquivo_contato)

    def carregamento_contato(self):
        try:
            with open("contatos.json",'r') as arquivo_contato:
                self.contatos = json.load(arquivo_contato)

        except FileNotFoundError:
                self.contatos = []
                print('Não tem nada salvo :' , self.contatos)

    def exibirContatos(self):
         for contato in self.contatos:
              print(f' * {contato['nome']} -> {contato['telefone']}')