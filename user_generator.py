from random import randint
import requests
import PySimpleGUI as sg

class UserGenerator():

    sg.theme('DarkGrey13')
    
    def __init__(self):
        self.url = "https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"

        self.headers = {'User-Agent': 'Chrome/61.0.3.3163.100'}

    def iniciar(self):
        self.r = requests.get(self.url, headers=self.headers)
        self.texto = self.r.text

        self.palavras = self.texto.split()

        self.layout = [
            [sg.Text('============ Gerar Usuário Aleatório ============')],
            [sg.Button('Gerar'), sg.Button('Sair')],
            [sg.Output()]
        ]

        self.janela = sg.Window('Gerar Usuário aletório!', layout=self.layout)


        while True:
            self.evento, self.valores = self.janela.Read()
            if self.evento == 'Sair':
                break

            self.num = randint(0, len(self.palavras))
            self.usuarios = self.palavras[self.num] + str(self.num)
            print(self.usuarios)
