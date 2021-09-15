import random
import PySimpleGUI as sg
class PassGen:
    def __init__(self):
        #layout
        sg.theme('Black')
        layout = [
            [sg.Text('Nome', size=(10,1)),
             sg.Input(key='site', size=(20,1))],
            [sg.Text('Email/Usuario',size=(10,1)),
            sg.Input(key='usuario',size=(20,1))],
            [sg.Text('Quantidade de caracteres'),sg.Combo(values=list(range(30)),
            key='total_chars',default_value=1, size=(3,1))],
            [sg.Output(size=(32,5))],
            [sg.Button('Gerar Senha')]
        ]
        #Declarar a janela
        self.janela = sg.Window('Gerador de senha', layout)

    def iniciar(self):
        while True:
            evento,valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar(nova_senha, valores)
    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%¨&*()_'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass
    def salvar(self, nova_senha, valores):
        with open('senhas.txt','a',newline='') as arquivo:
            arquivo.write(f'Nome: {valores["site"]},usuario: {valores["usuario"]}, nova senha: {nova_senha}')
        print('Arquivo Salvo')
gen = PassGen()
gen.iniciar()

