# Projeto de Biblioteca em Python com Árvore Binária 

Este projeto implementa um sistema de gerenciamento de livros utilizando uma **lista encadeada** para armazenar os livros e uma **árvore binária** para organizar e gerenciar os temas literários. O sistema permite cadastrar, listar, remover e recomendar livros com base em diferentes critérios, utilizando as vantagens das duas estruturas de dados.

## Estruturas de Dados Utilizadas

### Lista Encadeada 📝

A **lista encadeada** é utilizada para gerenciar os livros. Ela oferece:
- **Flexibilidade**: Permite inserções e remoções eficientes de livros em qualquer posição da lista.
- **Gerenciamento dinâmico de memória**: A alocação de memória é feita individualmente para cada nó, facilitando a adição e remoção de livros.

### Árvore Binária 🌲🌲

A **árvore binária** organiza os livros por temas e oferece:
- **Busca rápida por tema**: A árvore binária permite buscar temas de maneira eficiente.
- **Inserção dinâmica**: Permite adicionar novos temas ou livros sem a necessidade de reorganizar dados.
- **Exibição ordenada**: A árvore pode ser percorrida em ordem (in-order traversal), exibindo os temas e livros ordenados alfabeticamente.

## Classes 

### Classe Livro 📖

A classe **Livro** representa um livro na biblioteca, com os seguintes atributos:
- `titulo`: Título do livro (string).
- `autor`: Autor do livro (string).
- `ano`: Ano de publicação do livro (inteiro).
- `tema`: Gênero literário do livro (string).

A classe também implementa o método `__str__` para exibir os atributos de forma formatada.

### Classe Node 🪢

A classe **Node** representa um nó na árvore binária. Ela possui:
- `tema`: O tema ou gênero literário associado ao nó.
- `livros`: Lista de livros associados a esse tema.
- `esquerda`: Nó filho esquerdo.
- `direita`: Nó filho direito.

### Classe ArvoreBinaria 🌲🌲

A classe **ArvoreBinaria** gerencia os temas dos livros e oferece os seguintes métodos:
- `is_empty()`: Verifica se a árvore está vazia.
- `inserir(tema, livro)`: Insere um livro em um tema. Se o tema não existir, cria um novo nó.
- `buscar(tema)`: Busca um tema na árvore e retorna a lista de livros associados.
- `exibir_em_ordem()`: Exibe os temas e livros ordenados alfabeticamente.

## Funcionalidades

O sistema oferece um menu interativo com as seguintes opções:

1. **Cadastrar um novo livro**: Insere um novo livro na árvore binária, associando-o a um tema.
2. **Listar livros**: Exibe os livros associados a um tema, ordenados por ano de publicação.
3. **Visualizar um livro específico**: Exibe os detalhes de um livro, dado o tema e o índice do livro.
4. **Remover um livro**: Permite remover um livro pelo índice.
5. **Exibir todos os temas e livros cadastrados**: Exibe todos os temas e seus respectivos livros, ordenados por tema.
6. **Recomendar livros por autor**: Exibe livros escritos por um autor específico.
7. **Sair do sistema**: Encerra a execução do sistema de gerenciamento de livros.

## Como Usar

1. Clone o repositório para sua máquina local.
2. Execute o código Python.
3. Use o menu interativo para cadastrar, listar, remover ou recomendar livros.

## Desenvolvedores


- `Fábio Filho`,
- `Renata Mantovani`,
- `Jéssica Vitória`,
- `Evelyn Julia`,
- `Diogo Fernando`. 


