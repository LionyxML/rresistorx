#!/usr/bin/python3
# Arquivo : rresistorX.py
# Programa: Treino de leitura de resistores
# Autor   : Rahul Martim Juliato
# Versão  : 0.1  -  24.10.2018


#---===[0. Bibliotecas]===---
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
import math
#---===[0. Fim das Bibliotecas]===---


#---===[1. Funções]===---
def quit():
    """ Sai do programa destruindo o necessário
    """
    global janela
    janela.destroy()

    
def sobre():
    """ Mostra as informações do programa
    """
    mb.showinfo("r[RESISTOR]X",'''

    r[RESISTOR]X

Programa para treino de interpretação de faixas de resistores.

Versão: 0.1

Autor: Rahul Martim Juliato
(rahul.juliato@gmail.com)

''')

    
def erro(mensagem):
    """ Sobe uma messagebox de erro com a mensagem
    passada"""
    mb.showerror("Erro!", mensagem)
 
    
# Snipet para conversão em números de engenharia
from math import floor, log10

def powerise10(x):
    """ Returns x as a*10**b with 0 <= a < 10
    """
    if x == 0: return 0,0
    Neg = x < 0
    if Neg: x = -x
    a = 1.0 * x / 10**(floor(log10(x)))
    b = int(floor(log10(x)))
    if Neg: a = -a
    return a,b

def eng(x):
    """Return a string representing x in an engineer friendly notation"""
    a,b = powerise10(x)
    if -3 < b < 3: return "%.4g" % x
    a = a * 10**(b % 3)
    b = b - b % 3
    return "%.4gE%s" % (a,b)
## Fim do Snipet


def calcula():
    """ Realiza as leituras das cores selecionadas, calcula e formata
        a saída numérica.
    """ 

    global modo

    leitura_faixas=[ valores_padrao[x].get(str(selecionado[x].get())) for x in range(modo)]

    if modo != 5:
        final = str(leitura_faixas) + '  =  ' + str(eng((leitura_faixas[0]*10+leitura_faixas[1]) * leitura_faixas[2])) + chr(937) + '  ' + chr(177) + str(leitura_faixas[3]) + '%'
    else:
        final = str(leitura_faixas) + '  =  ' + str(eng((leitura_faixas[0]*100+leitura_faixas[1]*10+leitura_faixas[2])* leitura_faixas[3])) + chr(937) + '  ' + chr(177) + str(leitura_faixas[4]) + '%'
        
    ent_resultado.delete(0,100)
    ent_resultado.insert(0, final)


def selec_faixa():
    """ Funções para adaptação quanto à seleção de faixas.
    """

    global l, c, faixas, modo
    global valores_padrao, valores_5_faixas, valores_4_faixas

    ii = 7
    i = 1

    if opcao.get() == 2:

        valores_padrao = valores_5_faixas
        modo = 5
        
        desenha_botoes()
        
        l = tk.Label(janela, text=str('Faixa %s :' % (5)))
        c = tk.ttk.Combobox(janela, values = list(valores_padrao[4]), textvariable = selecionado[4])        
  
        l.grid(sticky='E', row = ii, column = i-1)

        c.configure(width = 10)
        c.grid(sticky='E', row = ii, column = i, columnspan = 2)
        faixas[str('Faixa %s' % (str(5)))] = c

    else:
        l.destroy()
        c.destroy()
        
        valores_padrao = valores_4_faixas
        modo = 4
        
        desenha_botoes()
        

def desenha(demo = 0):
    """ Realiza o desenho com base:
           demo == 0 : nas cores selecionadas
           demo == 1 : nas cores de demonstração para abertura do programa
    """

    global modo

    cores = {'Preto':'black', 'Marrom':'brown', 'Vermelho':'red', 'Laranja':'orange', 'Amarelo':'yellow', 'Verde':'green', 'Azul':'blue', 'Violeta':'magenta', 'Cinza':'gray', 'Branco':'white', 'Dourado':'#FFD700', 'Prateado':'#C0C0C0'}

    if demo == 1:
        pintura = [cores.get('Vermelho'), cores.get('Verde'), cores.get('Marrom'), cores.get('Prateado')]
    else:
        pintura = [ cores.get(str(selecionado[x].get())) for x in range(modo)]
    
    w = tk.Canvas(janela, width = 250, height = 90, bg='white')
    w.grid(sticky='', row = 0, column = 3, rowspan = 6, padx = 10)

    w.create_line(0, 45, 40, 45)
    w.create_line(250, 45, 210, 45)
    w.create_rectangle(40, 10, 210, 80)
    w.create_rectangle(55, 10,  75, 80, fill = pintura[0])
    w.create_rectangle(85, 10,  105, 80, fill = pintura[1])
    w.create_rectangle(115, 10,  135, 80, fill = pintura[2])
    w.create_rectangle(145, 10,  165, 80, fill = pintura[3])
    if modo == 5:
        w.create_rectangle(175, 10,  195, 80, fill = pintura[4])        



