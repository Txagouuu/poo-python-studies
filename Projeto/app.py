from modelos.restaurante import Restaurante
from modelos.avaliacao import Avaliacao


restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliacao('gui', 10)
restaurante_praca.receber_avaliacao('tiago', 9)
restaurante_praca.receber_avaliacao('joao', 2)



def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()