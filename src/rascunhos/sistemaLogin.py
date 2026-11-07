import json
class Sistema:
    def __init__(self):
        self.meusUsuarios = []

    def registrarInformacoes(self):
        '''Exemplo'''
        nomeUsuario = str(input('Nome de Usuário :'))
        email = str(input('Email de contato :'))
        senha = str(input('Senha :'))

        novoUsuario = {
            'usuario' : nomeUsuario,
            'email' : email,
            'senha' : senha 
        }
        self.meusUsuarios.append(novoUsuario)
        self.salvamento()

    def salvamento(self):
        with open('usuarios.json') as arquivojson:
            json.dump(self.meusUsuarios,arquivojson)

    def logando(self):
        tentativas = 0
        usuario = input('Usuário :')
        senha = input('Senha :')
        if usuario == self.meusUsuarios['usuario'] and senha == self.meusUsuarios['senha']:
            print('Acessso permitido')
            print(f'Bem-vindo {usuario} !')
        else:
            tentativas += 1
            print(f'Usuário desconhecido / Tentativa {tentativas}')

    def menu(self):
        while True:
            print('[1] Cadastra')
            print('[2] Login')
            opcao = int(input('Escolha :'))
            if opcao == 1:
                self.registrarInformacoes()
            elif opcao == 2:
                self.logando()
            else:
                break
