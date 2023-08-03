# pip install numpy
#pip install opencv-python
import cv2

webcam = cv2.VideoCapture(0) # serve para conectar a webcam do computador passamos sempre o atributo 0

if webcam.isOpened(): # serve para saber se conectou com a webcam
    print("conectou")
    webcam.read() # serve par pegar a informacao da webcam, pega um frame da webcam
