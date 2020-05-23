import PySimpleGUI as sg
import matplotlib.pyplot as plt

from telaGrafico import TelaGrafico

class TelaPython:



    def __init__(self):

        self.grafico = TelaGrafico ()
        sg.change_look_and_feel('Darkamber')
        #Layout
        layoutDados = [
            [sg.Text('Ponto 1   X', size=(8,0)), sg.InputText('0', size=(10,0), key='x1', focus=True), sg.Text('Y', size=(2,0)), sg.InputText('0', size=(10,0), key='y1'),
             sg.Text('Ponto 2   X', size=(8,0)), sg.InputText('0', size=(10,0), key='x2'), sg.Text('Y', size=(2,0)), sg.InputText('0', size=(10,0), key='y2')],
            [sg.Text('Ponto 3   X', size=(8,0)), sg.InputText('0', size=(10,0), key='x3'), sg.Text('Y', size=(2,0)), sg.InputText('0', size=(10,0), key='y3'),
             sg.Text('Ponto 4   X', size=(8,0)), sg.InputText('0', size=(10,0), key='x4'), sg.Text('Y', size=(2,0)), sg.InputText('0', size=(10,0), key='y4')],
            [sg.Ok('Desenhar', size=(10,1), font='Arial-black'), sg.Cancel('Sair', size=(10,1), font='Arial-black')]
        ]
        #Janela
        self.janela = sg.Window('Atividade Computação Gráfica: Os 4 pontos', size=(600,400)).layout(layoutDados)
        #Extrair dados da tela
        #self.button, self.values = janela.Read()
        while True:
            self.event, self.values = self.janela.read()
            if self.event is None or self.event == 'Sair':
                break
                window.close()

            if self.event is None or self.event == 'Desenhar':
                #ponto 1
                self.x1 = self.values['x1']
                self.y1 = self.values['y1']

                # ponto 2
                self.x2 = self.values['x2']
                self.y2 = self.values['y2']

                # ponto 3
                self.x3 = self.values['x3']
                self.y3 = self.values['y3']

                # ponto 4
                self.x4 = self.values['x4']
                self.y4 = self.values['y4']

                fig = plt.figure()

                self.vx = [self.x1, self.x2, self.x3, self.x4]
                self.vy = [self.y1, self.y2, self.y3, self.y4]

                # verificar maximo axis X e Y
                self.maximoX = '0'
                self.maximoY = '0'

                if self.x1 > self.maximoX:
                    self.maximoX = self.x1
                if self.x2 > self.maximoX:
                    self.maximoX = self.x2
                if self.x3 > self.maximoX:
                    self.maximoX = self.x3
                if self.x4 > self.maximoX:
                    self.maximoX = self.x4

                if self.y1 > self.maximoY:
                    self.maximoY = self.y1
                if self.y2 > self.maximoY:
                    self.maximoY = self.y2
                if self.y3 > self.maximoY:
                    self.maximoY = self.y3
                if self.y4 > self.maximoY:
                    self.maximoX = self.y4

                # vereficar minimo axis X e Y

                self.minimoX = '0'
                self.minimoY = '0'

                if self.x1 < self.minimoX:
                    self.minimoX = self.x1
                if self.x2 < self.minimoX:
                    self.minimoX = self.x2
                if self.x3 < self.minimoX:
                    self.minimoX = self.x3
                if self.x4 < self.minimoX:
                    self.minimoX = self.x4

                if self.y1 < self.minimoY:
                    self.minimoY = self.y1
                if self.y2 < self.minimoY:
                    self.minimoY = self.y2
                if self.y3 < self.minimoY:
                    self.minimoY = self.y3
                if self.y4 < self.minimoY:
                    self.minimoY = self.y4

                self.mxX = (float(self.maximoX) + 10)
                self.mnX = (float(self.minimoX) - 10)
                self.mxY = (float(self.maximoY) + 10)
                self.mnY = (float(self.minimoY) - 10)

                ax = fig.add_subplot(1, 1, 1)
                ax.spines['left'].set_position('zero')
                ax.spines['right'].set_color('none')
                ax.spines['bottom'].set_position('zero')
                ax.spines['top'].set_color('none')
                ax.xaxis.set_ticks_position('bottom')
                ax.yaxis.set_ticks_position('left')
                ax.annotate('Ponto 1', (int(self.x1), int(self.y1)))
                ax.annotate('Ponto 2', (int(self.x2), int(self.y2)))
                ax.annotate('Ponto 3', (int(self.x3), int(self.y3)))
                ax.annotate('Ponto 4', (int(self.x4), int(self.y4)))



                plt.axis([self.mnX, self.mxX, self.mnY, self.mxY])
                plt.scatter([int(self.x1),int(self.x2), int(self.x3), int(self.x4)], [int(self.y1), int(self.y2), int(self.y3), int(self.y4)], color='green')
                #plt.show()
                plt.savefig('./graphic')

                self.grafico.mostragrafico()
tela = TelaPython()
