from gerenciamentoControle import Gerenciamento
class Maestria:
    def __init__(self,nomeMaestria,elemento,vitalidade,forca,defesa,agilidade,inteligencia):
        self.nomeMaestria = nomeMaestria
        self.elemento = elemento
        self.nivel = 1
        self.vitalidade = vitalidade
        self.forca = forca
        self.defesa = defesa
        self.agilidade = agilidade
        self.inteligencia = inteligencia
        self.atributos = {
            "vitalidade" : self.vitalidade,
            "forca" : self.forca,
            "defesa" : self.defesa,
            "agilidade" : self.agilidade,
            "inteligencia" : self.inteligencia
        }

    def exibirAtributos(self):
        print(f"---- |Atributos {self.nomeMaestria}|----\n")
        print(f"     VIT : {self.atributos['vitalidade']}")
        print(f"     STR : {self.atributos['forca']}")
        print(f"     RES : {self.atributos['defesa']}")
        print(f"     AG : {self.atributos['agilidade']}")
        print(f"     INT : {self.atributos['inteligencia']}")

    def __repr__(self):
        return f" {self.nomeMaestria} Nv {self.nivel} | Elemento {self.elemento}\n"

class Lutador(Maestria):
    def __init__(self):
        super().__init__("LUTADOR","TERRA",10,15,12,10,8)

class Mago(Maestria):
    def __init__(self):
        super().__init__("MAGO","FOGO",10,8,12,15,17)

class Paladino(Maestria):
    def __init__(self):
        super().__init__("PALADINO","LUZ",15,17,10,15,12)


admin = Gerenciamento()

lutador = Lutador()
mago = Mago()
paladino = Paladino()
