from gerenciamentoControle import Gerenciamento
class Monstro:
    def __init__(self,nomeMob,elemento,vitalidade,forca,defesa,agilidade,inteligencia):
        self.nomeMob = nomeMob
        self.nivel = 1
        self.elemento = elemento
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