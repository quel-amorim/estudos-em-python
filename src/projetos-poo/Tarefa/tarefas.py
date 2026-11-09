from datetime import datetime , timedelta
class Tarefas:
    def __init__(self):
        self.minhasTarefas = []

    def criarTarefa(self):
        nomeTarefa = input('Nome da Tarefa :')
        modeloAtivacao = False # A tarefa vai está ativa / em aberto
        dataCriacao = datetime.now().strftime("%d/%m/%Y , %H %M")
        duracao = dataCriacao + timedelta(days=15)
        pontoTarefa = 10 # Quando concluir usuario ganha pontos por concluir a tarefa

        novaTarefa = {
            "tarefa" : nomeTarefa,
            "ativacao" : modeloAtivacao,
            "tempoCriado" : dataCriacao,
            "tempoLimite" : duracao,
            "pontos" : pontoTarefa
        }
        self.minhasTarefas.append(novaTarefa)

    def visualizar(self):
        for x in self.minhasTarefas:
            print(f'& {x["tarefa"]} Status {x["ativacao"]} -> Tarefa Criada : {x["tempoCriado"]} / Tempo Limite : {x["tempoLimite"]} || Pontos de Conclusão : {x["pontos"]}')

#Menu do Programa fora da classe
menu = Tarefas()
numero = len(menu.minhasTarefas)
while True:
    print(f'Tarefas Registradas : {numero}')
    print('  [1] Criar Tarefas')
    print('  [2] Visualizar Tarefas')
    opcao = int(input('Escolha :'))
    if opcao == 1:
        menu.criarTarefa()
    elif opcao == 2:
        menu.visualizar()
    else:
        break