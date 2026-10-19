from random import randint
from datetime import datetime
from gerenciamento import Armazenamento
class Contato(Armazenamento):
    def __init__(self):
        super().__init__()

    def gerandoTelefone(self):
            ddd = randint(11 , 99)
            p1 = randint(1 , 1000)
            p2 = randint(1, 1000)
            return f"+55 ({ddd}) 9 {p1} - {p2}"

    def dataNoticacao(self):
         dataAtual = datetime.now().strftime("%d/%m/%Y")
         return dataAtual
    
    def adicionado(self):
        nomeContato = input("Nome do Contato :")
        novoContato = {
             "nome" : nomeContato,
             "telefone" : self.gerandoTelefone(),
             "data" : self.dataNoticacao()
        }

        self.listaContatos.append(novoContato)
        self.salvamentoContato()
        print(f"{nomeContato} foi adicionado na sua lista telefonica !")

    def editarContato(self):
        pass

    def buscarContato(self):
        pass

    def listarTodos(self):
        pass

    def removerContato(self):
        pass