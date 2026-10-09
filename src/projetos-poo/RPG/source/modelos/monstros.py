from random import randint
import json
from gerenciamento import Gerenciamento

class Mob(Gerenciamento):
    def __init__(self):
        super().__init__()
        self.atributos = {
            'vit' : 0,
            'forca' : 0,
            'defesa' : 0,
            'inteligencia' : 0
        }

    def pegarValores(self,nomeAtributo):
        while True:
            try:
                valor = int(input(f'Valor da {nomeAtributo} :'))

                if valor <0 or valor <=20:
                    print('Não pode valores maior que 20')
                    continue

                break
            except ValueError:
                print('Apenas números !')
                continue

        return valor

    def criar(self):
        nome_mob = input('Nome do mob :')
        while True:
            try:
                print('='*10)
                print('ESCOLHA DE MODELOS ATRIBUTOS')
                print('='*10)
                modeloAtributo = int(input('[1] RANDOMIZAR\n[2] DEFINIÇÃO PELO USUÁRIO\nEscolha :'))
                if modeloAtributo == 1:
                    self.atributos['vit'] = randint(0,20)
                    self.atributos['forca'] = randint(0,20)
                    self.atributos['defesa'] =randint(0,20)
                    self.atributos['inteligencia'] = randint(0, 20)

                    return self.atributos
                
                elif modeloAtributo == 2:
                    self.atributos['vit'] = self.pegarValores('Vitalidade')
                    self.atributos['forca'] = self.pegarValores('Forca')
                    self.atributos['defesa'] =self.pegarValores('Defesa')
                    self.atributos['inteligencia'] = self.pegarValores('Inteligencia')

                    return self.atributos
                
                break
            except ValueError:
                print('Apenas números inteiros !')
                continue

        novoMob = {
            'nome' : nome_mob,
            'nivel' : 1,
            'atributos' : self.atributos.copy()
        }
        self.mobs.append(novoMob)
        self.salvarMobs()

    def salvarMobs(self):
        with open('monstros.json','w') as arquivo_mobs:
            json.dump(self.mobs,arquivo_mobs)

    def exibirMob(self):
        with open('monstros.json','r') as mobs:
            self.mobs = json.load(mobs)

        for npc in self.mobs:
            print(f' {npc['nome']} LV {npc['nivel']}')

menu = Mob()

menu.exibirMob()