from datetime import datetime , timedelta
class Tarefas:
    def __init__(self):
        self.minhasTarefas = []

    def criarTarefa(self):
        nomeTarefa = input('Nome da Tarefa :')
        modeloAtivacao = False # A tarefa vai está ativa / em aberto
        if modeloAtivacao == False:
            status = "Em Aberto"
        elif modeloAtivacao == True:
            status = "Concluido"
        
        dataCriacao = datetime.now()
        duracao = dataCriacao + timedelta(days=15)
        pontoTarefa = 10 # Quando concluir usuario ganha pontos por concluir a tarefa

        novaTarefa = {
            "tarefa" : nomeTarefa,
            "ativacao" : status,
            "tempoCriado" : dataCriacao.strftime("%d/%m/%Y , %H %M"),
            "tempoLimite" : duracao.strftime("%d/%m/%Y , %H:%M"),
            "pontos" : pontoTarefa
        }
        self.minhasTarefas.append(novaTarefa)

    def visualizar(self):
        for x in self.minhasTarefas:
            print(f'& {x["tarefa"]} Status {x["ativacao"]} -> Tarefa Criada : {x["tempoCriado"]} / Tempo Limite : {x["tempoLimite"]} || Pontos de Conclusão : {x["pontos"]}')

#Menu do Programa fora da classe
menu = Tarefas()
while True:
    print(f'Tarefas Registradas : {len(menu.minhasTarefas)}')
    print('  [1] Criar Tarefas')
    print('  [2] Visualizar Tarefas')
    opcao = int(input('Escolha :'))
    if opcao == 1:
        menu.criarTarefa()
    elif opcao == 2:
        menu.visualizar()
    else:
        break