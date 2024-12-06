
from biblioteca import BibliotecaAvancada
from livro import Livro  

biblioteca = BibliotecaAvancada()


livro1 = Livro(titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien", ano=1954, tema="Fantasia")
livro2 = Livro(titulo="O Hobbit", autor="J.R.R. Tolkien", ano=1937, tema="Fantasia")
livro3 = Livro(titulo="1984", autor="George Orwell", ano=1949, tema="Distopia")
livro4 = Livro(titulo="A Revolução dos Bichos", autor="George Orwell", ano=1945, tema="Distopia")
livro5 = Livro(titulo="Harry Potter e a Pedra Filosofal", autor="J.K. Rowling", ano=1997, tema="Fantasia")


biblioteca.cadastrar_livro(livro1, tema="Fantasia")
biblioteca.cadastrar_livro(livro2, tema="Fantasia")
biblioteca.cadastrar_livro(livro3, tema="Distopia")
biblioteca.cadastrar_livro(livro4, tema="Distopia")
biblioteca.cadastrar_livro(livro5, tema="Fantasia")

print("Testando listar livros:")
biblioteca.listar_livros()

print("\nTestando visualizar livro por índice (índice 1):")
biblioteca.visualizar_livro(1)

print("\nTestando recomendar livros por autor (J.R.R. Tolkien):")
biblioteca.recomendar_por_autor("J.R.R. Tolkien")

print("\nTestando recomendar livros por tema (Fantasia):")
biblioteca.recomendar_livros("Fantasia")


print("\nTestando visualizar livros por tema (Distopia):")
biblioteca.visualizar_tema("Distopia")

print("\nTestando exibir temas cadastrados:")
biblioteca.exibir_temas()

