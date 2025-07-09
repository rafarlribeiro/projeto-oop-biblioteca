# biblioteca.py

from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'Livro "{livro.titulo}" adicionado com sucesso!')

    def remover_livro_por_isbn(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                self.livros.remove(livro)
                print(f'Livro com ISBN {isbn} removido com sucesso!')
                return
        print(f'Livro com ISBN {isbn} não encontrado.')

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
        else:
            for livro in self.livros:
                print(livro)
                print('-' * 40)

    def buscar_por_titulo(self, palavra_chave):
        encontrados = [
            livro for livro in self.livros
            if palavra_chave.lower() in livro.titulo.lower()
        ]
        if encontrados:
            print(f"Livros encontrados com '{palavra_chave}' no título:")
            for livro in encontrados:
                print(livro)
                print('-' * 40)
        else:
            print(f"Nenhum livro encontrado com '{palavra_chave}' no título.")
