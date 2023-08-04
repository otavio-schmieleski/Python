# pdf usar PyPDF2
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

Pasta_Originais = Path(__file__).parent / 'pdf_original'
pasta_nova = Path(__file__).parent / 'arquivos_novos'

Relatorio_bacen = Pasta_Originais / 'R20230210.pdf'

pasta_nova.mkdir(exist_ok=True)

reader = PdfReader(Relatorio_bacen) # le o pdf

print(len(reader.pages))

page0 = reader.pages[0] # pegar as pagina esta so a primeira

print(page0.extract_text()) # serve para ler o pdf

print(page0.images[0]) # para peagr as imagens
# with open(pasta_nova / page0.imagens[0], 'wb') as fp: # salvar as imagens
#     fp.write(page0.images[0].data)

# print(page0.extract_text())
# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)


for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(pasta_nova / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)  # type: ignore