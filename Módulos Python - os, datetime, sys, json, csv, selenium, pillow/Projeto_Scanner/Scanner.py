#import cv2
#from pyzbar.pyzbar import decode
from pathlib import Path
import json
ROOT_FOLDER_USUARIOS = Path(__file__).parent / 'Users.json'
ROOT_FOLDER_PRODUTOS = Path(__file__).parent / 'Cadastro_Produtos.json'

scanner_codigo_barras = None
class Scanner:
    def __init__(self):
        camera_id = 0
        delay = 1
        window_name = 'OpenCV pyzbar'

        cap = cv2.VideoCapture(camera_id)
        autorizacao = True
        while autorizacao:
            ret, frame = cap.read()

            if ret:
                for d in decode(frame):
                    global scanner_codigo_barras
                    scanner_codigo_barras = d.data.decode()
                    print(scanner_codigo_barras)
                    if len(scanner_codigo_barras) == 8:
                        try:
                            with open(ROOT_FOLDER_PRODUTOS, 'r', encoding='utf-8') as file:
                                banco_produtos = json.load(file)
                            list(banco_produtos)
                        except FileNotFoundError:
                            pass
                        for codigo in  banco_produtos:
                            if scanner_codigo_barras == codigo['cod_barra']:
                                try:
                                    Ag = int(input('Deseja Transferir para qual Agencia: '))
                                    if Ag >= 1 and Ag <= 31:
                                        self.ag = Ag
                                        codigo['ag'] = self.ag
                                        with open(ROOT_FOLDER_PRODUTOS, 'w', encoding='utf-8') as file:
                                            json.dump(banco_produtos,file,ensure_ascii=False,indent=2)
                                        print('Trasnferencia feita com Sucesso!!')
                                        break
                                except TypeError and ValueError:
                                    print('Informe uma agencia valida')
                                    Scanner()
                                    pass
                            else:
                                continue
                        autorizacao = False
                        break
                    frame = cv2.rectangle(frame, (d.rect.left, d.rect.top),
                                        (d.rect.left + d.rect.width, d.rect.top + d.rect.height), (0, 255, 0), 3)
                    frame = cv2.putText(frame, scanner_codigo_barras, (d.rect.left, d.rect.top + d.rect.height),
                                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.imshow(window_name, frame)
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

        cv2.destroyWindow(window_name)
