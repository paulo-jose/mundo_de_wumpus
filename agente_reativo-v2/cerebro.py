class No:
    def __init__(self, posicao, probabilidade=0.0):
        self.posicao = posicao
        self.probabilidade = probabilidade
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

class Arvore:
    def __init__(self, linhas, colunas):
        self.raiz = No((0, 0), 0.0)
        self.linhas = linhas
        self.colunas = colunas
        self.nos = {(0, 0): self.raiz}
        self._construir_arvore()

    def _construir_arvore(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                posicao = (i, j)
                if posicao not in self.nos:
                    self.nos[posicao] = No(posicao, 0.5)
                no_atual = self.nos[posicao]
                
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < self.linhas and 0 <= nj < self.colunas:
                        posicao_adj = (ni, nj)
                        if posicao_adj not in self.nos:
                            self.nos[posicao_adj] = No(posicao_adj, 0.5)
                        no_filho = self.nos[posicao_adj]
                        no_atual.adicionar_filho(no_filho)

    def visitar_no(self, posicao):
        if posicao not in self.nos:
            print("Posição fora da matriz")
            return
        no = self.nos[posicao]
        print(f"Visitando nó na posição {posicao}, atualizando probabilidades...")
        probabilidade_atual = no.probabilidade
        for filho in no.filhos:
            filho.probabilidade = probabilidade_atual / len(no.filhos)

    def mostrar_probabilidades(self):
        for posicao in self.nos:
            no = self.nos[posicao]
            print(f"Posição: {no.posicao}, Probabilidade: {no.probabilidade}")

# Exemplo de uso
linhas, colunas = 4, 4
arvore = Arvore(linhas, colunas)

# Visitando a posição (1, 0) e atualizando probabilidades
arvore.visitar_no((1, 0))

# Mostrando as probabilidades
arvore.mostrar_probabilidades()
