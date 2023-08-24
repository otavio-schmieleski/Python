from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE,TEXT_MARGIN,MINIMUM_WIDTH,SMALL_FONT_SIZE,PRIMARY_COLOR,\
    DARKER_PRIMARY_COLOR,DARKEST_PRIMARY_COLOR,MEDIUM_FONT_SIZE
from utils import isEmpty,isNumOrDot,isValidNumber
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget,QPushButton,QGridLayout

class Display(QLineEdit):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')  #configurar o tamanho da fonte
        self.setMinimumHeight(BIG_FONT_SIZE * 2) # sempre colocar um dobro de height do size
        self.setMinimumWidth(MINIMUM_WIDTH) # tamanho maximo de comprimento
        self.setAlignment(Qt.AlignmentFlag.AlignRight) # alinha o elemento a direita da tela
        self.setTextMargins(TEXT_MARGIN,TEXT_MARGIN,TEXT_MARGIN,TEXT_MARGIN) # desempactodando a margem
    

class Info(QLabel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
    def confgSytle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;') # confg tamanho
        self.alignment(Qt.AlignmentFlag.AlignRight) # config ´posicao a direita da tela

class Button(QPushButton):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.configSytle()

    def configSytle(self):
        self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px;')
        self.setMinimumSize(75,75)

class ButtonGrid(QGridLayout):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self._makeGrid()

    def _makeGrid(self):
        for i,row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                button = Button(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'SpecialButton')
                self.addWidget(button,i,j)

    def _makeButtonDisplayConnection(self,func,*args,**kwargs):

        ...
    def _insertButtonTextToDisplay(self,checked,button):
        ...