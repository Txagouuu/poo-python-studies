class Musica:
    def __init__(self,nome= '',artista= '',duracao = 0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
    
    def __str__(self):
        return f'{self.nome} por {self.artista} - {self.duracao} minutos'


musica1 = Musica('Shape of You', 'Ed Sheeran', 3.53)
musica2 = Musica('Blinding Lights', 'The Weeknd', 3.20)
musica3 = Musica('Levitating', 'Dua Lipa', 3.23)


print(musica1)