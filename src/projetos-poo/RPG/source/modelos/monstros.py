import json
from random import randint
class Modelo_mob:
    def __init__(self,nome,elemento):
        self.nome = nome
        self.nivel = 1
        self.elemento = elemento
        self.gerar_atributos()

    def gerar_atributos(self):
        atributos = {
            'vit' : randint(0,20),
            'forca' : randint(0,20),
            'defesa' : randint(0,20),
            'inteligencia' : randint(0,20)
        }
        return atributos

    def exibir_atributos(self):
        atributos = self.gerar_atributos()
        print(f'---- ATRIBUTOS {self.nome} ----\n')
        print(f"    ELEMENTO     : {self.elemento}")
        print(f"    VITALIDADE   : {atributos['vit']}")
        print(f"    FORCA        : {atributos['forca']}")
        print(f"    DEFESA       : {atributos['defesa']}")
        print(f"    INTELIGENCIA : {atributos['inteligencia']}\n")

m1 = Modelo_mob('ZUMBI','TERRA')
m2 = Modelo_mob('DEMONIO','ESCURIDAO')
m3 = Modelo_mob('ANJO','LUZ')

lista_mobs = []
lista_mobs.append(m1)
lista_mobs.append(m2)
lista_mobs.append(m3)

m1.exibir_atributos()
m2.exibir_atributos()
m3.exibir_atributos()