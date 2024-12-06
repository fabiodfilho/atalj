from linked_list import LinkedList
from arvore_binaria import ArvoreBinaria


class BibliotecaAvancada:
    def __init__(self):
        self.livros = LinkedList()  # Lista encadeada para armazenar livros
        self.arvore_temas = ArvoreBinaria()  # Árvore binária para armazenar livros por tema

    def cadastrar_livro(self, livro, tema):
        """
        Cadastra um livro na biblioteca e o associa a um tema na árvore binária.
        """
        self.livros.append(livro)  # Adiciona o livro à lista
        self.arvore_temas.inserir(tema, livro)  # Adiciona o livro à árvore binária de temas

    def listar_livros(self):
        """
        Lista todos os livros cadastrados na biblioteca em ordem alfabética pelo título.
        """
        if self.livros.is_empty():
            print("Não há livros cadastrados ainda :(")
            return

        lista_livros = self.livros.to_list()
        lista_livros.sort(key=lambda livro: livro.titulo)

        print("\nLista de Livros:")
        for index, livro in enumerate(lista_livros):
            print(f"ID: {index + 1}")
            print(f"➥ Título: {livro.titulo}")
            print(f"➥ Autor: {livro.autor}")
            print(f"➥ Ano de lançamento: {livro.ano}\n")

    def visualizar_livro(self, index):
        """
        Exibe os detalhes de um livro específico com base no índice.
        """
        if self.livros.is_empty():
            print("Não há livros cadastrados ainda :(")
            return

        livro = self.livros.get_by_index(index)
        if livro:
            print("\nDetalhes do Livro:")
            print(f"➥ Título: {livro.titulo}")
            print(f"➥ Autor: {livro.autor}")
            print(f"➥ Ano de lançamento: {livro.ano}\n")
        else:
            print("Índice inválido.")

    def remover_livro(self, index):
        """
        Remove um livro da biblioteca com base no índice.
        """
        if self.livros.is_empty():
            print("Não há livros cadastrados ainda :(")
            return

        self.livros.remove_by_index(index)

    def visualizar_tema(self, tema):
        """
        Exibe todos os livros de um determinado tema.
        """
        if self.arvore_temas.is_empty():
            print("Não há livros cadastrados ainda :(")
            return

        livros_tema = self.arvore_temas.buscar(tema)
        if livros_tema:
            print(f"\nLivros sobre o tema '{tema}':")
            for livro in livros_tema:
                print(f"➥ Título: {livro.titulo}")
                print(f"➥ Autor: {livro.autor}")
                print(f"➥ Ano de lançamento: {livro.ano}\n")
        else:
            print(f"Não há livros cadastrados no tema '{tema}'.")

    def recomendar_livros(self, tema):
        """
        Recomenda livros baseados em um tema específico.
        """
        if self.arvore_temas.is_empty():
            print("Não há livros cadastrados ainda :(")
            return

        livros_recomendados = self.arvore_temas.buscar(tema)
        if livros_recomendados:
            print(f"\nRecomendações de livros sobre o tema '{tema}':")
            for livro in livros_recomendados:
                print(f"➥ Título: {livro.titulo}")
                print(f"➥ Autor: {livro.autor}")
                print(f"➥ Ano de lançamento: {livro.ano}\n")
        else:
            print(f"Não foi possível encontrar recomendações para o tema '{tema}'.")

    def exibir_livros(self):
        """
        Exibe todos os livros cadastrados na biblioteca.
        """
        if self.livros.is_empty():
            print("Não há livros cadastrados ainda :(")
        else:
            lista_livros = self.livros.to_list()
            lista_livros.sort(key=lambda livro: livro.titulo)
            print("\nLivros cadastrados:")
            for livro in lista_livros:
                print(f"➥ Título: {livro.titulo} | Autor: {livro.autor} | Ano: {livro.ano}")

    def exibir_temas(self):
        """
        Exibe todos os temas disponíveis na biblioteca.
        """
        temas = set()
        if not self.arvore_temas.is_empty():
            livros = self.arvore_temas.exibir_em_ordem()  
            for livro in livros:
                temas.add(livro.tema)
        
        if temas:
            print("Temas disponíveis:")
            for tema in temas:
                print(f"- {tema}")
        else:
            print("Não há temas cadastrados ainda :(")

    def recomendar_por_tema(self, tema):
        """
        Recomenda livros com base em um tema específico.
        """
        if not self.arvore_temas.is_empty():
            livros = self.arvore_temas.exibir_em_ordem()  # Supondo que o método de exibição em ordem retorne os livros
            recomendados = [livro for livro in livros if livro.tema == tema]
        else:
            recomendados = []

        if not recomendados:
            print("Biblioteca vazia ou nenhum livro encontrado para este tema.")
        else:
            print(f"Recomendações de livros sobre o tema '{tema}':")
            for livro in recomendados:
                print(f"➥ Título: {livro.titulo} | Autor: {livro.autor} | Ano: {livro.ano}")
