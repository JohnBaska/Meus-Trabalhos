from Cadastro import *
from tkinter import *
from Lista import *
from Busca import *
from Excluir import *

janelamenu = Tk()

janelamenu.title("MENU")

#Botao usado para abrir a janela de cadastro 
botao1 = Button(janelamenu, text="Cadastro", command=cadastro, bg="blue", fg="white", width=15, height=2)
botao1.grid(column=0, row=1)

#Botao usado para abrir janela de Lista
botao2 = Button(janelamenu, text="Lista", command=lista, bg="blue", fg="white", width=15, height=2)
botao2.grid(column=1, row=1)

#Botao usado para abrir janela e Busca
botao3 = Button(janelamenu, text="Busca", command=busca, bg="blue", fg="white", width=15, height=2)
botao3.grid(column=0, row=2)

#Botao usado para abrir janela de Exclusão
botao3 = Button(janelamenu, text="Apaga", command=buscaexcluir, bg="blue", fg="white", width=15, height=2)
botao3.grid(column=1, row=2)

janelamenu.mainloop()