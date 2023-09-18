import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime
from pathlib import Path
import json

ROOT_FOLDER_TEMP = Path(__file__).parent / 'temp.json'

class Email_Automatico():

    def __init__(self,Assunto,name,agencia):
        self.assunto = Assunto
        self.nome = name
        self.ag = agencia
        try:
            with open(ROOT_FOLDER_TEMP, 'r', encoding='utf-8') as file:
                banco_produtos = json.load(file)
            list(banco_produtos)
        except FileNotFoundError:
            pass
        # configurango o navegador
        navegador = webdriver.Chrome()
        navegador.maximize_window()
        # abrindo o outlook
        navegador.get('https://outlook.live.com/owa/')
        time.sleep(2)

        # inserindo o e-mail
        navegador.find_element('xpath','/html/body/header/div/aside/div/nav/ul/li[2]/a').click()
        navegador.find_element('xpath','//*[@id="i0116"]').send_keys('controle_de_imobilizados@outlook.com')
        navegador.find_element('xpath','//*[@id="idSIButton9"]').click()
        time.sleep(1)

        #inserindo a senha
        navegador.find_element('xpath','//*[@id="i0118"]').send_keys('controle_imobilizados')
        navegador.find_element('xpath','//*[@id="idSIButton9"]').click()
        time.sleep(2)

        #pulando notificacao
        navegador.find_element('xpath','//*[@id="idBtn_Back"]').click()
        time.sleep(2)

        # iniciando novo e-mail
        navegador.find_element('xpath','//*[@id="innerRibbonContainer"]/div[1]/div/div/div/div[1]/div/span/button[1]').click()
        time.sleep(3)

        # configurando o endereco que recebera o e-mail
        pyautogui.write('controle_de_imobilizados')
        pyperclip.copy("@")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.write('outlook.com')
        pyautogui.press('enter',interval=0.1,presses=1)

        # escrevendo o assunto 
        pyautogui.press('tab', interval=.01, presses=1)
        pyautogui.write(f'{self.assunto}')

        # escrevendo o corpo do e-mail
        pyautogui.press('tab',interval=0.1, presses=1)

        # pegando o horario para ver se manda bom dia ou boa tarde
        horario = datetime.today().strftime('%H')
        dia = datetime.today().strftime('%d/%m/%y')
        fuso_horario = datetime.today().strftime('%H:%M:%S')
        # configurando horario e enviando mensagem
        if horario <= '12':
            pyautogui.write(f'Bom dia Controle de Imobilizado')
            pyautogui.press('enter',interval=0.1, presses=1)
            pyautogui.write(f'o usuario {self.nome} na data do dia {dia}, no horario {fuso_horario}, Pediu alteração nos seguintes Produtos:')
            pyautogui.press('enter',interval=0.1,presses=2) 
            for i,item in enumerate(banco_produtos):
                pyautogui.write(f'Produto: {item["name"]}  |  Ag: {item["ag"]}  |  CODIGO DE BARRAS: {item["cod_barra"]}')
                pyautogui.press('enter',interval=0.1,presses=2)
            navegador.find_element('xpath','//*[@id="docking_InitVisiblePart_0"]/div/div[2]/div[1]/div/span/button[1]').click()
            time.sleep(3)
        else:
            pyautogui.write(f'Boa Tarde Controle de Imobilizado')
            pyautogui.press('enter',interval=0.1, presses=1)
            pyautogui.write(f'o usuario {self.nome} na data do dia {dia}, no horario {fuso_horario}, Pediu alteração nos seguintes Produtos:')
            pyautogui.press('enter',interval=0.1,presses=2) 
            for i,item in enumerate(banco_produtos):
                pyautogui.write(f'Produto: {item["name"]}  |  Ag: {item["ag"]}  |  CODIGO DE BARRAS: {item["cod_barra"]}')
                pyautogui.press('enter',interval=0.1,presses=2)
            navegador.find_element('xpath','//*[@id="docking_InitVisiblePart_0"]/div/div[2]/div[1]/div/span/button[1]').click()
            time.sleep(3)
