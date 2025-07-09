# main.py

from livro import Livro
from biblioteca import Biblioteca

def exibir_menu():
    print("\n==== MENU DA BIBLIOTECA ====")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Buscar livro por título")
    print("4. Remover livro por ISBN")
    print("5. Sair")

def main():
    biblioteca = Biblioteca()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano de publicação: ")
            isbn = input("ISBN: ")
            livro = Livro(titulo, autor, ano, isbn)
            biblioteca.adicionar_livro(livro)

        elif opcao == '2':
            print("\nLista de livros cadastrados:")
            biblioteca.listar_livros()

        elif opcao == '3':
            termo = input("Digite uma palavra para buscar no título: ")
            biblioteca.buscar_por_titulo(termo)

        elif opcao == '4':
            isbn = input("Digite o ISBN do livro a ser removido: ")
            biblioteca.remover_livro_por_isbn(isbn)

        elif opcao == '5':
            print("Saindo do programa... Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
