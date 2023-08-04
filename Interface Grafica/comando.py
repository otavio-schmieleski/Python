from PySide6.QtWidgets import QApplication,QPushButton,QWidget,QVBoxLayout

app = QApplication()

botao = QPushButton("texto botao") # faz botao
botao.setStyleSheet('font-size: 80px') # faz o estilizacao do botao
botao.show()# exibi a janela

central_widget = QWidget() # central para adicionar no layout
layout = QVBoxLayout()
layout.addWidget(botao)
central_widget.show()
app.exec()