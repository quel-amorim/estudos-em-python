from random import randint
import json
class Maestria:
    def __init__(self):
        self.nivel = 1
        self.minhas_maestrias = []
        self.atributos = {
            'vit' : 0,
            'forca' : 0,
            'defesa' : 0,
            'resistencia' : 0,
            'inteligencia' : 0
        }

    def pegar_valores(self,nome_atributo):
      while True:
            try:
                valor = int(input(f'{nome_atributo} ? '))

                if valor >= 0 and valor <= 20:
                    return valor

                print('O valor deve estar entre 0 e 20!')

            except ValueError:
                print('Digite apenas números!')


    def maestria_atributos(self):
        while True:
            try:
                opcoes_atributos = int(input('Quer definir seus atributos ou deixar o sistema gerar eles ?\n[1] SIM\n[2] NÃO\nEscolha :'))
                if opcoes_atributos == 1:
                    print('Randomizando os valores de atributos')
                    self.atributos['vit'] = randint(0,20)
                    self.atributos['forca'] = randint(0,20)
                    self.atributos['defesa'] = randint(0,20)
                    self.atributos['resistencia'] = randint(0,20)
                    self.atributos['inteligencia'] = randint(0,20)
                    break
                elif opcoes_atributos == 2:
                    print('Defina valores de 0 a 20')
                    self.atributos['vit'] = self.pegar_valores('Vitalidade')
                    self.atributos['forca'] = self.pegar_valores('Forca')
                    self.atributos['defesa'] = self.pegar_valores('Defesa')
                    self.atributos['resistencia'] = self.pegar_valores('Resistencia')
                    self.atributos['inteligencia'] = self.pegar_valores('Inteligencia')
                    break
                else:
                    print('Desconhecido volte ao começo !')
                    
            except ValueError:
                print('Apenas aceita 1 ou 2 , volte ao inicio !')

        return self.atributos


    def criar_maestria(self):
        nome_maestria = str(input('Nome para sua maestria :'))
        self.maestria_atributos()
        nova_maestria = {
            'nome' : nome_maestria,
            'nivel' : self.nivel,
            'status' : self.atributos.copy()
        }
        self.minhas_maestrias.append(nova_maestria)
        self.salvar()

    def salvar(self):
        with open('maestrias.json','w') as arquivo_json:
            json.dump(self.minhas_maestrias,arquivo_json)

    def carregar_dados(self):
        try:
            with open('maestrias.json', 'r') as arquivo_json:
                self.minhas_maestrias = json.load(arquivo_json)

        except (FileNotFoundError, json.JSONDecodeError):
            self.minhas_maestrias = []

    def exibir_maestrias(self):
        self.carregar_dados()

        print('------ Maestrias do Jogo ---------\n')

        for maestria in self.minhas_maestrias:
            print(f"{maestria['nome']} Nv {maestria['nivel']}")

    def remover_maestria(self):
        self.carregar_dados()
        self.exibir_maestrias()

        remover = input('Remover Maestria: ')

        for maestria in self.minhas_maestrias:
            if remover == maestria['nome']:
                self.minhas_maestrias.remove(maestria)
                print(f'Maestria {remover} removida com sucesso!')
                self.salvar()
                return

    print('Maestria não encontrada!')

    def menu_maestria(self):
        while True:
            print('[1] Nova Maestria')
            print('[2] Exibir Maestria')
            print('[3] Remover Maestria')

            try:
                opcao = int(input('\nEscolha: '))

                if opcao == 1:
                    self.criar_maestria()

                elif opcao == 2:
                    self.exibir_maestrias()

                elif opcao == 3:
                    self.remover_maestria()

                else:
                    print('Opção inválida!')
                    break

            except ValueError:
                print('Digite apenas números!')
        

teste = Maestria()

teste.menu_maestria()