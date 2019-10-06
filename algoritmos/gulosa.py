from time import time
from .helpers import *
from .node import No
from queue import PriorityQueue

def heuristica_gulosa(jogo):
    heuristica = 0
    objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    for i in range(3):
        for j in range(3):
            if (objetivo[i][j] != 0 and not objetivo[i][j] == jogo[i][j]):
                pos1, pos2 = get_posicao(objetivo[i][j], jogo)
                heuristica += (abs(pos1 - i) + abs(pos2 - j))
    return heuristica


def busca(jogo):
    inicio = time()

    borda = []
    borda.append((heuristica_gulosa(jogo.jogo), jogo))
    explorado = []
    nos_gerados = maxima_profundidade = 0

    while len(borda) != 0:
        borda.sort(key=lambda tupla: tupla[0], reverse=True)
        no = borda.pop()[1]
        explorado.append(no.jogo)

        if(verifica_venceu(no.jogo)):
            mostra_array(no.jogo)
            fim = time()
            tempo = fim - inicio
            ram = get_ram()
            return prepara_dic(no, "Gulosa", tempo, nos_gerados, maxima_profundidade, ram)
        
        filhos = gera_filhos(no)
        if maxima_profundidade != 100:
            for filho in filhos:
                if filho.jogo not in explorado:
                    nos_gerados += 1
                    maxima_profundidade = get_profundidade_maxima(
                        filho, maxima_profundidade)
                    borda.append((heuristica_gulosa(filho.jogo), filho))

    return False

