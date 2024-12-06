class LinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def append(self, data):
        """
        Adiciona um novo nó ao final da lista.
        """
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def to_list(self):
        """
        Converte a lista encadeada em uma lista do Python.
        """
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return result

    def is_empty(self):
        """
        Verifica se a lista está vazia.
        """
        return self.head is None

    def remove_by_index(self, index):
        """
        Remove um nó da lista pelo índice.
        """
        if self.head is None:
            print("A lista está vazia.")
            return

        # Caso especial: remover o primeiro nó
        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for i in range(index - 1):
            if current is None:
                print("Índice fora do alcance.")
                return
            current = current.next

        if current is None or current.next is None:
            print("Índice fora do alcance.")
            return

        current.next = current.next.next

    def get_by_index(self, index):
        """
        Retorna o nó da lista pelo índice.
        """
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def __str__(self):
        """
        Retorna uma representação em string dos dados da lista encadeada.
        """
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(elements)
