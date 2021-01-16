from password_generator import PasswordGenerator
from user_generator import UserGenerator
import PySimpleGUI as sg

class Generator():
    def iniciar(self):
        sg.theme('DarkGrey13')

        self.layout = [
            [sg.Text('Escolha a opção que deseja gerar: ')],
            [sg.Button('Gerar Usuário'), sg.Button('Gerar Senha'), sg.Button('Sair')]
        ]

        self.janela = sg.Window('Gerador de Usuário e Senhas', layout=self.layout)

        while True:
            self.eventos, self.valores = self.janela.Read()
            if self.eventos == 'Sair':
                break

            if self.eventos == 'Gerar Usuário':
                usu = UserGenerator()
                usu.iniciar()
            
            elif self.eventos == 'Gerar Senha':
                sen = PasswordGenerator()
                sen.iniciar()

# Teste
g = Generator()
g.iniciar()
