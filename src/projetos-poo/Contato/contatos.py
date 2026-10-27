from random import randint
from datetime import datetime
class Agenda:
    def __init__(self):
        self.contatosTelefonico = []
        self.proximoID = 1

    def gerandoTelefone(self):
        ddd = randint(11, 99)
        n1 = randint(1000, 9999)
        n2 = randint(1000, 9999)

        return f'+55 ({ddd}) 9{n1}-{n2}'

    def registraData(self):
        return datetime.now().strftime('%d/%m/%Y, %H:%M')

    def adicionarAgenda(self, nomeContato):
        nomeContato = nomeContato.strip()

        if not nomeContato:
            print("O nome não pode ficar vazio!")
            return

        novoContato = {
            'id': self.proximoID,
            'nome': nomeContato,
            'telefone': self.gerandoTelefone(),
            'registro': self.registraData()
        }

        self.contatosTelefonico.append(novoContato)
        self.proximoID += 1

        print(f"Contato cadastrado! ID: {novoContato['id']}")

    def exibirContato(self):
        if not self.contatosTelefonico:
            print("Nenhum contato cadastrado!")
            return

        for contato in self.contatosTelefonico:
            print(
                f"ID: {contato['id']} | "
                f"Nome: {contato['nome']} | "
                f"Telefone: {contato['telefone']} | "
                f"Registro: {contato['registro']}"
            )

    def editar(self, editarID):
        for contato in self.contatosTelefonico:
            if contato['id'] == editarID:
                print(f"\nContato encontrado: {contato['nome']}")
                print("[1] Editar nome")
                print("[2] Editar telefone")
                print("[3] Editar nome e telefone")

                opcao = input("O que deseja editar? ")

                if opcao == '1':
                    novoNome = input("Novo nome: ").strip()

                    if not novoNome:
                        print("O nome não pode ficar vazio!")
                        return

                    contato['nome'] = novoNome

                elif opcao == '2':
                    contato['telefone'] = self.gerandoTelefone()

                elif opcao == '3':
                    novoNome = input("Novo nome: ").strip()

                    if not novoNome:
                        print("O nome não pode ficar vazio!")
                        return

                    contato['nome'] = novoNome
                    contato['telefone'] = self.gerandoTelefone()

                else:
                    print("Opção inválida!")
                    return

                contato['registro'] = self.registraData()
                print("Contato atualizado com sucesso!")
                return

        print("Contato não encontrado!")


a1 = Agenda()

while True:
    print("\n===== AGENDA DE CONTATOS =====")
    print("[1] Adicionar contato")
    print("[2] Exibir contatos")
    print("[3] Editar contato")
    print("[4] Sair")

    opcao = input("Decisão: ").strip()

    if opcao == '1':
        nomeContato = input("Nome do contato: ")
        a1.adicionarAgenda(nomeContato)

    elif opcao == '2':
        a1.exibirContato()

    elif opcao == '3':
        a1.exibirContato()

        if a1.contatosTelefonico:
            try:
                editarID = int(
                    input("Digite o ID do contato que deseja editar: ")
                )
                a1.editar(editarID)

            except ValueError:
                print("Digite um ID numérico válido!")

    elif opcao == '4':
        print("Encerrando a agenda...")
        break

    else:
        print("Opção inválida!")
