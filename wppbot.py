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

    def inicia(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://web.whatsapp.com/')
        self.driver.implicitly_wait(15)

    def escuta(self):
        post = self.driver.find_element_by_tag_name('html').text
        # ultimo = len(post) - 1
        # texto = post[0].find_element_by_css_selector(
        #    'span.selectable-text').text
        return post
