
class Node:
    def __init__(self, tema, livro=None):
        self.tema = tema
        self.livros = [livro] if livro else []
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def is_empty(self):
        return self.raiz is None

    def inserir(self, tema, livro):
        """
        Insere um novo livro em um tema na árvore binária.
        """
        if self.is_empty():
            self.raiz = Node(tema, livro)
        else:
            self._inserir(self.raiz, tema, livro)

    def _inserir(self, node, tema, livro):
        """
        Função auxiliar recursiva para inserir o livro de acordo com o tema.
        """
        if tema < node.tema:
            if node.esquerda is None:
                node.esquerda = Node(tema, livro)
            else:
                self._inserir(node.esquerda, tema, livro)
        elif tema > node.tema:
            if node.direita is None:
                node.direita = Node(tema, livro)
            else:
                self._inserir(node.direita, tema, livro)
        else:
            # Caso o tema já exista, apenas adiciona o livro à lista de livros
            node.livros.append(livro)

    def buscar(self, tema):
        """
        Retorna uma lista de livros para um determinado tema.
        """
        if self.is_empty():
            return None

        return self._buscar(self.raiz, tema)

    def _buscar(self, node, tema):
        """
        Função auxiliar recursiva para buscar o tema na árvore.
        """
        if node is None:
            return None

        if tema < node.tema:
            return self._buscar(node.esquerda, tema)
        elif tema > node.tema:
            return self._buscar(node.direita, tema)
        else:
            return node.livros

    def exibir_em_ordem(self):
        """
        Exibe os livros em ordem alfabética pelo tema.
        """
        if self.is_empty():
            print("A árvore está vazia.")
        else:
            self._exibir_em_ordem(self.raiz)

    def _exibir_em_ordem(self, node):
        """
        Função auxiliar recursiva para exibir os livros em ordem.
        """
        if node:
            self._exibir_em_ordem(node.esquerda)
            print(f"Tema: {node.tema}")
            for livro in node.livros:
                print(f"  ➥ Título: {livro.titulo}")
                print(f"  ➥ Autor: {livro.autor}")
                print(f"  ➥ Ano de Lançamento: {livro.ano}")
            self._exibir_em_ordem(node.direita)

