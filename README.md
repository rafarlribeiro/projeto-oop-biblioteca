# 📚 Projeto de Biblioteca em OOP

Este é um projeto simples de gerenciamento de uma biblioteca, desenvolvido em Python com uso de Programação Orientada a Objetos (OOP). O sistema permite adicionar, listar, buscar e remover livros por meio de um menu interativo no terminal.

---

## 🔧 Tecnologias e Recursos Utilizados

- **Python 3.x**
- Programação Orientada a Objetos (OOP)
  - Classes, atributos e métodos
  - Encapsulamento de dados
- F-strings para formatação de texto
- Listas e estruturas de controle (`if`, `for`, `while`)
- Organização modular em múltiplos arquivos (`livro.py`, `biblioteca.py`, `main.py`)
- Menu interativo em linha de comando

---

## 🚀 Funcionalidades

- ✅ Adicionar novos livros à biblioteca
- ✅ Remover livros pelo ISBN
- ✅ Listar todos os livros cadastrados
- ✅ Buscar livros por título (busca parcial, sem diferenciação entre maiúsculas e minúsculas)
- ✅ Interface via terminal com menu de opções

---

## 🛠️ Estrutura do Projeto

biblioteca-oop/
- ├── livro.py # Classe Livro com atributos e método str
- ├── biblioteca.py # Classe Biblioteca com métodos de manipulação da lista de livros
- └── main.py # Script principal com menu para o usuário

---

## 📦 Como Executar

1. Certifique-se de ter o Python 3 instalado no seu sistema.

2. Clone ou baixe este repositório.

3. No terminal, navegue até a pasta do projeto:
```bash
cd biblioteca-oop
```
Execute o script principal:
```bash
python main.py
```
Use o menu para interagir com a biblioteca:

==== MENU DA BIBLIOTECA ====
1. Adicionar livro
2. Listar livros
3. Buscar livro por título
4. Remover livro por ISBN
5. Sair

---

## 🔮 Possíveis Melhorias Futuras
- 💾 Persistência de dados com arquivos (JSON, CSV) ou banco de dados (SQLite)

- 🖼️ Interface gráfica com Tkinter, PyQt ou web (Flask/Django)

- 📱 Validações de entrada mais robustas (verificar tipos e campos obrigatórios)

- 📘 Ordenação de livros (por título, autor ou ano)

- 🔐 Controle de usuários (login/senha) para diferentes permissões

## Autor do projeto
Rafael da Silva Ribeiro

