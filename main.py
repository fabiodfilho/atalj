import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from biblioteca import BibliotecaAvancada
from livro import Livro

if __name__ == "__main__":
    biblioteca = BibliotecaAvancada()
    comando = 0

    while comando != 7:
        print("\n           ┏━━━━━━━━━━━━━┓")
        print("                 MENU     ")
        print("           ┗━━━━━━━━━━━━━┛" + "\n")
        print("[ 1 ] Cadastrar um novo livro")
        print("[ 2 ] Listar todos os livros")
        print("[ 3 ] Visualizar detalhes de um livro")
        print("[ 4 ] Remover um livro")
        print("[ 5 ] Visualizar livros por tema")
        print("[ 6 ] Recomendar livros por autor")
        print("[ 7 ] Sair do sistema\n")

        try:
            comando = int(input("▶ Escolha a opção que deseja acessar: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if comando == 1:
            titulo = input("\n▶ Digite o título do livro: ")
            autor = input("▶ Digite o autor do livro: ")
            try:
                ano = int(input("▶ Digite o ano de publicação do livro: "))
            except ValueError:
                print("Por favor, insira um ano válido.")
                continue
            tema = input("▶ Digite o tema do livro: ")
            livro = Livro(titulo, autor, ano, tema)
            biblioteca.cadastrar_livro(livro, tema)
            print("Livro cadastrado com sucesso!")

        elif comando == 2:
            biblioteca.listar_livros()

        elif comando == 3:
            try:
                index = int(input("▶ Digite o ID do livro para visualizar os detalhes: ")) - 1
                biblioteca.visualizar_livro(index)
            except ValueError:
                print("Por favor, insira um ID válido.")
            except IndexError:
                print("Índice fora do intervalo.")

        elif comando == 4:
            try:
                index = int(input("▶ Digite o ID do livro que deseja remover: ")) - 1
                biblioteca.remover_livro(index)
                print("Livro removido com sucesso!")
            except ValueError:
                print("Por favor, insira um ID válido.")
            except IndexError:
                print("Índice fora do intervalo.")

        elif comando == 5:
            tema = input("▶ Digite o tema para visualizar os livros: ")
            biblioteca.visualizar_tema(tema)

        elif comando == 6:
            autor = input("▶ Digite o nome do autor para recomendações: ")
            biblioteca.recomendar_por_autor(autor)

        elif comando == 7:
            print("Saindo do sistema. Até mais!")
            break

        else:
            print("Comando inválido. Tente novamente.")
