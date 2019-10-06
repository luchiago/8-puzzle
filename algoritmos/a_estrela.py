from time import time
from .helpers import *
from .node import No

def heuristica_manhattan(jogo):
        heuristica = distancia = 0
        count = 1
        for i in range(3):
            for j in range(3):
                indice = jogo[i][j] - 1
                if indice == -1:
                    distancia = (2-i)+(2-j)
                else:
                    distancia = abs(i - (indice/3)) + abs(j - (indice % 3))
                heuristica += distancia
                count += 1
        return heuristica

def busca(jogo):
    inicio = time()

    borda = []
    borda.append((heuristica_manhattan(jogo.jogo), jogo)) 
    explorado = []
    nos_gerados = maxima_profundidade = 0

    while (len(borda) != 0):
        borda.sort(key=lambda tupla: tupla[0], reverse=True)
        no = borda.pop()[1]
        explorado.append(no.jogo)

        if(verifica_venceu(no.jogo)):
            mostra_array(no.jogo)
            fim = time()
            tempo = fim - inicio
            ram = get_ram()
            return prepara_dic(no, "A*", tempo, nos_gerados, maxima_profundidade, ram)
    
        filhos = gera_filhos(no)
        if maxima_profundidade != 100:
            for filho in filhos:
                if filho.jogo not in explorado:
                    nos_gerados += 1
                    maxima_profundidade = get_profundidade_maxima(
                        filho, maxima_profundidade)
                    borda.append((heuristica_manhattan(filho.jogo) + filho.custo, filho))
                    
    return False
