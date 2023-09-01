from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

navegador = webdriver.Chrome()
navegador.get('https://www.google.com/intl/pt-BR/gmail/about/')
time.sleep(5)
navegador.find_element('xpath','/html/body/header/div/div/div/a[2]').click()
navegador.find_element('xpath','//*[@id="identifierId"]').send_keys('controleimobilizado@gmail.com')
navegador.find_element('xpath','//*[@id="identifierNext"]/div/button').click()
time.sleep(5)
navegador.find_element('xpath','//*[@id="password"]/div[1]/div/div[1]/input').send_keys('sicredi23')
navegador.find_element('xpath','//*[@id="passwordNext"]/div/button').click()
time.sleep(3)
navegador.find_element('xpath',"//div[text()='Compose']").click()
time.sleep(3)
navegador.find_element('By.ID',':tm').send_keys('controleimobilizado@outolook.com')
time.sleep(50)