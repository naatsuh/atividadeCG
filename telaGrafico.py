import PySimpleGUI as sg

class TelaGrafico:

    def mostragrafico(self):
        sg.change_look_and_feel('Darkamber')
        # Layout
        layoutg = [
            [sg.Image(r'./graphic.png')],
            [sg.Cancel('Sair', size=(10, 1), font='Arial-black')]
        ]
        # Janela
        window = sg.Window('Atividade Computação Gráfica: Os 4 pontos').layout(layoutg)
        # Extrair dados da tela
        # self.button, self.values = janela.Read()
        while True:
            event, values = window.read()
            if event is None or event == 'Sair':
                break
        window.close()
