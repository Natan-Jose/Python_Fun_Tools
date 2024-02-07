class ItemDeCompra:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
        self.comprado = False

class ListaDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, nome, quantidade):
        item = ItemDeCompra(nome, quantidade)
        self.itens.append(item)

    def remover_item(self, indice):
        if 0 <= indice < len(self.itens):
            del self.itens[indice]

    def marcar_como_comprado(self, indice):
        if 0 <= indice < len(self.itens):
            self.itens[indice].comprado = True

    def mostrar_lista(self):
        for i, item in enumerate(self.itens):
            status = "Comprado" if item.comprado else "Pendente"
            print(f"{i + 1}. {item.quantidade}x {item.nome} - {status}")

def main_lista_de_compras():
    lista_compras = ListaDeCompras()

    while True:
        print("\n=== Lista de Compras ===")
        lista_compras.mostrar_lista()

        opcao = input("\n1. Adicionar Item\n2. Remover Item\n3. Marcar como Comprado\n4. Sair\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do item: ")
            quantidade = int(input("Digite a quantidade: "))
            lista_compras.adicionar_item(nome, quantidade)
        elif opcao == "2":
            indice = int(input("Digite o número do item a ser removido: ")) - 1
            lista_compras.remover_item(indice)
        elif opcao == "3":
            indice = int(input("Digite o número do item comprado: ")) - 1
            lista_compras.marcar_como_comprado(indice)
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_lista_de_compras()
