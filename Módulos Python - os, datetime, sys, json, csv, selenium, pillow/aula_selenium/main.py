from pathlib import Path
import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

ROOT_FLODER = Path(__file__).parent # caminho para pasta do projeto
CHROMEDRIVER_EXEC = ROOT_FLODER / 'drivers' / 'chromedriver.exe' # caminho para a pasta dos drivers

chrome_options =webdriver.ChromeOptions() # opcoes se quiser colocar
chrome_service =Service(executable_path=CHROMEDRIVER_EXEC) # é o servico que sera atualizado
chrome_browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_options) # chrome que utilizaremos

chrome_browser.get('https://www.google.com.br/') # serve para abrir uma pagina no navegador
time.sleep(5) # serve para aguardar 30 segundos o chrome aberto

# --headless serve para nao mostrar o chrome na tela

# escreve na tela o elemto em xpath
chrome_browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys('otavio schmieleski')
# usando o Keys.ENTER e da enter no objeto escolhido
chrome_browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys(Keys.ENTER)
# pegar o resultado da tela inteira
results = chrome_browser.find_element(By.ID,'search')
# vai pegar os link da pagina de results que havia selecionado e pegar apenas as teag a = a href sao os links em html
links = results.find_elements(By.TAG_NAME, 'a')
# aqui vai clicar no primeiro link
links[0].click()
time.sleep(5) # deixa um tempo esperando