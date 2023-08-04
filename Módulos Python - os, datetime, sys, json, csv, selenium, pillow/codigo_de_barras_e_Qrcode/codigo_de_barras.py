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



# ler QRCODE
# Este exemplo de código demonstra como ler o código QR em Python.
import aspose.barcode as barcode

# Carregar imagem do código QR
reader = barcode.barcoderecognition.BarCodeReader("qrcode_python.png")

# Ler códigos QR
recognized_results = reader.read_bar_codes()

# Mostrar resultados
for x in recognized_results:
    print("Code Text: " + x.code_text)
    print("Type: " + x.code_type_name)