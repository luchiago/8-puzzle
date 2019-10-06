"""
Esse arquivo vai conter algumas funções 
úteis para todos os algoritmos
"""
from copy import deepcopy
from .node import No
import sys

def transforma_em_array(jogo):
    novo = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(int(jogo[i * 3 + j]))
        novo.append(linha)
    return novo

def verifica_venceu(jogo):
    #Jogo é um array bidimensional
    estado_objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    for i in range(3):
        for j in range(3):
            if jogo[i][j] != estado_objetivo[i][j]:
                return False
    return True

def get_posicao_vazio(jogo):
    #Jogo é um array bidimensional
    #Retorna a posição linha, coluna da posição vazia
    espaço_vazio = 0
    for i in range(3):
        for j in range(3):
            if jogo[i][j] == espaço_vazio:
                return i, j

def mostra_array(jogo):
    for i in range(3):
        for j in range(3):
            print(jogo[i][j], end=' ')
        print('')

def gera_filhos(jogo):
    #Jogo é um no
    #Retorna uma lista com todos as jogadas possiveis
    i, j = get_posicao_vazio(jogo.jogo)
    possibilidades = []
    limite_superior = limite_esquerda = 0
    limite_inferior = limite_direita = 2
    # mostra_array(jogo.jogo)

    #Mover para a esquerda
    if j > limite_esquerda:
        novo = deepcopy(jogo.jogo)
        novo[i][j - 1], novo[i][j] = novo[i][j], novo[i][j - 1]
        novo = No(novo, 'Esquerda', jogo, jogo.custo + 1)
        # mostra_array(novo.jogo)
        possibilidades.append(novo)

    #Mover para a direita
    if j < limite_direita:
        novo = deepcopy(jogo.jogo)
        novo[i][j + 1], novo[i][j] = novo[i][j], novo[i][j + 1]
        novo = No(novo, 'Direita', jogo, jogo.custo + 1)
        # mostra_array(novo.jogo)
        possibilidades.append(novo)

    #Mover para cima
    if i > limite_superior:
        novo = deepcopy(jogo.jogo)
        novo[i - 1][j], novo[i][j] = novo[i][j], novo[i - 1][j]
        novo = No(novo, 'Cima', jogo, jogo.custo + 1)
        # mostra_array(novo.jogo)
        possibilidades.append(novo)

    #Mover para baixo
    if i < limite_direita: 
        novo = deepcopy(jogo.jogo)
        novo[i + 1][j], novo[i][j] = novo[i][j], novo[i + 1][j]
        novo = No(novo, 'Baixo', jogo, jogo.custo + 1)
        # mostra_array(novo.jogo)
        possibilidades.append(novo)
    
    return possibilidades

def get_caminho(no):
    #Recebe o no da solução
    #Faz todo o caminho inverso pegando os passos
    caminho_das_pedras = []
    atual = no
    while atual.pai != None:
        caminho_das_pedras.append(no.passo)
        atual = atual.pai
    
    return caminho_das_pedras

def get_custo(no):
    #Recebe o nó da solução
    custo = len(get_caminho_das_pedras(no))
    return custo

def get_profundidade_maxima(no, profundidade=0):
    #Recebe um no de teste
    #Vê se o custo dele foi o maior
    custo = get_custo(no)
    if custo > profundidade:
        profundidade = custo
    return profundidade

def get_caminho_das_pedras(no):
    #Recebe o nó vitorioso
    #Retorna o array com o caminho completo
    caminho = []
    atual = no
    while atual.pai != None:
        caminho.append(atual.passo)
        atual = atual.pai
    return caminho[::-1]

def prepara_dic(no, algoritmo, tempo, gerados, maxima, ram):
    dic = {
        'algoritmo': "Algoritmo: " + algoritmo,
        'tempo': str(round(tempo, 2)) + " s",
        'gerados': "Nós gerados: " + str(gerados),
        'profundidade_solucao': "Profundidade da Solução: " + str(get_custo(no)),
        'maxima_profundidade': "Profundiade máxima atingida: " + str(maxima),
        'acoes': get_caminho_das_pedras(no),
        'ram': "Uso de RAM: " + str(round(ram), 2) + " MB"
    }
    return dic

def get_ram():

    if sys.platform == "win32":
        import psutil
        return psutil.Process().memory_info().rss/1024/1024
    else:
        import resource
        return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024/1024


def get_posicao(num, jogo):
    for i in range(3):
        for j in range(3):
            if num == jogo[i][j]:
                return i, j

def proximo(jogo, passo):
    i, j = get_posicao_vazio(jogo)
    if passo == "Esquerda":
        jogo[i][j - 1], jogo[i][j] = jogo[i][j], jogo[i][j - 1]
    elif passo == "Direita":
        jogo[i][j + 1], jogo[i][j] = jogo[i][j], jogo[i][j + 1]
    elif passo == "Cima":
        jogo[i - 1][j], jogo[i][j] = jogo[i][j], jogo[i - 1][j]
    elif passo == "Baixo":
        jogo[i + 1][j], jogo[i][j] = jogo[i][j], jogo[i + 1][j]
    return jogo
