from algoritmos import helpers, node, profundidade, largura, gulosa, a_estrela
from tkinter import *
from tkinter import messagebox
from resultados import Resultado

class Jogo:
    def __init__(self, master):
        self.frame1 = Frame(master)
        self.frame1.pack(side=TOP, padx=10, pady=10)
        self.matriz = LabelFrame(master, padx=20, pady=20)
        self.matriz.pack()
        self.cont1 = Frame(self.matriz)
        self.cont1.pack()
        self.e1 = Entry(self.cont1, width=5)
        self.e1.pack(side=LEFT)
        self.e2 = Entry(self.cont1, width=5)
        self.e2.pack(side=LEFT)
        self.e3 = Entry(self.cont1, width=5)
        self.e3.pack(side=LEFT)
        self.cont2 = Frame(self.matriz)
        self.cont2.pack()
        self.e4 = Entry(self.cont2, width=5)
        self.e4.pack(side=LEFT)
        self.e5 = Entry(self.cont2, width=5)
        self.e5.pack(side=LEFT)
        self.e6 = Entry(self.cont2, width=5)
        self.e6.pack(side=LEFT)
        self.cont3 = Frame(self.matriz)
        self.cont3.pack()
        self.e7 = Entry(self.cont3, width=5)
        self.e7.pack(side=LEFT)
        self.e8 = Entry(self.cont3, width=5)
        self.e8.pack(side=LEFT)
        self.e9 = Entry(self.cont3, width=5)
        self.e9.pack(side=LEFT)
        algo1 = Button(self.matriz, text="Busca em Largura", command=self.largura)
        algo2 = Button(self.matriz, text="Busca em Profundidade", command=self.profundidade)
        algo3 = Button(self.matriz, text="Busca Gulosa", command=self.gulosa)
        algo4 = Button(self.matriz, text="Busca A*", command=self.a_estrela)
        algo1.pack(side=TOP)
        algo2.pack(side=TOP)
        algo3.pack(side=BOTTOM)
        algo4.pack(side=BOTTOM)

    def get_tabuleiro(self):
        tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        try:
            tabuleiro[0][0] = int(self.e1.get().strip())
        except:
            tabuleiro[0][0] = 0
        try:
            tabuleiro[0][1] = int(self.e2.get().strip())
        except:
            tabuleiro[0][1] = 0
        try:
            tabuleiro[0][2] = int(self.e3.get().strip())
        except:
            tabuleiro[0][2] = 0
        try:
            tabuleiro[1][0] = int(self.e4.get().strip())
        except:
            tabuleiro[1][0] = 0
        try:
            tabuleiro[1][1] = int(self.e5.get().strip())
        except:
            tabuleiro[1][1] = 0
        try:
            tabuleiro[1][2] = int(self.e6.get().strip())
        except:
            tabuleiro[1][2] = 0
        try:
            tabuleiro[2][0] = int(self.e7.get().strip())
        except:
            tabuleiro[2][0] = 0
        try:
            tabuleiro[2][1] = int(self.e8.get().strip())
        except:
            tabuleiro[2][1] = 0
        try:
            tabuleiro[2][2] = int(self.e9.get().strip())
        except:
            tabuleiro[2][2] = 0
        return tabuleiro
    
    def largura(self):
        tabuleiro = self.get_tabuleiro()
        jogo = node.No(tabuleiro, "Inicial")
        self.mostra_resultado(largura.busca(jogo), tabuleiro)

    def profundidade(self):
        tabuleiro = self.get_tabuleiro()
        jogo = node.No(tabuleiro, "Inicial")
        self.mostra_resultado(profundidade.busca(jogo), tabuleiro)

    def gulosa(self):
        tabuleiro = self.get_tabuleiro()
        jogo = node.No(tabuleiro, "Inicial")
        self.mostra_resultado(gulosa.busca(jogo), tabuleiro)

    def a_estrela(self):
        tabuleiro = self.get_tabuleiro()
        jogo = node.No(tabuleiro, "Inicial")
        self.mostra_resultado(a_estrela.busca(jogo), tabuleiro)
    
    def mostra_resultado(self, resultado, inicial):
        if resultado is False:
            messagebox.showinfo("Erro!", "Não foi encontrada solução")
        else:
            nova = Tk()
            Resultado(nova, resultado, inicial)
            nova.title("Resultado da busca em" + resultado['algoritmo'][10:])
            nova.geometry("400x400")
            nova.mainloop()

root = Tk()
Jogo(root)
root.title("8 Puzzle")
root.geometry("400x400")
root.mainloop()

