from agendamento import Agenda
from random import randint,choice
from datetime import datetime
from string import ascii_uppercase , digits , punctuation
class Contato(Agenda):
    def __init__(self):
        super().__init__()

    def geradorNumero(self):
        ddds = [11, 12, 13, 19, 21, 22, 24, 27, 28, 31, 32, 41, 47, 48, 51, 61, 71, 81, 85]
        numeroDDD = choice(ddds)
        parte1 = randint(1000, 9999)
        parte2 = randint(1000, 9999)
        telefone = f"+55 ({numeroDDD}) 9{parte1}-{parte2}"
        return telefone


    def dataAdicao(self):
        dataAtual = datetime.now()
        data = dataAtual.strftime("%d/%m/%Y")
        return data

    def geradorIDEspecial(self,tamanho):
        numeros = digits
        letras = ascii_uppercase # Ex(A,B,C etc...)
        pontuacoes = punctuation # Ex (!,@,#,$ etc...)
        especial = letras + numeros + pontuacoes

        return "".join(choice(especial) for _ in range(tamanho))
        

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
    
    def remocaoContato(self):
            remover_especial = input('Informe Código especial para Remoção do contato :')
            for pessoa in self.contatos:
                 if remover_especial == pessoa['codigoespecial']:
                    remover = int(input(f"Deseja remover {pessoa['nome']} da sua lista de contatos?\n[1] SIM\n[2]NÃO\nESCOLHA :"))
                    if remover == 1:
                        self.contatos.remove(remover_especial)
                        self.salvamento_contato()
                    else:
                        print('Nada será feito !')