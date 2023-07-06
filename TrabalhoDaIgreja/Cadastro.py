import os
from tkinter import *

#Funcao que cria um novo arquivo
def criaarq (nome):
    arq = open(nome, "w")
    arq.close()

#Funcao que retorna numero de cadastrados  
def numcad (NOME):
    info = 0
    arq = open(NOME, "r")
    for line in arq:
        info+=1
    arq.close()

    return int(info/5)

#Retorna um string sem o '\n' no final
def tiraquebra (nome):
    text = nome.replace("\n", "")
    return text

#Gera um novo codigo
def geracod (NOME):
    
    if os.path.exists(NOME) == TRUE:
        arq = open(NOME, "r")
        lines = arq.readlines()
        arq.close()

        if len(lines) != 0:

            nc = numcad(NOME)

            text = tiraquebra(lines[(nc-1) * 5])
        else:
            text = "1"
    else:
        text = "1"
        
    return int(text)+1
    
def cadastro ():
    #Abre uma janela em segundo plano
    janela = Toplevel()

    #Muda titulo da janela
    janela.title("CADASTRO") 
  
    #Se o arquivo cadastro existe  
    if os.path.exists("Cadastrados") == TRUE:
        #Gera um codigo = numeros de cadastrados + 1
        cod = geracod("Cadastrados")
    else:
        cod = 1

    #Mostra o codigo gerado na posicao 0,0 e 0,1 da janela
    Mcod = Label(janela, text = f'Código gerado: {cod}')
    Mcod.grid(column=0, row=0, columnspan=2)

    #Linha vazia
    Label(janela, text="").grid(column=0, row=1)

    #Pega a data do usuario
        #Dia
    Label(janela, text="Data: ").grid(column=0, row=2)
    dia = StringVar(janela)
    dia.set("Dia")
    dias = range(1, 32)
    opcao = OptionMenu(janela, dia, "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", 
                       "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
    opcao.grid(column=1, row=2)

    Label(janela, text="/").grid(column=2, row=2)
     
        #Mês
    mes = StringVar(janela)
    mes.set("Mes")
    opcao = OptionMenu(janela, mes, "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
    opcao.grid(column=3, row=2)

    Label(janela, text="/").grid(column=4, row=2)

        #Ano
    ano = StringVar(janela)
    ano.set("Ano")
    opcao = OptionMenu(janela, ano, "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", 
                       "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023")
    opcao.grid(column=5, row=2)

    #Junta tudo em uma string
    data = dia.get() +'/'+ mes.get() +'/'+ ano.get()
    """Mdata = Label(janela, text = "Data (00/00/0000)")
    Mdata.grid(column=0, row=2)
    data = Entry(janela, width=20)
    data.grid(column=1, row=2)"""

    #Linha vazia
    Label(janela, text="").grid(column=0, row=3)

    #O usuario escolhe o culto
    Label(janela, text="Culto: ").grid(column=0, row=4)
    culto = StringVar(janela)
    culto.set("CULTO")
    opcao = OptionMenu(janela, culto, "Santa Ceia",
                            "Irmas", "Missoes", "Jovens",
                            "Criancas", "EBD")
    opcao.grid(column=1, row=4)

    #Linha vazia
    Label(janela, text="").grid(column=0, row=5)

    #Escreve a quantidade de pessoas que estavam presentes no culto
    Label(janela, text="Quantidade de presentes: ").grid(column=0, row=6)
    quant = Entry(janela, width=10)
    quant.grid(column=1, row=6)

    #Linha vazia
    Label(janela, text="").grid(column=0, row=7)

    def cadastrar ():
        NOME = "Cadastrados"
        
        #Se o arquivo NOME nao existir ele e criado
        if os.path.exists(NOME) == False:
            criaarq (NOME)
        
        #Le tudo dentro do arquivo NOME 
        arq = open (NOME, "r")
        texto = arq.read()
        arq.close()

        #Cria um novo arquivo NOME e escreve dentro 
        #dele o texto que estava no arquivo anterior
        #com o mesmo nome
        arq = open (NOME, "w")
        arq.write(texto)
        arq.write(f'{cod}\n{data.get()}\n{culto.get()}\n{quant.get()}\n\n')
        arq.close()

        #Destroi a janela de cadastro
        janela.destroy()

    #Botao que faz um novo cadastro e fecha a janela de cadastro
    botao = Button(janela, text = "cadastrar", command=cadastrar, width=35)
    botao.grid(column=3, row=8, columnspan=3)

    #Botao que fecha a janela de cadastro sem terminar o cadastro
    botao = Button(janela, text = "cancelar", command=janela.destroy, width=35)
    botao.grid(column=0, row=8, columnspan=3)




    janela.mainloop()