from agendamento import Agenda
from random import randint,choice
from datetime import datetime
from string import ascii_uppercase , digits
class Contato(Agenda):
    def __init__(self):
        super().__init__()

    def geradorNumero(self):
        ddds = [11, 12, 13, 19, 21, 22, 24, 27, 28, 31, 32, 41, 47, 48, 51, 61, 71, 81, 85]
        numeroDDD = choice(ddds)
        parte1 = randint(1000, 9999)
        parte2 = randint(1000, 9999)
        return f"+55 ({numeroDDD}) 9{parte1}-{parte2}"


    def dataAdicao(self):
        return datetime.now().strftime("%d/%m/%Y")

    def geradorIDEspecial(self, tamanho=8):
        caracteres = ascii_uppercase + digits
        while True:
            codigo = "".join(choice(caracteres) for _ in range(tamanho))
            if not any(contato["codigoespecial"] == codigo for contato in self.contatos):
                return codigo
        

    def criarContato(self):
        nome_contato = input('Nome do Contato:')
        contato = {
           'codigoespecial' : self.geradorIDEspecial(7),
            'nome' : nome_contato,
            'telefone' : self.geradorNumero(),
            'adicao' : self.dataAdicao()
        }
        self.contatos.append(contato)
        self.salvamento_contato()
        print(f"O {contato['nome']} foi adicionado com sucesso , código especial é {contato['codigoespecial']}")
    