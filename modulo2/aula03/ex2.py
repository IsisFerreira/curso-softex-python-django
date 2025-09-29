class Midia:
    def __init__(self, titulo, duracao_seg):
        self.titulo = titulo
        self.duracao_seg = duracao_seg

    def exibir(self):
        print(f'\nO titulo da midia é {self.titulo} e a duração é {self.duracao_seg} segundos')

class Musica(Midia):
    def __init__(self, titulo, duracao_seg, artista):
        super().__init__(titulo, duracao_seg, artista)
        self.artista = artista
    
    def exibir(self):
        print(f'\nO titulo da musica é {self.titulo} e a duração é {self.duracao_seg} segundos e o artista que a criou foi {self.artista}')

class Video(Midia):
    def __init__(self, titulo, duracao_seg, resolucao):
        super().__init__(titulo, duracao_seg, resolucao)
        self.resolucao = resolucao

    def exibir(self):
        print(f'\nO titulo do video é {self.titulo} e a duração é {self.duracao_seg} segundos e o resolucao é {self.resolucao}')

musica = Musica("Tu", 156, "Katy")
video = Video("Tutorial python 2025", 1800, "1500x1600")

dicionario_midia = {"musicas":[], "videos":[]}
dicionario_midia["musicas"].append(musica)
dicionario_midia["videos"].append(video)

print(dicionario_midia)

for item in dicionario_midia.values():
    for midia in item:
        midia.exibir()