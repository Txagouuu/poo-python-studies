class Restaurante:
    def __init__(self,nome,categoria,): #Padrao do python para construtor de classe são o self, mas pode ser qualquer nome
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    def __str__(self):                                          #refencia do objeto atual de forma que possa ser escrita
        return f'{self.Nome} - {self.categoria}'                #retorna uma string com o nome e a categoria do restaurante

restaurante_praca = Restaurante('praca', 'Comida Brasileira')
restaurante_pizza = Restaurante('pizzaEXPRESS', 'Pizza')


print(restaurante_praca)                                        #imprime o objeto restaurante_praca
print(restaurante_pizza)                                        #imprime o objeto restaurante_pizza  

#print(vars(restaurante_pizza))
#print(vars(restaurante_praca))
