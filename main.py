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

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

if __name__ == "__main__":
    biblioteca = LinkedList()  # Usando lista encadeada

    while True:
        comando = input("Digite um comando (adicionar, listar, sair): ")
        if comando == "adicionar":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))
            livro = Livro(titulo, autor, ano)
            biblioteca.append(livro)
        elif comando == "listar":
            # Ordenar a lista antes de imprimir
            lista_livros = []
            curr_node = biblioteca.head
            while curr_node:
                lista_livros.append(curr_node.data)
                curr_node = curr_node.next
            bubble_sort(lista_livros)
            for livro in lista_livros:
                print(livro)
        elif comando == "sair":
            break
        else:
            print("Comando inválido.")