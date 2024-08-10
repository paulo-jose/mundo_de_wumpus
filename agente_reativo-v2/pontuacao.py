class Pontuacao:
    def __init__(self):
        self.pontos = 0
        self.qnt_mortes_wumpus = 0

    def passo(self):
        self.pontos -= 1

    def morreu_wumpus_poco(self):
        self.pontos -= 1000

    def matou_wumpus(self):
        self.pontos += 1000
    
    def pegou_ouro(self):
        self.pontos += 1000
    
    def atirou_flecha(self):
        self.pontos -= 10
    
    def wumpus_morto(self):
        self.qnt_mortes_wumpus += 1



