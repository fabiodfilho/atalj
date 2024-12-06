class Livro:
    def __init__(self, titulo, autor, ano, tema):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.tema = tema

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Tema: {self.tema}"
