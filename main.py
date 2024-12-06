import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from biblioteca import BibliotecaAvancada
from livro import Livro

if __name__ == "__main__":
    biblioteca = BibliotecaAvancada()
    comando = 0

    while comando != 6:

        print("           ┏━━━━━━━━━━━━━┓")
        print("                 MENU     ")
        print("           ┗━━━━━━━━━━━━━┛" + "\n")
        print("[ 1 ] Cadastrar um novo livro")
        print("[ 2 ] Listar livros")
        print("[ 3 ] Visualizar temas e livros")
        print("[ 4 ] Recomendar livros por tema")
        print("[ 5 ] Remover um livro")
        print("[ 6 ] Sair do sistema" + "\n")

        comando = int(input("▶ Escolha a opção que deseja acessar: "))

        if comando == 1:
            titulo = input("\n▶ Digite o nome do livro: ")
            autor = input("▶ Digite o nome do autor do livro: ")
            ano = int(input("▶ Digite o ano de publicação do livro: "))
            tema = input("▶ Digite o tema do livro: ")
            livro = Livro(titulo, autor, ano, tema)
            biblioteca.livros.append(livro)

        elif comando == 2:
            biblioteca.exibir_livros()

        elif comando == 3:
            biblioteca.exibir_temas()

        elif comando == 4:
            tema = input("▶ Digite o tema para recomendação: ")
            biblioteca.recomendar_por_tema(tema)

        elif comando == 6:
            print("Saindo do sistema.")
            break

        else:
            print("Comando inválido.")
