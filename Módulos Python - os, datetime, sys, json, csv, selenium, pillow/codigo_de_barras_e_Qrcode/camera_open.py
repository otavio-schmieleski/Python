# pip install numpy
#pip install opencv-python
import cv2

webcam = cv2.VideoCapture(0) # serve para conectar a webcam do computador passamos sempre o atributo 0

if webcam.isOpened(): # serve para saber se conectou com a webcam
    print("conectou")
    validacao,frame = webcam.read()# serve par pegar a informacao da webcam, pega um frame da webcam
    while validacao:
        validacao, frame = webcam.read() # serve par pegar a informacao da webcam, pega um frame da webcam
        cv2.imshow("imagem webcam",frame)
        key = cv2.waitKey(5) #espera 5 milisengudos e armazena a tecla que voce apertou no teclado
        if key == 27: # o key salva numero de tecla o numero 27 é a tecla ESC no teclado
            break
    
    cv2.imwrite("foto.png",frame)

webcam.release() #ele serve para fechar completamento o arquivo para finalizar a conexao com a webcam
cv2.destroyAllWindows() # para garantir que a imagem que aparece na tela feche completamente