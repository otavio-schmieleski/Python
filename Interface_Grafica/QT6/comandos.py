from PyQt6.QtGui import QIcon,QFont,QPixmap
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
import sys

from PyQt6.QtWidgets import QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()

        #CONFIGURACOES PADROES DA JANELA
        self.setGeometry(200,200,400,400) # posicao da tela 
        self.setWindowTitle('Primeiro Programa') # muda titulo da tela
        self.setWindowIcon(QIcon('imagem.jpg')) # coloca a imagem de icone
        self.setMaximumWidth(1200) # maximo da janela
        self.setMinimumHeight(600) # maximo da janela
        #self.setStyleSheet('background-color: black') # altera a cor da janela

        #LABEL
        label = QLabel(self) # criacao de label
        label.setText('hello word') # escrevendo no label
        label.move(120,30) # move o label na tela
        label.setFont(QFont('Sanserif', 20)) # altera a fonte
        label.setStyleSheet('color: red') # altera a cor 
        label.clear() # limpa o label
        #pixmap = QPixmap('endereco da imagem') # pega a imagem
        #label.setPixmap(pixmap) # coloca de fundo no label

        #BOTAO
        btn = QPushButton('titulo',self) 
        btn.setFont('times',25) # altera a font e tamanho
        btn.setStyleSheet('background-color: black') # altera a cor do botao
        #btn.setIcon(QIcon('endereco')) # passa um icone para o botao
        btn.clicked.connect('passa o paramentro ou funcao') # pegando o envento do botao

        #LINE_EDIT
        line_edit = QLineEdit()
        line_edit.setFont('time') # muda a fonte do line
        line_edit.setPlaceholderText('digite seu nome') # fica de fundo do line_edit
        line_edit.setText('digite um textoo que ja vai por padrao') # fica predefinido já
        line_edit.setEchoMode(QLineEdit.EchoMode.Password) # deixa o formato com *** de senha
        
        #LAYOUT E GRID
        hbox = QBoxLayout() # coloca na horizontal os elementos
        vbox = QVBoxLayout() # coloca na vertical os elementos
        btn1 = QPushButton()
        line1 = QLineEdit()
        line2 = QLineEdit()
        hbox.addWidget(btn1) # adiciona a tela
        hbox.addWidget(line1)# adiciona a tela
        hbox.addWidget(line2)# adiciona a tela
        vbox.addWidget(btn1)# adiciona a tela
        vbox.addWidget(line1)# adiciona a tela
        vbox.addWidget(line2)# adiciona a tela

        # BOTAO RADIO
        rad1 = QRadioButton('whtasapp') # faz botao de selecao redondo
        rad1.toggleed.connect('funcao ') # para conectar o botao do tipo radio
        rad1.sender() #passa se esta selecionado o botao

        # BOTAO DE CHECKBOX
        check1 = QCheckBox() # seleciona mais de uma opcao
        check1.setText('instagram')
        check1.toggle.connect('passa funcao') # serve para vincular uma execucao
        check1.isChecked() # serve para saber se esta selecionado ou nao

        #SPIN BOX QUE CLICA E AUMANTA O NUMERO
                            #valor inicial  #valor maximo #valor minimo #prefizado na parte da frente
        self.spin = QSpinBox(self,value = 2, maximum = 10, minumun =1, prefix ='#', suffix='pizzas')
                                                                                    #escrita na tela do lado
        self.spin.valueChanged.connect()# serve para toda vez que mudar o valor da spin chmar a funcao

        #COMBO BOX
        self.combo = QComboBox()
        self.combo.addItem('mussarela') # adiciona ao comboBox um de cada vez
        sabores = ['calabresa,catupry,frango']
        self.combo.addItems(sabores) # adiciona a lista a comboBox
        self.combo.currentTextChanged() # ele passa o sinal de qual esta selecionado

        #Lista
        self.list = QListWidget()
        self.list.addItem('mussarela') # adiciona a lista que sera exibido na tela
        self.list.clicked.connect() # manda o que esta selecionado
        texto =self.list.currentItem() # pega o item so nao esta em str
        texto.text() # aqui sim pega o str da lista

        #Table
        table = QTableWidget()
        table.setRowCount(10) # defini o tamanho da tabela das linhas
        table.setColumnCount(4) # defini o tamanho das colunas
        table.setItem(0,0, QTableWidgetItem('id')) # adiciona item a tabela
        table.setItem(0,0, QTableWidgetItem('nome')) # adiciona item a tabela
        table.setItem(0,0, QTableWidgetItem('produto')) # adiciona item a tabela
        table.setItem(0,0, QTableWidgetItem('cod_barra')) # adiciona item a tabela
        # da para utilizar o for no lugar do primeiro 0 e do segundo 0

        







        


app = QApplication(sys.argv)
window = Window() # janela
window.show()
sys.exit(app.exec())