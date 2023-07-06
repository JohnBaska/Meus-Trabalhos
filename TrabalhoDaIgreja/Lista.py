from tkinter import *
from tkinter import ttk
from struct import *

#Funcao que retorna numero de cadastrados
def numcad ():
    NOME = "Cadastrados"
    info = 0
    arq = open(NOME, "rb")
    for line in arq:
        info+=1

        
    return int(info/5)

#Retorna um string sem o '\n' no final
def tiraquebra (nome):
    text = nome.replace("\n", "")
    return text
            
#Cria uma tabela com todos os dados
def lista ():
    #Abre uma janela em segundo plano
    janela = Toplevel()

    #Muda titula da janela
    janela.title("LISTA")

    #Cria uma tabela de 4 colunas em branco
    tree = ttk.Treeview(janela, selectmode="browse", column=("c0", "c1", "c2", "c3"), show='headings')
    
    #1º coluna
    tree.column("c0", width=200, minwidth=50, stretch=NO)
    tree.heading("#1", text='CODIGO')

    #2º coluna
    tree.column("c1", width=200, minwidth=50, stretch=NO)
    tree.heading("#2", text='DATA')
    
    #3º coluna
    tree.column("c2", width=200, minwidth=50, stretch=NO)
    tree.heading("#3", text='CULTO')

    #4º coluna
    tree.column("c3", width=200, minwidth=50, stretch=NO)
    tree.heading("#4", text='QUANT. DE PESSOAS')

    #Posicao da tabela
    tree.grid(column=0, row=0)

    
    NOME = "Cadastrados"
    A = range(numcad())
    arq = open(NOME, "r")
    
    #Preenche a tabela com os dados do arquivo
    for i in A:
        cod = arq.readline()
        cod = tiraquebra(cod)
        data = arq.readline()
        data = tiraquebra(data)
        culto = arq.readline()
        culto = tiraquebra(culto)
        quant = arq.readline()
        quant = tiraquebra(quant)
        arq.read(1)
        elementos = (cod, data, culto, quant)
        tree.insert("", END, values=elementos, tag=f'{i+1}')
    
         

    janela.mainloop()
