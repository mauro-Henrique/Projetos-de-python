from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class login:
    def __init__(self, root):
        self.root = root
        self.root.title('Sistema de login')
        self.root.geometry('1199x600+100+50')
        self.root.resizable(False, False)
        #imagem
        #self.bg = ImageTk.PhotoImage(file="plateleira.jpg")
        #self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        #login frame
        frameLogin = Frame(self.root, bg='white')
        frameLogin.place(x=330,y=150,width=500,height=400)
        #titulo
        title = Label(frameLogin, text='Sitema de login',font=('impact',30,'bold'),
                      fg='#6164FF',bg='white').place(x=90, y=30)
        # Usuario
        usuario = Label(frameLogin, text='Escreva o nome', font=('Goudy old style', 15, 'bold'),
                      fg='grey', bg='white').place(x=90, y=140)
        self.usuario = Entry(frameLogin, font=('Goudy old style', 15, 'bold'),
                           bg='#E7E6E6')
        self.usuario.place(x=90, y=170, width=320,height=35)
        #Senha
        senha = Label(frameLogin, text='Escreva sua senha', font=('Goudy old style', 15, 'bold'),
                        fg='grey', bg='white').place(x=90, y=210)
        self.senha = Entry(frameLogin, font=('Goudy old style', 15, 'bold'),
                             bg='#E7E6E6')
        self.senha.place(x=90, y=240, width=320, height=35)
        # Botão
        esqueceu = Button(frameLogin, text='Esqueceu sua senha',bd=0,cursor="hand2",  font=('Goudy old style', 12, 'bold'),
                      fg='#6162FF', bg='white').place(x=90, y=280)
        submeter = Button(frameLogin,command=self.checar,cursor="hand2", text='fazer login', bd=0, font=('Goudy old style', 15, 'bold'),
                          bg='#6162FF', fg='white').place(x=90, y=320, width=180,height=40)
    def checar(self):
        if self.usuario.get()=="" or self.senha.get()=="":
            messagebox.showerror('erro','precisa preencher todos os espaços',parent=self.root)
        elif self.usuario.get() != "1234" or self.senha.get() != "1234":
            messagebox.showerror('erro', 'nome e senha invalidos',parent=self.root)
        else:
            messagebox.showinfo('bem, vindo',f"bem vindo{self.usuario.get()}")

root = Tk()
obj = login(root)
root.mainloop()