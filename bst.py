class BSTNode:
    def __init__(self, tema):
        self.tema = tema  # Tema é a chave do nó
        self.livros = []  # Lista de livros associados ao tema
        self.left = None  # Subárvore esquerda
        self.right = None  # Subárvore direita


class BST:
    def __init__(self):
        self.root = None

    def insert(self, livro):
        """Insere um livro na BST com base no tema."""
        if self.root is None:
            self.root = BSTNode(livro.tema)
            self.root.livros.append(livro)
        else:
            self._insert(self.root, livro)

    def _insert(self, current_node, livro):
        if livro.tema < current_node.tema:
            if current_node.left is None:
                current_node.left = BSTNode(livro.tema)
                current_node.left.livros.append(livro)
            else:
                self._insert(current_node.left, livro)
        elif livro.tema > current_node.tema:
            if current_node.right is None:
                current_node.right = BSTNode(livro.tema)
                current_node.right.livros.append(livro)
            else:
                self._insert(current_node.right, livro)
        else:
            # Se o tema já existe, adiciona o livro à lista de livros
            current_node.livros.append(livro)

    def search_by_tema(self, tema):
        """Busca livros por tema na BST."""
        return self._search(self.root, tema)

    def _search(self, current_node, tema):
        if current_node is None:
            return None
        if tema == current_node.tema:
            return current_node.livros
        elif tema < current_node.tema:
            return self._search(current_node.left, tema)
        else:
            return self._search(current_node.right, tema)

    def display(self):
        """Exibe todos os temas e seus livros."""
        self._display(self.root)

    def _display(self, current_node):
        if current_node:
            self._display(current_node.left)
            print(f"Tema: {current_node.tema}")
            for livro in current_node.livros:
                print(f"  ➥ {livro}")
            self._display(current_node.right)
