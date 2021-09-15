from tkinter import *
import os
def mostrar_tela():
    # mostra tela inicial
    global tela
    tela = Tk()
    tela.geometry('350x300')
    tela.title('Cadastro de Produtos')
    Label(text='Cadastro de produtos', bg='grey',width='300',height='2', font=('calibri',13)).pack()
    Label(text="").pack()
    #botões
    Button(text='Consultar',width='30',height='2',command=consultar).pack()
    Label(text="").pack()
    Button(text='Cadastrar',command=cadastro, width='30',height='2').pack()
    tela.mainloop()

def cadastro():
    #mostrar tela de cadastro
        global fornecedor,sessão,codp,nome,preço,quantidade,fornecedorEntry,sessãoEntry,codpEntry,nomeEntry,preçoEntry,quantEntry, telaCad

        telaCad = Toplevel(tela)
        telaCad.title('cadastro')
        telaCad.geometry('550x450')

        fornecedor = StringVar()
        sessão = StringVar()
        codp = StringVar()
        nome = StringVar()
        preço = StringVar()
        quantidade = StringVar()
    #mostra as labels que serão escritas
        Label(telaCad, text="Por favor prencha as lacunas", font=('calibri',13)).pack()
        Label(telaCad, text='').pack()

        Label(telaCad, text="Fornecedor",font=('calibri',13)).pack()
        fornecedorEntry = Entry(telaCad, textvariable=fornecedor)
        fornecedorEntry.pack()

        Label(telaCad, text="Sessão",font=('calibri',13)).pack()
        sessãoEntry = Entry(telaCad, textvariable=sessão)
        sessãoEntry.pack()

        Label(telaCad, text="Codigo",font=('calibri',13)).pack()
        codpEntry = Entry(telaCad, textvariable=codp)
        codpEntry.pack()

        Label(telaCad, text="Nome do Produto",font=('calibri',13)).pack()
        nomeEntry = Entry(telaCad, textvariable=nome)
        nomeEntry.pack()

        Label(telaCad, text="Preço",font=('calibri',13)).pack()
        preçoEntry = Entry(telaCad, textvariable=preço)
        preçoEntry.pack()

        Label(telaCad, text="Quantidade",font=('calibri',13)).pack()
        quantEntry = Entry(telaCad, textvariable=quantidade)
        quantEntry.pack()

        Label(telaCad, text='').pack()
        Button(telaCad, text='Cadastro', command=registrar, width='30',height='2').pack()

def registrar():
    #Registra o cadastro
    global arquivo, rfornecedor, rsessão, rcodp, rnome,rpreço,rquantidade
    rfornecedor = fornecedor.get()
    rsessão = sessão.get()
    rcodp = codp.get()
    rnome = nome.get()
    rpreço = preço.get()
    rquantidade = quantidade.get()
    #tranforma em arquivos o que foi escritos no cadastro
    arquivo = open(rnome,'a+')
    arquivo.write(str(rfornecedor)+'\n')
    arquivo.write(str(rsessão) + '\n')
    arquivo.write(str(rcodp) + '\n')
    arquivo.write(str(nome) + '\n')
    arquivo.write(str(rpreço) + '\n')
    arquivo.write(str(rquantidade))

    fornecedorEntry.delete(0, END)
    sessãoEntry.delete(0, END)
    codpEntry.delete(0, END)
    nomeEntry.delete(0, END)
    preçoEntry.delete(0, END)
    quantEntry.delete(0, END)
    arquivo.close()
    Label(telaCad, text = 'Cadastro registrado', fg = 'green', font=('calibri',11)).pack()
def consultar():
    #abre a tela de consulta
    global ccod, cnome, ccodpEntry, cnomeEntry,telaCon,verificar

    telaCon = Toplevel(tela)
    telaCon.title('cadastro')
    telaCon.geometry('350x300')

    ccod = StringVar()
    cnome = StringVar()
    #mostra as lebels para escrever o codigo e a
    Label(telaCon, text="Por favor prencha as lacunas", font=('calibri', 13)).pack()
    Label(telaCon, text='').pack()

    Label(telaCon, text="Codigo", font=('calibri', 13)).pack()
    ccodpEntry = Entry(telaCon, textvariable=ccod)
    ccodpEntry.pack()

    Label(telaCon, text="Nome do Produto", font=('calibri', 13)).pack()
    cnomeEntry = Entry(telaCon, textvariable=cnome)
    cnomeEntry.pack()

    Label(telaCon, text='').pack()
    Button(telaCon, text='Consultar', command= consultarRegistro, width='30', height='2').pack()
def consultarRegistro():
    # consulta o registro
    global verificar, crnome, crcod, listaAquivo, arquivoLog
    crcod = ccod.get()
    crnome = cnome.get()

    ccodpEntry.delete(0, END)
    cnomeEntry.delete(0, END)
    #le os arquivos salvos dentro do cadastro
    listaAquivo = os.listdir()
    if crnome in listaAquivo:
        arquivoLog = open(crnome, 'r')
        verificar = arquivoLog.read().splitlines()
        if crcod in verificar:
            consultarCerto()
        else:
            naoCod()
    else:
        naoEncontrado()

def consultarCerto():
    #abre uma tela mostrando q o codigo deu certo e mostra as infromações do cadastro
    global telaSucesso
    telaSucesso = Toplevel(tela)
    telaSucesso.title()
    telaSucesso.geometry('350x300')
    Label(telaSucesso,text = 'cosulta aceita', font=('calibri',15)).pack()
    Label(telaSucesso, text='')
    for linha in verificar:
        linha = linha.rstrip()
        Label(telaSucesso, text=f'informações: {linha}', font=('calibri',13)).pack()
    Label(telaSucesso, text ='').pack()
    Button(telaSucesso, text='Voltar',  width='20', height='2',command=sair).pack()

def naoEncontrado():
    #motra se o nome não foi achado
    global telaSS
    telaSS = Toplevel(tela)
    telaSS.title('não encotrado')
    telaSS.geometry('150x100')
    Label(telaSS, text='Nome não achado').pack()
    Button(telaSS, text='Voltar', command=sair1).pack()

def naoCod():
    #mostra se o codigo não foi achado
    global telaNC
    telaNC = Toplevel(tela)
    telaNC.title('não encotrado')
    telaNC.geometry('150x100')
    Label(telaNC, text='codigo não encontrado').pack()
    Button(telaNC, text='Voltar', command=sair2).pack()

def sair():
    #fecha a tela de sucesso
    telaSucesso.destroy()
def sair1():
    #fecha a tela q mostra o erro do nome
    telaSS.destroy()
def sair2():
    # fecha a tela q mostra o erro do codigo
        telaNC.destroy()
mostrar_tela()





