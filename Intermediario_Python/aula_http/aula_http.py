# Protocolo HTTP
# HTTP (HyperText Transfer Protocol) é um protocolo usado enviar e receber
# dados na Internet. Ele funciona no modo cliente/servidor, onde o cliente
# (seu navegador, por exemplo) faz uma requisição ao servidor
# (site, por exemplo), que responde com os dados adequados.
#
# A mensagem de requisição do cliente deve incluir dados como:
# - O método HTTP
#     - leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (métodos suportados)
#     - escrita - POST, PUT (substitui), PATCH (atualiza), DELETE
# - O endereço do recurso a ser acessado (/users/)
# - Os cabeçalhos HTTP (Content-Type, Authorization)
# - O Corpo da mensagem (caso necessário, de acordo com o método HTTP)
#
# A mensagem de resposta do servidor deve incluir dados como:
# - código de status HTTP (200 success, 404 Not found, 301 Moved Permanently)
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# - Os cabeçalhos HTTP (Content-Type, Accept)
# - O corpo da mensagem (Pode estar em vazio em alguns casos)

# para iniciar o http para servir algum site
#python -m http.server -d Intermediario_Python\\aula_http/ porta(ex:3000) no terminal
import requests
from bs4 import BeautifulSoup

# http:// -> 80
# https:// -> 443

url = "http://localhost:3001/" # url do site com a porta

response = requests.get(url)# serve para pegar a resposta no servidor ou site com o requests.get()
print(response.status_code)

# web scraping pegar informacoes da internet
raw_thml = response.text # pega as informacoes da pagina em formato de texto html
print(raw_thml)
parsed_html = BeautifulSoup(raw_thml,'html.parser', from_encoding='utf-8') # pega o html da pagina e salva na variavel
print(parsed_html.title.text) # vai printar o titulo da pagina title
