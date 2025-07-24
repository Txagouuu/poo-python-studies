from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []                                           #lista de restaurantes é um atributo de classe
    def __init__(self,nome,categoria,):                         #Padrao do python para construtor de classe são o self, mas pode ser qualquer nome
        self._nome = nome.title()                        #atributo nome do restaurante, converte o nome para título
        self._categoria = categoria.upper()                #atributo categoria do restaurante, converte a categoria para maiúsculas
        self._ativo = False                                     #atributo privado para indicar se o restaurante está ativo ou não
        self._avaliacao=[]
        Restaurante.restaurantes.append(self)                   #adiciona o objeto atual na lista de restaurantes
    
    def __str__(self):                                          #refencia do objeto atual de forma que possa ser escrita
        return f'{self._nome} - {self._categoria}'                #retorna uma string com o nome e a categoria do restaurante
    
    @classmethod
    def listar_restaurantes(cls):                                  #método de classe para listar todos os restaurantes | cls uma convencao sobre classmethod
        print(f'{'Restaurantes:'.ljust(25)} | {'categoia'.ljust(25)} | {'status'.ljust(25)} | {'avaliacao'.ljust(25)}' )                                      #imprime o título da lista de restaurantes
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)}')  #imprime o nome, categoria, status e média de avaliação de cada restaurante                                                  
    
    @property
    def ativo(self):                                            #método para retornar o nome do restaurante
        return '✅' if self._ativo else '❌'                   #retorna 'Ativo' se o restaurante estiver ativo, caso contrário retorna 'Inativo'
    
    def alternar_estado(self):                                  #método para OBEJTOS e para alternar o estado do restaurante
        self._ativo = not self._ativo                          #inverte o valor do atributo _ativo
        return self.ativo                                      #retorna o estado atual do restaurante

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)                   #cria um objeto avaliacao com o cliente e a nota
        self._avaliacao.append(avaliacao)                     #adiciona a avaliação à lista de avaliações do restaurante
                                                                #retorna o objeto avaliacao criado

    @property                                   #método para calcular a média das avaliações e para que seja possivel a leitura do atributo    
    def media_avaliacao(self):
        if not self._avaliacao:                               #verifica se a lista de avaliações está vazia
            return 0                                          #retorna 0 se não houver avaliações
        soma_das_notas = sum(Avaliacao._nota for Avaliacao in self._avaliacao)  #soma todas as notas das avaliações
        media = round(soma_das_notas / len(self._avaliacao),1)         #média das notas
        return media                                          #retorna a média das avaliações do restaurante
#restaurante_praca = Restaurante('praca', 'Comida Brasileira')   #cria um objeto restaurante_praca
#restaurante_praca.alternar_estado()                             #altera o estado do restaurante_praca para ativo
#restaurante_pizza = Restaurante('pizzaEXPRESS', 'Pizza')        #cria um objeto restaurante_pizza

#Restaurante.listar_restaurantes()                               #chama o método listar_restaurantes para listar todos os restaurantes

#print(restaurante_praca)                                       #imprime o objeto restaurante_praca
#print(restaurante_pizza)                                       #imprime o objeto restaurante_pizza  

#print(vars(restaurante_pizza))
#print(vars(restaurante_praca))
