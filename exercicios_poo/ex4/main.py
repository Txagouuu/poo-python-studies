from livros import Livro

def main():
    Livro.listar_livros()  # Chama o método da classe

if __name__ == "__main__":
    main()

livro_main1 = Livro("Python para Iniciantes", "Carlos Coder", 2021)
livro_main2 = Livro("Web Development Essentials", "Laura Developer", 2023)
