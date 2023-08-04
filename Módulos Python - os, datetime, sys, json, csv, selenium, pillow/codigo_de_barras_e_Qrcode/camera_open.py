# # pip install numpy
# #pip install opencv-python
# import cv2

# webcam = cv2.VideoCapture(0) # serve para conectar a webcam do computador passamos sempre o atributo 0

# if webcam.isOpened(): # serve para saber se conectou com a webcam
#     print("conectou")
#     validacao,frame = webcam.read()# serve par pegar a informacao da webcam, pega um frame da webcam
#     while validacao:
#         validacao, frame = webcam.read() # serve par pegar a informacao da webcam, pega um frame da webcam
#         cv2.imshow("imagem webcam",frame)
#         key = cv2.waitKey(5) #espera 5 milisengudos e armazena a tecla que voce apertou no teclado
#         if key == 27: # o key salva numero de tecla o numero 27 é a tecla ESC no teclado
#             break
    
#     cv2.imwrite("foto.png",frame)

# webcam.release() #ele serve para fechar completamento o arquivo para finalizar a conexao com a webcam
# cv2.destroyAllWindows() # para garantir que a imagem que aparece na tela feche completamente

# ler codigo de barras e 
import cv2
from pyzbar.pyzbar import decode

camera_id = 0
delay = 1
window_name = 'OpenCV pyzbar'

cap = cv2.VideoCapture(camera_id)

while True:
    ret, frame = cap.read()

    if ret:
        for d in decode(frame):
            s = d.data.decode()
            print(s)
            frame = cv2.rectangle(frame, (d.rect.left, d.rect.top),
                                  (d.rect.left + d.rect.width, d.rect.top + d.rect.height), (0, 255, 0), 3)
            frame = cv2.putText(frame, s, (d.rect.left, d.rect.top + d.rect.height),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)