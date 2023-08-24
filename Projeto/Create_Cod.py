#pip install python-barcode para usar no codigo de barras
#pip install pillow para manipular imagens com o codigo de barras

from barcode import EAN8  # padrao de codigos de barras
from barcode.writer import ImageWriter # serve para salver em outro tipo de arquivo

# este padrao EAN13 tem que passar 12 digitos, assim que cria codigo de barra
codigo_de_barra = EAN8("12312312",writer=ImageWriter()) # e o writer é para salvar em png a imagem

codigo_de_barra.save("codigo_barra") # serve para salva o codigo de barras

codigos_produtos = {
    "feijao" : "12345678",
    "Arroz": "12345678"
}

# faz um for para criar o codigo de barras dos codigos_produtos
for i in codigos_produtos:
    codigo = codigos_produtos[i] # pega o codigo que passamos na parte de cima
    codigo_de_barras_auto = EAN8(codigo,writer=ImageWriter())
    codigo_de_barras_auto.save(f"codigo_barra{i}") # salva com o nome do codigo

"""
QRCODE AGORA
pip install qrcode para usar cim QRcode
"""
import qrcode

imagem_qr = qrcode.make("https://github.com/otavio-schmieleski") # esta criando a imagem do qrcode com o link
imagem_qr.save("qrcode_python.png") # para salvar no qrcode passa a extensao do arquivo