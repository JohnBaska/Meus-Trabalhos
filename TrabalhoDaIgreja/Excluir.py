from tkinter import *
from tkinter import ttk
import os
from Busca import *
from Lista import *

#Funcao que retorna o numero de cadastrados
def numcad (NOME):
    info = 0
    arq = open(NOME, "rb")
    for line in arq:
        info+=1
    arq.close()

    return int(info/5)

#Retorna um string sem o '\n' no final
def tiraquebra (nome):
    text = nome.replace("\n", "")
    return text

#Filtra os dados da tabela
def buscaexcluir ():
    #Abre uma janela em segundo plano
    janela = Toplevel()

    #Muda titulo da janela
    janela.title("EXCLUSÂO") 

    #Se o arquivo cadastro existe
    if os.path.isfile("Buscados"):
        #Exclui um arquivo
        os.remove("Buscados")
    
    #Pega a data do usuario
    Mdata = Label(janela, text = "Data (00/00/0000)")
    Mdata.grid(column=0, row=0)
    Edata = Entry(janela, width=20)
    Edata.grid(column=1, row=0)

    #Linha vazia
    Label(janela, text="").grid(column=0, row=1)

    #O usuario escolhe o culto
    Label(janela, text="Culto: ").grid(column=0, row=2)
    Eculto = StringVar(janela)
    Eculto.set("CULTO")
    opcao = OptionMenu(janela, Eculto, "Santa Ceia",
                            "Irmas", "Missoes", "Jovens",
                            "Criancas", "EBD")
    opcao.grid(column=1, row=2)

    #Linha vazia
    Label(janela, text="").grid(column=0, row=3)
    
    #Escreve a quantidade de pessoas que estavam 
    #presentes no culto
    Label(janela, text="Quantidade de presentes: ").grid(column=0, row=4)
    Equant = Entry(janela, width=10)
    Equant.grid(column=1, row=4)

    #Linha vazia
    Label(janela, text="").grid(column=0, row=5)

    #Pega o codigo do usuario
    Mcod = Label(janela, text = "Codigo: ")
    Mcod.grid(column=0, row=6)
    Ecod = Entry(janela, width=20)
    Ecod.grid(column=1, row=6)
    
    #Linha vazia
    Label(janela, text="").grid(column=0, row=7)

    def tabela ():
        arq = open("Cadastrados", "r")
        arq1 = open("Buscados", "w")
        
        #Busca por cadastros com os dados fornecidos pelo usuario
        for i in range(numcad("Cadastrados")):
            #Pega dados do arquivo
            cod = arq.readline()
            cod = tiraquebra(cod)
            data = arq.readline()
            data = tiraquebra(data)
            culto = arq.readline()
            culto = tiraquebra(culto)
            quant = arq.readline()
            quant = tiraquebra(quant)
            lx = arq.readline()

            #Compara com os dados fornecidos pelo usuario
            if Eculto.get() == "CULTO" or Eculto.get() == culto:
                if Edata.get() == "" or Edata.get() == data:
                    if Equant.get() == "" or Equant.get() == quant:
                        if Ecod.get() == "" or Ecod.get() == cod:
                            arq1.write(f'{cod}\n{data}\n{culto}\n{quant}\n\n')

        arq1.close()
        arq.close()
 

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
        tree.grid(column=0, row=8, columnspan=3)

        
        NOME = "Buscados"
        A = range(numcad(NOME))
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
   
    def excluir ():
        #Pega tudo que esta dentro do arquivo Cadastro
        arq = open ("Cadastrados", "r")
        text = arq.read()
        arq.close()

        #Exlui o arquivo Cadastro
        if os.path.isfile("Cadastrados"):
            os.remove("Cadastrados")

        
        #Cria um arquivo temporario
        NOME = "Temporario"
        arq = open (NOME, "w")
        arq.write(text)
        arq.close()

        arq = open(NOME, "r")
        arq1 = open("Cadastrados", "w")
        
        #Busca por cadastros com os dados fornecidos pelo usuario
        for i in range(numcad(NOME)):
            #Pega dados do arquivo
            cod = arq.readline()
            cod = tiraquebra(cod)
            data = arq.readline()
            data = tiraquebra(data)
            culto = arq.readline()
            culto = tiraquebra(culto)
            quant = arq.readline()
            quant = tiraquebra(quant)
            lx = arq.readline()

            #Compara com os dados fornecidos pelo usuario
            if Eculto.get() == "CULTO" or Eculto.get() != culto:
                if Edata.get() == "" or Edata.get() != data:
                    if Equant.get() == "" or Equant.get() != quant:
                        if Ecod.get() == "" or Ecod.get() != cod:
                            arq1.write(f'{cod}\n{data}\n{culto}\n{quant}\n\n')    

        arq1.close()
        arq.close()

        #Exlui o arquivo Cadastro
        if os.path.isfile(NOME):
            os.remove(NOME)
        
        lista()



    #Botao que fecha a janela de cadastro sem terminar o cadastro
    botao1 = Button(janela, text="Cancelar", command=janela.destroy, width=20)
    botao1.grid(column=0, row=9)

    #Botao que faz um novo cadastro e fecha a janela de cadastro
    botao2 = Button(janela, text="Excluir", command=excluir, width=20)
    botao2.grid(column=1, row=9)

    #Botao que faz um novo cadastro e fecha a janela de cadastro
    botao2 = Button(janela, text="Buscar", command=tabela, width=20)
    botao2.grid(column=2, row=9)



    janela.mainloop()