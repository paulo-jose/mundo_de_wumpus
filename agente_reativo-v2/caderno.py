class Caderno:

    def __init__(self):
        self.caderno = {}
    
    def get_caderno(self):
        return self.caderno
    
    def adicionar_anotacao(self, posicao, lista_posicoes):
        if posicao not in self.caderno:
            self.caderno[posicao] = lista_posicoes
        else:
            print("Posição já anotada")

    def verificar_caderno(self, posicao):
        for posicoes in self.caderno.values():
            if posicao in posicoes:
                posicoes.remove(posicao)
                return posicoes
        return False
