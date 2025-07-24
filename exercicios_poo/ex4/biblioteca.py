from livros import Livro

livro_biblioteca = Livro("Biblioteca Python", "Autor Exemplo", 2023)
livro_biblioteca.emprestar()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponibilidade}")

ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")