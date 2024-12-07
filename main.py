import sys
import os
from bst import BST
from livro import Livro
from linked_list import LinkedList
from biblioteca import BibliotecaAvancada


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def obter_input_com_validacao(prompt, tipo, valida_ano=False):
    while True:
        try:
            entrada = input(prompt)
            if tipo == "int":
                entrada = int(entrada)
                if valida_ano and (entrada < 1000 or entrada > 2100):
                    print("Ano inválido. Por favor, insira um ano válido entre 1000 e 2100.")
                    continue
            elif tipo == "str" and not entrada.strip():
                print("Entrada não pode ser vazia. Tente novamente.")
                continue
            return entrada
        except ValueError:
            print(f"Por favor, insira um valor válido para {tipo}.")

def main():
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

        comando = obter_input_com_validacao("▶ Escolha a opção que deseja acessar: ", "int")

        if comando == 1:
            titulo = obter_input_com_validacao("\n▶ Digite o título do livro: ", "str")
            autor = obter_input_com_validacao("▶ Digite o autor do livro: ", "str")
            ano = obter_input_com_validacao("▶ Digite o ano de publicação do livro: ", "int", valida_ano=True)
            tema = obter_input_com_validacao("▶ Digite o tema do livro: ", "str")
            livro = Livro(titulo, autor, ano, tema)
            biblioteca.cadastrar_livro(livro, tema)
            print("Livro cadastrado com sucesso!")

        elif comando == 2:
            biblioteca.listar_livros()

        elif comando == 3:
            index = obter_input_com_validacao("▶ Digite o ID do livro para visualizar os detalhes: ", "int")
            try:
                biblioteca.visualizar_livro(index - 1)
            except IndexError:
                print("Índice fora do intervalo.")

        elif comando == 4:
            index = obter_input_com_validacao("▶ Digite o ID do livro que deseja remover: ", "int")
            try:
                biblioteca.remover_livro(index - 1)
                print("Livro removido com sucesso!")
            except IndexError:
                print("Índice fora do intervalo.")

        elif comando == 5:
            tema = obter_input_com_validacao("▶ Digite o tema para visualizar os livros: ", "str")
            biblioteca.visualizar_tema(tema)

        elif comando == 6:
            autor = obter_input_com_validacao("▶ Digite o nome do autor para recomendações: ", "str")
            biblioteca.recomendar_por_autor(autor)

        elif comando == 7:
            print("Saindo do sistema. Até mais!")

        else:
            print("Comando inválido. Tente novamente.")

if __name__ == "__main__":
    main()
