class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def get_by_index(self, index):
        curr_node = self.head
        current_index = 0
        while curr_node:
            if current_index == index:
                return curr_node.data
            curr_node = curr_node.next
            current_index += 1
        return None

    def remove_by_index(self, index):
        if self.head is None:
            print("A lista está vazia.")
            return

        if index == 0:
            self.head = self.head.next
            print("Livro removido com sucesso.")
            return

        curr_node = self.head
        prev_node = None
        current_index = 0

        while curr_node and current_index != index:
            prev_node = curr_node
            curr_node = curr_node.next
            current_index += 1

        if curr_node is None:
            print("Índice inválido.")
        else:
            prev_node.next = curr_node.next


def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j].titulo > lista[j + 1].titulo:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

if __name__ == "__main__":
    biblioteca = LinkedList()

    comando = 0
    while comando != 5:

        print("           ┏━━━━━━━━━━━━━┓")
        print("                 MENU     ")
        print("           ┗━━━━━━━━━━━━━┛" + "\n")
        print("[ 1 ] Cadastrar um novo livro")
        print("[ 2 ] Listar livros")
        print("[ 3 ] Visualizar um livro específico")
        print("[ 4 ] Remover um livro")
        print("[ 5 ] Sair do sistema" + "\n")

        comando = int(input("▶ Escolha a opção que deseja acessar: "))

        if comando == 1:
            titulo = input("\n" + "▶ Digite o nome do livro: ")
            autor = input("▶ Digite o nome do autor do livro: ")
            ano = int(input("▶ Digite o ano de publicação do livro: "))
            livro = Livro(titulo, autor, ano)
            biblioteca.append(livro)

        elif comando == 2:
            try:
                lista_livros = []
                curr_node = biblioteca.head
                while curr_node:
                    lista_livros.append(curr_node.data)
                    curr_node = curr_node.next

                if not lista_livros:
                    raise ValueError("Lista vazia")

                bubble_sort(lista_livros)
                for index, livro in enumerate(lista_livros):
                    print(f"\nID do Livro: {index + 1}")
                    print(f"➥ Título: {livro.titulo}")
                    print(f"➥ Autor: {livro.autor}")
                    print(f"➥ Ano de lançamento: {livro.ano}\n")

            except ValueError as e:
                print(e)

        elif comando == 3:
            try:
                index = int(input("▶ Digite o índice do livro que deseja visualizar: ")) - 1
                livro = biblioteca.get_by_index(index)
                if livro:
                    print("\nDetalhes do Livro:")
                    print(f"➥ Título: {livro.titulo}")
                    print(f"➥ Autor: {livro.autor}")
                    print(f"➥ Ano de lançamento: {livro.ano}\n")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")

        elif comando == 4:
            try:
                index = int(input("▶ Digite o índice do livro que deseja remover: ")) - 1
                biblioteca.remove_by_index(index)
            except ValueError:
                print("Por favor, digite um número válido.")

        elif comando == 5:
            print("Saindo do sistema.")
            break

        else:
            print("Comando inválido.")

