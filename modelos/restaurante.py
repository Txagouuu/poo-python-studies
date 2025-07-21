class Restaurante:
    restaurantes = []                                           #lista de restaurantes é um atributo de classe
    def __init__(self,nome,categoria,):                         #Padrao do python para construtor de classe são o self, mas pode ser qualquer nome
        self.nome = nome
        self.categoria = categoria
        self._ativo = False                                     #atributo privado para indicar se o restaurante está ativo ou não
        Restaurante.restaurantes.append(self)                   #adiciona o objeto atual na lista de restaurantes
    def __str__(self):                                          #refencia do objeto atual de forma que possa ser escrita
        return f'{self.Nome} - {self.categoria}'                #retorna uma string com o nome e a categoria do restaurante
    def listar_restaurantes():                                  #método de classe para listar todos os restaurantes
        print(f'{'Restaurantes:'.ljust(25)} | {'categoia'.ljust(25)} | {'status'}')                                      #imprime o título da lista de restaurantes
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')                                                               
    @property
    def ativo(self):                                            #método para retornar o nome do restaurante
        return '✅' if self._ativo else '❌'                    #retorna 'Ativo' se o restaurante estiver ativo, caso contrário retorna 'Inativo'
restaurante_praca = Restaurante('praca', 'Comida Brasileira')   #cria um objeto restaurante_praca
restaurante_pizza = Restaurante('pizzaEXPRESS', 'Pizza')        #cria um objeto restaurante_pizza

Restaurante.listar_restaurantes()                               #chama o método listar_restaurantes para listar todos os restaurantes

#print(restaurante_praca)                                       #imprime o objeto restaurante_praca
#print(restaurante_pizza)                                       #imprime o objeto restaurante_pizza  

#print(vars(restaurante_pizza))
#print(vars(restaurante_praca))
