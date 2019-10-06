from time import time
from .helpers import *


def busca(jogo):
    maxima_profundidade = 0
    borda = [jogo]
    borda_com_jogos =[jogo.jogo] 
    explorado = []
    nos_gerados = maxima_profundidade = 0
    inicio = time()

    while (len(borda) != 0):
        no = borda.pop()
        jogo = borda_com_jogos.pop()
        mostra_array(jogo)
        explorado.append(jogo)

        if verifica_venceu(jogo):
            mostra_array(filho.jogo)
            fim = time()
            tempo = fim - inicio
            ram = get_ram()
            return prepara_dic(no, "Profundidade", tempo, nos_gerados, maxima_profundidade, ram)
        
        maxima_profundidade = get_profundidade_maxima(
            no, maxima_profundidade)

        filhos = reversed(gera_filhos(no))
        for filho in filhos:
            nos_gerados += 1
            if filho.jogo not in explorado and filho.jogo not in borda_com_jogos:
                if verifica_venceu(filho.jogo):
                    mostra_array(filho.jogo)
                    fim = time()
                    tempo = fim - inicio
                    ram = get_ram()
                    return prepara_dic(filho, "Profundidade", tempo, nos_gerados, maxima_profundidade, ram)
                borda.append(filho)
                borda_com_jogos.append(filho.jogo)

    return False
