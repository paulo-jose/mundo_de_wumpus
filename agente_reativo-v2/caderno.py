class Caderno:

    def __init__(self):
        self.caderno = {}
    
    def get_caderno(self):
        return self.caderno
    
    def get_chaves(self):
        pass

    def get_valores(self):
        valores = []

        for chave, lista_valores in self.caderno.items():  # Itera sobre chaves e listas de valores
            for valor in lista_valores:  # Itera sobre cada valor na lista
                valores.append(valor)  # Adiciona o valor à lista
        
        return valores

    
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
