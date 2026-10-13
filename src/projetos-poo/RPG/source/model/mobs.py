from gerenciamentoControle import Gerenciamento
from random import randint,choice

#Observação ao uso dos atributos será randomizado porque sim  :)
class Monstro(Gerenciamento):
    def __init__(self):
        super().__init__()
        self.carregamentoMobs()

    def criarMob(self):
        sugestoesMobs = ['Zumbi','Vampiro','Demonio','Anjo','Lobinho','MIMADO']
        sugestoesElementos = ['Fogo', 'Água', 'Terra', 'Ar']
        mob = choice(sugestoesMobs)
        elemento = choice(sugestoesElementos)
        nivel = 1
        atributos = {
            'vitalidade' : randint(1,20),
            'forca' : randint(1,20),
            'defesa' : randint(1,20),
            'agilidade' : randint(1,20),
            'inteligencia' :randint(1,20),
        }

        novoMob = {
            'nome' : mob,
            'elemento' : elemento,
            'nivel' : nivel,
            'atributos' : atributos.copy(),
        }
        self.mobs.append(novoMob)
        self.salvamentoMobs()
        print(mob , " foi adicionado a lista de mobs !")

    def exibirMob(self):
        print('---- Mobs do Sistema ----\n')
        for mob in self.mobs:
            print(f' * {mob['nome']} Nv {mob['nivel']} -> Elemento {mob['elemento']}\n')

    def menuMob(self):
        while True:
            print('[1] Criar Mob')
            print('[2] Mostrar todos os mobs')
            try:
                escolha = int(input('Escolha :'))

            except ValueError:
                print('Apenas números !')
                continue

            if escolha == 1:
                self.criarMob()
            elif escolha == 2:
                self.exibirMob()
                break
            else:
                continue

m = Monstro()

m.menuMob()
