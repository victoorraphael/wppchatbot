import os
import time
import re
import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup


class wppbot:
    dir_path = os.getcwd()

    def __init__(self, nome_bot):
        print('Iniciado')
        #self.chrome = self.dir_path+'/chromedriver_linux64.zip'
        #self.options = webdriver.ChromeOptions()
        # self.options.add_argument(
        #     r"user-data-dir="+self.dir_path+"/profile/wpp")
        # self.driver = webdriver.Chrome(
        #     self.chrome, chrome_options=self.options)

    def inicia(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://web.whatsapp.com/')
        self.driver.implicitly_wait(15)

    def escuta(self):
        #post = self.driver.find_element_by_tag_name('body').text
        # ultimo = len(post) - 1
        # texto = post[0].find_element_by_css_selector(
        #    'span.selectable-text').text
        try:
            # post = self.driver.find_element_by_xpath(
            #     '//*[@id="main"]/div[3]/div/div/div[3]/div[16]/div/div/div/div[1]/div/span/span').text
            # //*[@id="main"]/div[3]/div/div/div[3]/div[16]/div/div/div/div[1]/div/span/span
            post = self.driver.find_elements_by_class_name('FTBzM')
            ultimo = len(post) - 1
            #Vamos pegar o  texto da última conversa e retornar.
            texto = post[ultimo].find_element_by_css_selector('span.selectable-text').text
            return texto
        except:
            return 'ainda nada encontrado'
    
    #def responde(self):
    def responde(self,resposta):
        
        response = str(resposta)
        #Setamos caixa de mensagens preenchemos com a resposta e clicamos em enviar.
        self.caixa_de_mensagem = self.driver.find_element_by_class_name('_3FeAD')
        self.caixa_de_mensagem.send_keys(response)
        time.sleep(1)
        self.botao_enviar = self.driver.find_element_by_class_name('_3M-N-')
        self.botao_enviar.click()