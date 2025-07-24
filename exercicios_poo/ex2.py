class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade

class Pessoa:
    def __init__(self,nome = '',idade= '',profissao= ''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Ola, meu nome é {self.nome}, sou {self.profissao} e tenho {self.idade} anos.'
        else:
            return f'Ola, meu nome é {self.nome} e tenho {self.idade} anos.'
        
    def aniversario(self):
        self.idade += 1
    
livro1 = Livro('1984', 'George Orwell', 328)
livro2 = Livro('To Kill a Mockingbird', 'Harper Lee', 281)
livro3 = Livro('The Great Gatsby', 'F. Scott Fitzgerald', 180)
print(livro1)