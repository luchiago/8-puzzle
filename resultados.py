from tkinter import *
from algoritmos import helpers

class Resultado:
    def __init__(self, raiz, resultado, inicial):
        self.raiz = raiz
        self.raiz.title('Resultado')

        self.cont9 = Frame(raiz)
        self.cont9.pack(side=BOTTOM)

        self.cont0 = Frame(raiz)
        self.cont0.pack(side=RIGHT)

        group = LabelFrame(raiz, text="Tabuleiro", padx=5, pady=5)
        group.pack(padx=20, pady=10)
        self.passos = list(resultado['acoes'])
        self.matriz = inicial
        i, j = helpers.get_posicao_vazio(inicial)
        self.matriz[i][j] = ' '

        self.cont1 = Frame(group)
        self.cont1.pack()
        self.m1 = Entry(self.cont1)
        self.m1['width'] = 5
        self.m1.insert(0, str(self.matriz[0][0]))
        self.m1.pack(side=LEFT)
        self.m2 = Entry(self.cont1)
        self.m2['width'] = 5
        self.m2.insert(0, str(self.matriz[0][1]))
        self.m2.pack(side=LEFT)
        self.m3 = Entry(self.cont1)
        self.m3['width'] = 5
        self.m3.insert(0, str(self.matriz[0][2]))
        self.m3.pack(side=LEFT)

        self.cont2 = Frame(group)
        self.cont2.pack()
        self.m4 = Entry(self.cont2)
        self.m4['width'] = 5
        self.m4.insert(0, str(self.matriz[1][0]))
        self.m4.pack(side=LEFT)
        self.m5 = Entry(self.cont2)
        self.m5['width'] = 5
        self.m5.insert(0, str(self.matriz[1][1]))
        self.m5.pack(side=LEFT)
        self.m6 = Entry(self.cont2)
        self.m6['width'] = 5
        self.m6.insert(0, str(self.matriz[1][2]))
        self.m6.pack(side=LEFT)

        self.cont3 = Frame(group)
        self.cont3.pack()
        self.m7 = Entry(self.cont3)
        self.m7['width'] = 5
        self.m7.insert(0, str(self.matriz[2][0]))
        self.m7.pack(side=LEFT)
        self.m8 = Entry(self.cont3)
        self.m8['width'] = 5
        self.m8.insert(0, str(self.matriz[2][1]))
        self.m8.pack(side=LEFT)
        self.m9 = Entry(self.cont3)
        self.m9['width'] = 5
        self.m9.insert(0, str(self.matriz[2][2]))
        self.m9.pack(side=LEFT)

        group2 = LabelFrame(self.cont0, text="Solução", padx=5, pady=5)
        group2.pack(padx=20, pady=10)
        Label(group2, text=resultado['algoritmo']).pack()
        Label(group2, text=resultado['tempo']).pack()
        Label(group2, text=resultado['gerados']).pack()
        Label(group2, text=resultado['profundidade_solucao']).pack()
        Label(group2, text=resultado['maxima_profundidade']).pack()
        Label(group2, text=resultado['ram']).pack()
        self.prog = Button(self.cont9, text='Próximo passo',
                           padx=2, command=self.movimento)
        self.prog.pack(pady=10, padx=5, side=RIGHT)

    def movimento(self):
        if len(self.passos) == 0:
            return None
        mov = self.passos[0]
        del self.passos[0]
        self.matriz = helpers.proximo(self.matriz, mov)
        i, j = helpers.get_posicao_vazio(self.matriz)
        self.matriz[i][j] = ' '
        self.m1.delete(0, END)
        self.m1.insert(0, str(self.matriz[0][0]))
        self.m2.delete(0, END)
        self.m2.insert(0, str(self.matriz[0][1]))
        self.m3.delete(0, END)
        self.m3.insert(0, str(self.matriz[0][2]))
        self.m4.delete(0, END)
        self.m4.insert(0, str(self.matriz[1][0]))
        self.m5.delete(0, END)
        self.m5.insert(0, str(self.matriz[1][1]))
        self.m6.delete(0, END)
        self.m6.insert(0, str(self.matriz[1][2]))
        self.m7.delete(0, END)
        self.m7.insert(0, str(self.matriz[2][0]))
        self.m8.delete(0, END)
        self.m8.insert(0, str(self.matriz[2][1]))
        self.m9.delete(0, END)
        self.m9.insert(0, str(self.matriz[2][2]))
