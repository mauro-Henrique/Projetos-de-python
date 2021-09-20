from tkinter import *
from mt_mercado import Produtos
from cadastro_mercado import Cadastrar
class mercado():
    def __init__(self):
        Tela = Tk()
        Tela.geometry('300x250')
        Tela.resizable(False, False)  # Não deixa a tela mudar de tamanho
        #botões
        Label(text="").pack()
        Button(text='Cliente',width='30',height='2',command = Cadastrar).pack()
        Label(text="").pack()
        Button(text='Funcionario', width='30',height='2', command= Produtos).pack()
        Tela.mainloop()
mercado()
