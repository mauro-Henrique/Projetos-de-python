from tkinter import *
from tkinter import messagebox
class Cadastrar():
    def __init__(self):
        #Mostrar a Interface Grafica (GUI)
        self.Interface = Tk()
        ### Criação do botao
        global Senha, CPF, var1, var2, var3
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()

        #Tela Configuração
        self.Tela = self.Interface
        self.Tela.configure(bg="#00FFFF")
        self.Tela.geometry("500x600")
        self.Tela.resizable(False, False)  # Não deixa a tela mudar de tamanho
        self.Tela.minsize(width=500, height=600)

        #Botoes tela de inicio
        self.frame_1 = Frame(self.Tela, bd=4, highlightbackground="Gray", bg="Yellow", highlightthickness=3)
        self.frame_1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)
        self.Cad = Button(self.frame_1, text="Cadastrar", bd=4, bg="Green", command=lambda: self.Cadastro())
        self.Cad.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.1)
        self.Login = Button(self.frame_1, text="Logar", bd=4, bg="Green", command=lambda: self.Logar())
        self.Login.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.1)
        self.lbl1 = Label(self.frame_1, text="Conta Usuario", fg="Red", font=("Arial", 20), bg="Yellow")
        self.lbl1.place(relx=0.3, rely=0.1)
        self.Tela.mainloop()

    def Logar(self):
        self.TelaLog = Toplevel(self.Interface)
        self.TelaLog.configure(bg="#00FFFF")
        self.TelaLog.geometry("500x600")
        self.TelaLog.resizable(False, False)
        self.TelaLog.minsize(width=500, height=600)
        self.frame_2 = Frame(self.TelaLog, bd=4, highlightbackground="Gray", bg="Yellow", highlightthickness=3)
        self.frame_2.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

        # Caixa CPF
        self.lbl2 = Label(self.TelaLog, text="CPF", fg="Red", font=("Arial, 14"), bg="Yellow")
        self.lbl2.place(relx=0.4, rely=0.25)
        self.txt_CPF = Entry(self.TelaLog, textvariable=var1)
        self.txt_CPF.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.06)

        # Caixa Senha
        self.lbl4 = Label(self.TelaLog, text="Senha", fg="Red", font=("Arial, 14"), bg="Yellow")
        self.lbl4.place(relx=0.4, rely=0.4)
        self.txt_senha = Entry(self.TelaLog, textvariable=var2)
        self.txt_senha.place(relx=0.3, rely=0.45, relwidth=0.4, relheight=0.06)

        # Button Login
        self.Log2 = Button(self.TelaLog, text="Login", bd=4, bg="Green", command=lambda: self.Login_Funci())
        self.Log2.place(relx=0.33, rely=0.7, relwidth=0.3, relheight=0.05)

    def Verificar_Dados(self):
        CPF = var1.get()
        Senha = var2.get()
        if CPF == "":
            messagebox.showinfo("Erro", "Informe o CPF")
        if Senha == "":
            messagebox.showinfo("Erro", "Informe a Senha")
        else:
            for linha in self.banco:
                self.verificar = linha.rstrip().split("/")
                if self.verificar[0] == CPF and self.verificar[2] == Senha:
                    self.correto = 1
                elif self.verificar[0] != CPF:
                    self.correto = 2
                elif self.verificar[0] != Senha:
                    self.correto = 3

    def Login_Funci(self):
        CPF = var1.get()
        Senha = var2.get()
        self.banco = open("Banco de Dados.txt", "r")
        self.Verificar_Dados()
        if self.correto == 1:
            self.TelaLog_sucesso = Toplevel(self.Interface)
            self.TelaLog_sucesso.configure(bg="#00FFFF")
            self.TelaLog_sucesso.geometry("500x600")
            self.TelaLog_sucesso.resizable(False, False)
            self.TelaLog_sucesso.minsize(width=500, height=600)
            self.frame_2 = Frame(self.TelaLog_sucesso, bd=4, highlightbackground="Gray", bg="Yellow", highlightthickness=3)
            self.frame_2.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)
            self.lbl_sucesso = Label(self.TelaLog_sucesso, text="Login realizado com sucesso")
            self.lbl_sucesso.place(relx=0.5, rely=0.5)
            self.txt_CPF.delete(0, END)
            self.txt_senha.delete(0, END)
        elif self.correto == 2:
            messagebox.showerror("Erro", "CPF não encontrado")
            self.txt_CPF.delete(0, END)
            self.txt_senha.delete(0, END)
        elif self.correto == 3:
            messagebox.showerror("Erro", "Senha não encontrado")
            self.txt_CPF.delete(0, END)
            self.txt_senha.delete(0, END)

    def Cadastro(self):
        self.TelaCad = Toplevel(self.Interface)
        self.TelaCad.configure(bg="#00FFFF")
        self.TelaCad.geometry("500x600")
        self.TelaCad.resizable(False, False)
        self.TelaCad.minsize(width=500, height=600)
        self.frame_2 = Frame(self.TelaCad, bd=4, highlightbackground="Gray", bg="Yellow", highlightthickness=3)
        self.frame_2.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

        #Caixa CPF
        self.lbl2 = Label(self.TelaCad, text="CPF", fg="Red", font=("Arial, 14"), bg="Yellow")
        self.lbl2.place(relx=0.4, rely=0.15)
        self.txt_CPF = Entry(self.TelaCad, textvariable=var1)
        self.txt_CPF.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.06)

        #Caixa Email
        self.lbl3 = Label(self.TelaCad, text="Email", fg="Red", font=("Arial, 14"), bg="Yellow")
        self.lbl3.place(relx=0.4, rely=0.3)
        self.txt_email = Entry(self.TelaCad, textvariable=var3)
        self.txt_email.place(relx=0.3, rely=0.35, relwidth=0.4, relheight=0.06)

        #Caixa Senha
        self.lbl4 = Label(self.TelaCad, text="Senha", fg="Red", font=("Arial, 14"), bg="Yellow")
        self.lbl4.place(relx=0.4, rely=0.45)
        self.txt_senha = Entry(self.TelaCad, textvariable=var2)
        self.txt_senha.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.06)

        #Button Cadastrar
        self.Cad2 = Button(self.TelaCad, text="Cadastrar", bd=4, bg="Green", command=lambda: self.Cadastrar_Funci())
        self.Cad2.place(relx=0.33, rely=0.7, relwidth=0.3, relheight=0.05)

    def Cadastrar_Funci(self):
        CPF = var1.get()
        Senha = var2.get()
        Email = var3.get()

        if CPF == "":
            messagebox.showinfo("Erro", "CPF nao informado")
        elif Email == "":
            messagebox.showinfo("Erro", "Email nao informado")
        elif Senha == "":
            messagebox.showinfo("Erro", "Senha nao informada")
        else:
            self.banco = open("Banco de Dados.txt", "a")
            self.banco.writelines(CPF + "/")
            self.banco.writelines(Email + "/")
            self.banco.writelines(Senha + "\n")

            #Deletar dados da caixa de texto
            self.txt_CPF.delete(0, END)
            self.txt_email.delete(0, END)
            self.txt_senha.delete(0, END)
            self.banco.close()