def desenha_botoes():
    """ Desenha os labels e entrys com base na quantidade de faixas selecionadas
        e preenche com as opções padrão de cada faixa.
    """

    global valores_padrao, selecionado, faixas, modo, l, c
    
    ii = inicio_row + 1
    i  = inicio_col

    for y in range(4):
        l = tk.Label(janela, text=str('Faixa %s :' % (1+y)))
        l.grid(sticky='E', row = ii, column = i-1)
        
        c = tk.ttk.Combobox(janela, values = list(valores_padrao[y]), textvariable = selecionado[y])
        c.configure(width = 10)
        c.grid(sticky='E', row = ii, column = i, columnspan = 2)
        faixas[str('Faixa %s' % (str(y)))] = c

        ii += 1


#---===[1. Fim das Funções]===---



#---===[2. Início da geração da Janela]===---
# 2.0. Definições principais da janela
janela = tk.Tk()
janela.wm_title('r[RESISTOR]X v0.1')
janela.wm_minsize(600,220)
janela.grid_anchor(anchor='c')
#janela.tk_setPalette('white')


# 2.0. Barra de menu
barramenu = tk.Menu(janela)
arquivo = tk.Menu(barramenu, tearoff=800)
arquivo.add_command(label="Sobre", command=sobre)
arquivo.add_separator()
arquivo.add_command(label="Sair", command=quit)
barramenu.add_cascade(label="Arquivo", menu=arquivo)

janela.config(menu=barramenu)


# 2.0. Apresentaçã da tela principal


# Base para alinhamento do grid
inicio_row = 0
inicio_col = 1


# Desenha os labels
lab_faixas = tk.Label(janela, text='Faixas :')
lab_faixas.grid(sticky='E', row = inicio_row, column = inicio_col-1)


# Radio Button para seleção da quantidade de faixas
opcao = tk.IntVar()
opcao.set(1)

rad_opf = tk.Radiobutton(janela, text = '4', variable     = opcao, value = 1, command = selec_faixa)
rad_opf.grid(column = inicio_col, row = inicio_row, padx = 4)

rad_opf = tk.Radiobutton(janela, text = '5', variable     = opcao, value = 2, command = selec_faixa)
rad_opf.grid(column = inicio_col+1, row = inicio_row, padx = 4)


# Dicionário de definições dos valores padrão de cada faixa em cada tipo de resistor
valores_4_faixas = [{'Marrom':1, 'Vermelho':2, 'Laranja':3, 'Amarelo':4, 'Verde':5, 'Azul':6, 'Violeta':7, 'Cinza':8, 'Branco':9},
                  {'Preto':0, 'Marrom':1, 'Vermelho':2, 'Laranja':3, 'Amarelo':4, 'Verde':5, 'Azul':6, 'Violeta':7, 'Cinza':8, 'Branco':9},
                  {'Preto':1, 'Marrom':10, 'Vermelho':100, 'Laranja':1000, 'Amarelo':10000, 'Verde':100000, 'Azul':1000000, 'Violeta':10000000, 'Cinza':100000000, 'Branco':1000000000, 'Dourado':0.1, 'Prateado':0.01},
                  {'Marrom':1, 'Vermelho':2, 'Verde':0.5, 'Azul':0.25, 'Violeta':0.1, 'Cinza':0.05, 'Dourado':5, 'Prateado':10}]

valores_5_faixas = [{'Marrom':1, 'Vermelho':2, 'Laranja':3, 'Amarelo':4, 'Verde':5, 'Azul':6, 'Violeta':7, 'Cinza':8, 'Branco':9},
                  {'Preto':0, 'Marrom':1, 'Vermelho':2, 'Laranja':3, 'Amarelo':4, 'Verde':5, 'Azul':6, 'Violeta':7, 'Cinza':8, 'Branco':9},
                  {'Preto':0, 'Marrom':1, 'Vermelho':2, 'Laranja':3, 'Amarelo':4, 'Verde':5, 'Azul':6, 'Violeta':7, 'Cinza':8, 'Branco':9},
                  {'Preto':1, 'Marrom':10, 'Vermelho':100, 'Laranja':1000, 'Amarelo':10000, 'Verde':100000, 'Azul':1000000, 'Violeta':10000000, 'Cinza':100000000, 'Branco':1000000000, 'Dourado':0.1, 'Prateado':0.01},
                  {'Marrom':1, 'Vermelho':2, 'Verde':0.5, 'Azul':0.25, 'Violeta':0.1, 'Cinza':0.05, 'Dourado':5, 'Prateado':10}]


# Seta o valor inicial para o resistor padrão e o modo de 4 faixas
valores_padrao = valores_4_faixas
modo = 4

# Cria a variável que irá conter os objetos Entrys onde ocorrerá a seleção
faixas = {}

# Cria a variável que irá conter a seleção de cada objeto Entry
selecionado = [tk.StringVar() for x in range(6)]

# Inicia o programa com o desenho demo e desenhando as entrys
desenha(1)
desenha_botoes()

# Botão para chamar a função que desenha o resistor
but_desenha = tk.Button(janela, text = "Desenha", command = desenha, width = 10)
but_desenha.grid(sticky='EW', row = 8, column = 0, columnspan = 3, pady = 10)

# Botão para calcular o valor ôhmico do resistor
but_calcula = tk.Button(janela, text = "Calcula", command = calcula, width = 10)
but_calcula.grid(sticky='EW', row = 9, column = 0, columnspan = 3)

# Entry para a saída do cálculo
ent_resultado = tk.Entry(janela, width = 40)
ent_resultado.grid(row = 9, column = 3)


tk.mainloop()
#---===[2 Fim da Geração da Janela]===---
