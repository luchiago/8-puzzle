from time import time
from .helpers import *
from .node import No
from collections import deque

def busca(jogo):
    inicio = time()
    borda = deque([jogo])
    borda_com_jogos = deque([jogo.jogo])  
    explorado = []
    nos_gerados = maxima_profundidade = 0
    

    while (len(borda) != 0):
        no = borda.pop()
        jogo = borda_com_jogos.pop()
        explorado.append(jogo)

        if verifica_venceu(jogo):
            mostra_array(no.jogo)
            fim = time()
            tempo = fim - inicio
            ram = get_ram()
            return prepara_dic(no, "Largura", tempo, nos_gerados, maxima_profundidade, ram)

        filhos = gera_filhos(no)
        if maxima_profundidade != 100:
            for filho in filhos:
                nos_gerados += 1
                maxima_profundidade = get_profundidade_maxima(filho, maxima_profundidade)
                if filho.jogo not in explorado and filho.jogo not in borda_com_jogos:
                    borda.appendleft(filho)
                    borda_com_jogos.appendleft(filho.jogo)
    
    return False
