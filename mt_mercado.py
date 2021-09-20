from tkinter import *
import os
class Produtos():
    def __init__(self):
        # mostra tela inicial
        self.Inter = Tk()
        self.tela = self.Inter
        self.tela.geometry('350x300')
        self.tela.resizable(False, False)
        self.tela.title('Cadastro de Produtos')
        self.lbl = Label(self.tela, text='Cadastro de produtos', bg='grey',width='300',height='2', font=('calibri',13)).pack()
        self.lbl = Label(self.tela,text="").pack()
        #botões
        self.lbl = Button(self.tela,text='Consultar',width='30',height='2',command = lambda: self.consultar()).pack()
        self.lbl = Label(self.tela,text="").pack()
        self.bt = Button(self.tela,text='Cadastrar',command= lambda: self.cadastro(), width='30',height='2').pack()
        self.Inter.mainloop()

    def cadastro(self):
        #mostrar tela de cadastro
            global fornecedor,sessão,codp,nome,preço,quantidade,fornecedorEntry,sessãoEntry,codpEntry,nomeEntry,preçoEntry,quantEntry, telaCad

            self.telaCad = Toplevel(self.Inter)
            self.telaCad.title('cadastro')
            self.telaCad.geometry('550x450')

            fornecedor = StringVar()
            sessão = StringVar()
            codp = StringVar()
            nome = StringVar()
            preço = StringVar()
            quantidade = StringVar()
        #mostra as labels que serão escritas
            self.lbl_2 = Label(self.telaCad, text="Por favor prencha as lacunas", font=('calibri',13)).pack()
            self.lbl_2 = Label(self.telaCad, text='').pack()

            self.lbl_2 = Label(self.telaCad, text="Fornecedor",font=('calibri',13)).pack()
            self.fornecedorEntry = Entry(self.telaCad, textvariable=fornecedor)
            self.fornecedorEntry.pack()

            self.lbl_2 = Label(self.telaCad, text="Sessão",font=('calibri',13)).pack()
            self.sessãoEntry = Entry(self.telaCad, textvariable=sessão)
            self.sessãoEntry.pack()

            self.lbl_2 = Label(self.telaCad, text="Codigo",font=('calibri',13)).pack()
            self.codpEntry = Entry(self.telaCad, textvariable=codp)
            self.codpEntry.pack()

            self.lbl_2 = Label(self.telaCad, text="Nome do Produto",font=('calibri',13)).pack()
            self.nomeEntry = Entry(self.telaCad, textvariable=nome)
            self.nomeEntry.pack()

            self.lbl_2 = Label(self.telaCad, text="Preço",font=('calibri',13)).pack()
            self.preçoEntry = Entry(self.telaCad, textvariable=preço)
            self.preçoEntry.pack()

            self.lbl_2 = Label(self.telaCad, text="Quantidade",font=('calibri',13)).pack()
            self.quantEntry = Entry(self.telaCad, textvariable=quantidade)
            self.quantEntry.pack()

            self.lbl_2 = Label(self.telaCad, text='').pack()
            self.bt_2 = Button(self.telaCad, text='Cadastro', command=lambda: self.registrar(), width='30',height='2').pack()

    def registrar(self):
        #Registra o cadastro
        global arquivo, rfornecedor, rsessão, rcodp, rnome,rpreço,rquantidade
        rfornecedor = fornecedor.get()
        rsessão = sessão.get()
        rcodp = codp.get()
        rnome = nome.get()
        rpreço = preço.get()
        rquantidade = quantidade.get()
        #tranforma em arquivos o que foi escritos no cadastro
        self.arquivo = open(rnome,'a+')
        self.arquivo.write(str(rfornecedor)+'\n')
        self.arquivo.write(str(rsessão) + '\n')
        self.arquivo.write(str(rcodp) + '\n')
        self.arquivo.write(str(rnome) + '\n')
        self.arquivo.write(str(rpreço) + '\n')
        self.arquivo.write(str(rquantidade))

        self.fornecedorEntry.delete(0, END)
        self.sessãoEntry.delete(0, END)
        self.codpEntry.delete(0, END)
        self.nomeEntry.delete(0, END)
        self.preçoEntry.delete(0, END)
        self.quantEntry.delete(0, END)
        self.arquivo.close()
        self.lbl_2 = Label(self.telaCad, text = 'Cadastro registrado', fg = 'green', font=('calibri',11)).pack()

    def consultar(self):
        #abre a tela de consulta
        global ccod, cnome, ccodpEntry, cnomeEntry,telaCon,verificar

        self.telaCon = Toplevel(self.Inter)
        self.telaCon.title('cadastro')
        self.telaCon.geometry('350x300')

        ccod = StringVar()
        cnome = StringVar()
        #mostra as lebels para escrever o codigo e a
        self.lbl_3 = Label(self.telaCon, text="Por favor prencha as lacunas", font=('calibri', 13)).pack()
        self.lbl_3 = Label(self.telaCon, text='').pack()

        self.lbl_3 = Label(self.telaCon, text="Codigo", font=('calibri', 13)).pack()
        self.ccodpEntry = Entry(self.telaCon, textvariable=ccod)
        self.ccodpEntry.pack()

        self.lbl_3 = Label(self.telaCon, text="Nome do Produto", font=('calibri', 13)).pack()
        self.cnomeEntry = Entry(self.telaCon, textvariable=cnome)
        self.cnomeEntry.pack()

        self.lbl_3 = Label(self.telaCon, text='').pack()
        self.bt_3 = Button(self.telaCon, text='Consultar', command= lambda: self.consultarRegistro(), width='30', height='2').pack()

    def consultarRegistro(self):
        # consulta o registro
        global verificar, crnome, crcod, listaAquivo, arquivoLog
        crcod = ccod.get()
        crnome = cnome.get()

        self.ccodpEntry.delete(0, END)
        self.cnomeEntry.delete(0, END)
        #le os arquivos salvos dentro do cadastro
        self.listaAquivo = os.listdir()
        if crnome in self.listaAquivo:
            self.arquivoLog = open(crnome, 'r')
            self.verificar = self.arquivoLog.read().splitlines()
            if crcod in self.verificar:
                self.consultarCerto()
            else:
                self.naoCod()
        else:
            self.naoEncontrado()

    def consultarCerto(self):
        #abre uma tela mostrando q o codigo deu certo e mostra as infromações do cadastro
        global telaSucesso
        self.telaSucesso = Toplevel(self.Inter)
        self.telaSucesso.title()
        self.telaSucesso.geometry('350x300')
        self.lbl_4 = Label(self.telaSucesso,text = 'cosulta aceita', font=('calibri',15)).pack()
        self.lbl_4 = Label(self.telaSucesso, text='')
        for self.linha in self.verificar:
            self.linha = self.linha.rstrip()
            self.lbl_4 = Label(self.telaSucesso, text=f'informações: {self.linha}', font=('calibri',13)).pack()
        self.lbl_4 = Label(self.telaSucesso, text ='').pack()
        self.bt_4 = Button(self.telaSucesso, text='Voltar',  width='20', height='2',command=lambda: self.sair()).pack()

    def naoCod(self):
        #motra se o nome não foi achado
        global telaSS
        self.telaSS = Toplevel(self.Inter)
        self.telaSS.title('não encotrado')
        self.telaSS.geometry('150x100')
        self.lbl_5 = Label(self.telaSS, text='Codigo não achado').pack()
        self.bt_5 = Button(self.telaSS, text='Voltar', command= lambda: self.sair1()).pack()

    def naoEncontrado(self):
        #mostra se o codigo não foi achado
        global telaNC
        self.telaNC = Toplevel(self.Inter)
        self.telaNC.title('não encotrado')
        self.telaNC.geometry('150x100')
        self.lbl_6 = Label(self.telaNC, text='Nome não encontrado').pack()
        self.bt_6 = Button(self.telaNC, text='Voltar', command= lambda: self.sair2()).pack()

    def sair(self):
        #fecha a tela de sucesso
        self.telaSucesso.destroy()

    def sair1(self):
        #fecha a tela q mostra o erro do nome
        self.telaSS.destroy()

    def sair2(self):
        # fecha a tela q mostra o erro do codigo
            self.telaNC.destroy()
