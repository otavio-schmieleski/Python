import sys
from typing import Optional
import PySide6.QtCore
from window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow,QApplication

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None ):
        super().__init__(parent)
        self.setupUi(self)

        text = self.lineEdit.text()
        self.pushButton.clicked.connect(self.changeLabelResult) # conectar um botao
    
    def changeLabelResult(self):
        print(self.lineEdit.text()) # printar um label
        print(123)

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()

"""
        self.finished.emit(value)


class Worker2(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def executeMe(self):
        value = '0'
        self.started.emit(value)
        for i in range(50, 100, 5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(0.3)
        self.finished.emit(value)


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)
        self.button1.clicked.connect(self.hardWork1)  # type: ignore
        self.button2.clicked.connect(self.hardWork2)  # type: ignore

    def hardWork1(self):
        self._worker = Worker1()
        self._thread = QThread()
        self._worker1 = Worker1()
        self._thread1 = QThread()

        worker = self._worker
        thread = self._thread
        # Isso garante que o widget vai ter uma referência para worker e thread
        worker = self._worker1
        thread = self._thread1

        # Mover o worker para a thread
        # Worker é movido para a thread. Todas as funções e métodos do
        # objeto de worker serão executados na thread criado pela QThread.
        worker.moveToThread(thread)

        # Run
        thread.started.connect(worker.doWork)
        # Quando uma QThread é iniciada, emite o sinal started automaticamente.
        thread.started.connect(worker.doWork)  # type: ignore

        # O sinal finished é emitido pelo objeto worker quando o trabalho que
        # ele está executando é concluído. Isso aciona o método quit da qthread
        # que interrompe o loop de eventos dela.
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        # deleteLater solicita a exclusão do objeto worker do sistema de
        # gerenciamento de memória do Python. Quando o worker finaliza, ele
        # emite um sinal finished que vai executar o método deleteLater.
        # Isso garante que objetos sejam removidos da memória corretamente.
        thread.finished.connect(thread.deleteLater)  # type: ignore
        worker.finished.connect(worker.deleteLater)

        # Aqui estão seus métodos e início, meio e fim
        # execute o que quiser
        worker.started.connect(self.worker1Started)
        worker.progressed.connect(self.worker1Progressed)
        worker.finished.connect(self.worker1Finished)

        # Inicie a thread
        thread.start()

    def worker1Started(self, value):
        self.button1.setDisabled(True)
        self.label1.setText(value)
        print('worker iniciado')
        print('worker 1 iniciado', value)

    def worker1Progressed(self, value):
        self.label1.setText(value)
        print('em progresso')
        print('1 em progresso', value)

    def worker1Finished(self, value):
        self.label1.setText(value)
        self.button1.setDisabled(False)
        print('worker finalizado')
        print('worker 1 finalizado', value)

    def hardWork2(self):
        self._worker2 = Worker1()
        self._worker2 = Worker2()
        self._thread2 = QThread()

        # Isso garante que o widget vai ter uma referência para worker e thread
        worker = self._worker2
        thread = self._thread2

        # Mover o worker para a thread
        # Worker é movido para a thread. Todas as funções e métodos do
        # objeto de worker serão executados na thread criado pela QThread.
        worker.moveToThread(thread)

        # Run
        thread.started.connect(worker.doWork)
        # Quando uma QThread é iniciada, emite o sinal started automaticamente.
        # Nome do método "doWork" modificado para "executeMe" (p/ exemplo)
        thread.started.connect(worker.executeMe)  # type: ignore

        # O sinal finished é emitido pelo objeto worker quando o trabalho que
        # ele está executando é concluído. Isso aciona o método quit da qthread
        # que interrompe o loop de eventos dela.
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        # deleteLater solicita a exclusão do objeto worker do sistema de
        # gerenciamento de memória do Python. Quando o worker finaliza, ele
        # emite um sinal finished que vai executar o método deleteLater.
        # Isso garante que objetos sejam removidos da memória corretamente.
        thread.finished.connect(thread.deleteLater)  # type: ignore
        worker.finished.connect(worker.deleteLater)

        # Aqui estão seus métodos e início, meio e fim
        # execute o que quiser
        worker.started.connect(self.worker2Started)
        worker.progressed.connect(self.worker2Progressed)
        worker.finished.connect(self.worker2Finished)

        # Inicie a thread
        thread.start()

    def worker2Started(self, value):
        self.button2.setDisabled(True)
        self.label2.setText(value)
        print('worker 2 iniciado')
        print('worker 2 iniciado', value)

    def worker2Progressed(self, value):
        self.label2.setText(value)
        print('2 em progresso')
        print('2 em progresso', value)

    def worker2Finished(self, value):
        self.label2.setText(value)
        self.button2.setDisabled(False)
        print('2 worker finalizado')
        print('worker 2 finalizado', value)

"""