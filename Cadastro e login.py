from tkinter import *
import os
def mostrar_tela():
    #abre a tela inicial
    global tela
    tela = Tk()
    tela.geometry('300x250')
    tela.title('Sistema de login e cadastro')
    Label(text='Login e cadastro', bg='grey',width='300',height='2', font=('calibri',13)).pack()
    Label(text="").pack()
    Button(text='Login',width='30',height='2',command=login).pack()
    Label(text="").pack()
    Button(text='cadastre-se',command=cadastro, width='30',height='2').pack()
    tela.mainloop()
def cadastro():
    #abre a tela de cadastro
    global usuario, senha, usuarioEntry, senhaEntry, telaCad

    telaCad = Toplevel(tela)
    telaCad.title('cadastro')
    telaCad.geometry('300x250')

    usuario = StringVar()
    senha = StringVar()

    Label(telaCad, text="Por favor prencha as lacunas").pack()
    Label(telaCad, text='').pack()
    Label(telaCad,text="Usuario").pack()
    usuarioEntry = Entry(telaCad, textvariable=usuario)
    usuarioEntry.pack()
    Label(telaCad, text="Senha").pack()
    senhaEntry = Entry(telaCad, textvariable=senha)
    senhaEntry.pack()
    Label(telaCad, text='').pack()
    Button(telaCad, text='Cadastro', command=registrarCadastro, width=10, height=1).pack()
def registrarCadastro():
    #Registra o cadastro do usuario
    global arquivo
    nomeUsuario = usuario.get()
    senhaUsuario = senha.get()

    arquivo = open(nomeUsuario,'w')
    arquivo.write(nomeUsuario+'\n')
    arquivo.write(senhaUsuario)
    arquivo.close()
    usuarioEntry.delete(0, END)
    senhaEntry.delete(0, END)

    Label(telaCad, text = 'Cadastro registrado', fg = 'green', font=('calibri',11)).pack()    
def login():
    #Abre a tela de login
    global telaLog, logUsuario, logSenha, logEntryusu, logEntrysen
    telaLog = Toplevel(tela)
    telaLog.title('Login')
    telaLog.geometry('300x250')
    Label(telaLog, text='Por favor preenca as lacunas').pack()
    Label(telaLog, text='').pack()

    logUsuario = StringVar()
    logSenha = StringVar()

    Label(telaLog, text='Nome do Usuario').pack()
    logEntryusu = Entry(telaLog, textvariable=logUsuario)
    logEntryusu.pack()
    Label(telaLog, text = 'senha do usuario').pack()
    logEntrysen = Entry(telaLog, textvariable=logSenha)
    logEntrysen.pack()
    Label(telaLog, text='').pack()
    Button(telaLog, text='Login', command=confirmarLogin, width=10, height=1).pack()

def confirmarLogin():
    #Cofirma se o login esta correto
    logu = logUsuario.get()
    logs = logSenha.get()
    logEntryusu.delete(0, END)
    logEntrysen.delete(0, END)

    listaAquivo = os.listdir()
    if logu in listaAquivo:
        arquivoLog = open(logu, 'r')
        verificar = arquivoLog.read().splitlines()
        if logs in verificar:
            loginCerto()
        else:
            senhaErrada()
    else:
        usuarioErrado()

def loginCerto():
    #abre uma tela e mostra que o login esta certo
    global telaSucesso
    telaSucesso = Toplevel(tela)
    telaSucesso.title('Sucesso')
    telaSucesso.geometry('150x100')
    Label(telaSucesso,text = 'Login feito com sucesso').pack()
    Button(telaSucesso,text='Voltar', command = sair).pack()
def sair():
    #sai da tela de confirma????o de login
    telaSucesso.destroy()
def usuarioErrado():
    #abre uma tela e mostra q o usuaiio n foi achado
    global telaNE
    telaNE = Toplevel(tela)
    telaNE.title('n??o encontrado')
    telaNE.geometry('150x100')
    Label(telaNE, text='Usuario n??o encontrado').pack()
    Button(telaNE, text='Voltar', command=sair1).pack()
def sair1():
    #sai da tela de erro do usuario
    telaNE.destroy()   
def senhaErrada():
    #mabre uma tela que fala sobre a senha estar incorreta
    global telaSS
    telaSS = Toplevel(tela)
    telaSS.title('n??o encotrado')
    telaSS.geometry('150x100')
    Label(telaSS, text='senha n??o encontrada').pack()
    Button(telaSS, text='Voltar', command=sair2).pack()
def sair2():
    #sai da tela de erro da senha
    telaSS.destroy()    


mostrar_tela()



