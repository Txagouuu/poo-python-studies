class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponibilidade = True
        Livro.livros.append(self)
    
    def __str__(self):
      return f"Livro: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao}"
        
    def emprestar(self):
        self.disponibilidade = False
    
    @classmethod
    def listar_livros(cls):
        print(f'{'Titulo:'.ljust(25)} | {'autor'.ljust(25)} | {'ano de Publicacao'.ljust(25)} | {'Disponibilidade'.ljust(25)}' )                                      #imprime o título da lista de restaurantes
        for livros in cls.livros:
            print(f'{livros.titulo.ljust(25)} | {livros.autor.ljust(25)} | {str(livros.ano_publicacao).ljust(25)} | {str(livros.disponibilidade).ljust(25)}')  #imprime o nome, categoria, status e média de avaliação de cada livros
    
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponibilidade]
        return livros_disponiveis
        




livro1 = Livro("Aprendendo Python", "John Doe", 2022)
livro2 = Livro("Data Science Fundamentals", "Jane Smith", 2020)

livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)

#print(f"Antes de emprestar: Livro disponível? {livro3.disponibilidade}") #Disponivel
livro3.emprestar()
#print(f"Depois de emprestar: Livro disponível? {livro3.disponibilidade}") #Indisponivel

livros = [livro1, livro2, livro3]