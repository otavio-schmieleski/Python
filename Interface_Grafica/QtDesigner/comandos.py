# para converter o ui em py, temos que entrar na pasta onde esta salva o ui e digitar o seguinte comando no terminal:
#pyside6-uic nome-do-arquivo.ui -o nome-do-arquivo-escolhido.py

"""
    import sys
    from typing import Optional
    import PySide6.QtCore
    from window import Ui_MainWindow
    from PySide6.QtWidgets import QMainWindow,QApplication

    class MainWindow(QMainWindow,Ui_MainWindow):
        def __init__(self, parent=None ):
            super().__init__(parent)
            self.setupUi(self)

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()
        app.exec()

padrao de procedimento para subir a tela
"""