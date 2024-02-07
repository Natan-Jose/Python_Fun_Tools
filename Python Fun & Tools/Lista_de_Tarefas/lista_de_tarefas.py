class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        tarefa = Tarefa(descricao)
        self.tarefas.append(tarefa)

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]

    def marcar_como_concluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluida = True

    def mostrar_tarefas(self):
        for i, tarefa in enumerate(self.tarefas):
            status = "Concluída" if tarefa.concluida else "Pendente"
            print(f"{i + 1}. {tarefa.descricao} - {status}")

def main_lista_de_tarefas():
    lista_tarefas = ListaDeTarefas()

    while True:
        print("\n=== Lista de Tarefas ===")
        lista_tarefas.mostrar_tarefas()

        opcao = input("\n1. Adicionar Tarefa\n2. Remover Tarefa\n3. Marcar como Concluída\n4. Sair\nEscolha uma opção: ")

        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ")
            lista_tarefas.adicionar_tarefa(descricao)
        elif opcao == "2":
            indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
            lista_tarefas.remover_tarefa(indice)
        elif opcao == "3":
            indice = int(input("Digite o número da tarefa concluída: ")) - 1
            lista_tarefas.marcar_como_concluida(indice)
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_lista_de_tarefas()
