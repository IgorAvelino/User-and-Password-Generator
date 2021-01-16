import random, PySimpleGUI as sg

class PasswordGenerator():

    sg.theme('DarkGrey13')

    def __init__(self):
        self.letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.letras_minusculas = self.letras_maiusculas.lower()
        self.digitos = "0123456789"
        self.simbolos = "!@#$%¨&*()[]{\/}~^;:.,|+=-"
        self.comprimento = 12
        self.tudo = ""
        self.tudo += self.letras_maiusculas
        self.tudo += self.letras_minusculas

    def iniciar(self):
        self.layout = [
            [sg.Text('============ Gerar Senhas Aleatoriamente!! ============')],
            [sg.Radio('Números','grupo1', key='numeros')],
            [sg.Radio('Símbolos','grupo2', key='simbolos')],
            [sg.Button('Gerar'), sg.Button('Sair')],
            [sg.Output()]
        ]

        self.janela = sg.Window('Password Generator', layout=self.layout)

        while True:
            self.eventos, self.valores = self.janela.Read()
            if self.eventos == 'Sair':
                break

            if self.valores['numeros']:
                self.tudo += self.digitos
            
            if self.valores['simbolos']:
                self.tudo += self.simbolos
            
            self.senha = "".join(random.sample(self.tudo, self.comprimento))
            print(self.senha)
