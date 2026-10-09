import json
import os
from random import randint
from gerenciamento import Gerenciamento
class Modelo_maestria(Gerenciamento):
    def __init__(self):
        super().__init__()
        self.atributos = {
            'vit' :0,
            'forca' : 0,
            'defesa' : 0,
            'inteligencia' : 0
        }
        self.nivel = 1
        self.carregar_dados()

    def carregar_dados(self):
        """Carrega as maestrias salvas anteriormente se o arquivo existir."""
        if os.path.exists('maestria.json'):
            try:
                with open('maestria.json', 'r', encoding='utf-8') as arquivo_json:
                    self.maestrias = json.load(arquivo_json)
            except json.JSONDecodeError:
                self.maestrias = []


    def definir_valores(self,nome_atributo):
        while True:
            try:
                valor = int(input(f'Valor {nome_atributo} (0 , 20):'))

                if valor <=0 or valor <=20:
                    print('Não poder colocar valores maior que 20 ou menor que 0')
                    continue

                break
            except ValueError:
                print('Apenas números !')
                continue

        return valor

    def randomizar_valores(self):
        self.atributos['vit'] = randint(0 ,20)
        self.atributos['forca'] = randint(0 ,20)
        self.atributos['defesa'] = randint(0 ,20)
        self.atributos['inteligencia'] = randint(0 ,20)

        return self.atributos

    def criar_maestria(self):
        nome_maestria = input('Nome maestria/classe :').upper()
        while True:
            modelo_definicao_at = int(input('ESCOLHA SE O SISTEMA VAI ESCOLHER SEUS ATRIBUTOS , OU VOCÊ MESMO IRÁ FAZER\n[1] SISTEMA ESCOLHE\n[2] VOCÊ ESCOLHE\nDecisão :'))
            if modelo_definicao_at == 1:
                self.randomizar_valores()
                break
            elif modelo_definicao_at == 2:
                self.atributos['vit'] = self.definir_valores('Vitalidade')
                self.atributos['forca'] = self.definir_valores('Forca')
                self.atributos['defesa'] = self.definir_valores('Defesa')
                self.atributos['inteligencia'] = self.definir_valores('Inteligencia')
                break

        nova_maestria = {
            'nome' : nome_maestria,
            'nivel' : self.nivel,
            'atributo' : self.atributos.copy()
        }
        self.maestrias.append(nova_maestria)
        print('CLASSE {} CRIADA COM SUCESSO !'.format(nome_maestria))
        self.salvar()

    def exibir_atributos(self):
            for maestria in self.maestrias:
                print(f'-- Atributos do {maestria['nome']} --')
                print(f"    VITALIDADE   : {maestria['atributo']['vit']}")
                print(f"    FORCA        : {maestria['atributo']['forca']}")
                print(f"    DEFESA       : {maestria['atributo']['defesa']}")
                print(f"    INTELIGENCIA : {maestria['atributo']['inteligencia']}\n")

    def salvar(self):
        with open('maestria.json','w') as arquivo_json:
            json.dump(self.maestrias,arquivo_json)

    def listar_todas_maestrias(self):
        for maestria in self.maestrias:
            print(f' * {maestria['nome']} LV {maestria['nivel']}')


            


SISTEMA = Modelo_maestria()

SISTEMA.listar_todas_maestrias()
SISTEMA.exibir_atributos()