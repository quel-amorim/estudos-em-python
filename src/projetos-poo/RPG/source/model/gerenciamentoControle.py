import json
class Gerenciamento:
    def __init__(self):
        """Separando as minhas listas"""
        self.maestria = []
        self.mobs = []

    def salvamentoMaestria(self):
        with open('maestrias.json','w') as arquivoMaestria:
            json.dump(self.maestria,arquivoMaestria)

    def salvamentoMobs(self):
        with open('mobs.json','w') as arquivoMob:
            json.dump(self.mobs,arquivoMob)

    def carregamentoMobs(self):
        try:
            with open('mobs.json','r') as arquivoMob:
                self.mobs = json.load(arquivoMob)
        except FileNotFoundError:
            self.mobs = []

    def carregamentoMaestria(self):
        try:
            with open('maestrias.json','r') as arquivoMaestria:
                self.maestria = json.load(arquivoMaestria)
        except FileNotFoundError:
            self.maestria = []