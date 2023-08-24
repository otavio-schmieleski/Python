"""from PySide6.QtWidgets import QApplication,QPushButton,QWidget,QVBoxLayout,QMainWindow

app = QApplication()

botao = QPushButton("texto botao") # faz botao
botao.setStyleSheet('font-size: 80px') # faz o estilizacao do botao
botao.show()# exibi a janela

central_widget = QWidget() # central para adicionar no layout
layout = QVBoxLayout()
layout.addWidget(botao)


window = QMainWindow()
window.setWindowTitle('primeiro projeto') # altera o nome da janela

def slot_example(status_bar):
    status_bar.showMessage('o meu sloat foi executado')

# barra no fundo da aplicacao
status_bar = window.statusBar() # faz a barra no fundo da aplicacao
status_bar.showMessage('mostra mensagem na barra') # exbi mensagem na barra da aplicacao

# menuBar
menu = window.menuBar() # cria uma menu na parte susperior
primeiro_menu = menu.addMenu('primeiro menu') # vai adicionar um meno na tela na parte superior
primeira_acao = primeiro_menu.addAction('primeira acao') # adicionando uma acao ao menu e printando
# sempre tem que passar algum parametro
primeira_acao.triggered.connect(lambda: slot_example(status_bar)) # aqui faz uma lamba para adicar a excucao e retorna uma boolean


central_widget.show() # aparecer na tela
app.exec() # o loop da aplicacao
"""
# O básico sobre Signal e Slots (eventos e documentação)
import sys
from typing import Optional

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)

class MyWindow(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha janela bonita')

        self.botao1 = QPushButton('Texto do botão') # cria botoes
        self.botao1.setStyleSheet('font-size: 80px;') # modifica o tamanho da fonte
        self.botao1.clicked.connect(self.outro_slot)  # type:ignore

        self.botao2 = QPushButton('Botão 2') # cria botoes
        self.botao2.setStyleSheet('font-size: 40px;') # modifica o tamanho da fonte

        self.botao3 = QPushButton('Botão 3') # cria botoes
        self.botao3.setStyleSheet('font-size: 40px;') # modifica o tamonha da fonte

        self.grid_layout = QGridLayout() # cfia um grid como layout
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra')

        # menuBar
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Primeiro menu')
        self.primeira_acao = self.primeiro_menu.addAction('Primeira ação')
        self.primeira_acao.triggered.connect(self.slot_example)  # type:ignore

        self.segunda_action = self.primeiro_menu.addAction('Segunda ação')
        self.segunda_action.setCheckable(True)
        self.segunda_action.toggled.connect(self.outro_slot)  # type:ignore
        self.segunda_action.hovered.connect(self.outro_slot)  # type:ignore

    @Slot()
    def slot_example(self,status_bar):
        def inner():
            status_bar.showMessage('O meu slot foi executado')
        return inner


    @Slot()
    def outro_slot(self):
        print('Está marcado?', self.segunda_action.isChecked())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()  # O loop da aplicação

