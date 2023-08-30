import cv2
from pyzbar.pyzbar import decode
from pathlib import Path
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer
ROOT_FOLDER_USUARIOS = Path(__file__).parent / 'Users.json'
ROOT_FOLDER_PRODUTOS = Path(__file__).parent / 'Cadastro_Produtos.json'

scanner_codigo_barras = None
class Scanner(QWidget):
    def __init__(self,parent = None):
        super().__init__(parent)
        camera_id = 0
        delay = 1
        window_name = 'OpenCV pyzbar'

        cap = cv2.VideoCapture(camera_id)
        autorizacao = True
        self.label = QLabel(self)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(10)
        while autorizacao:
            ret, frame = cap.read()
            if ret:
                for d in decode(frame):
                    global scanner_codigo_barras
                    scanner_codigo_barras = d.data.decode()
                    if len(scanner_codigo_barras) == 8:
                        return scanner_codigo_barras
                    frame = cv2.rectangle(frame, (d.rect.left, d.rect.top),
                                        (d.rect.left + d.rect.width, d.rect.top + d.rect.height), (0, 255, 0), 3)
                    frame = cv2.putText(frame, scanner_codigo_barras, (d.rect.left, d.rect.top + d.rect.height),
                                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
                    cv2.imshow(window_name, frame)
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

        cv2.destroyWindow(window_name)
