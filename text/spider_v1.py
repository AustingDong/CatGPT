import os
import re
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

class Spider:

    def __init__(self) :
        self.driver = ''



    def get_answer(self):
        ans=''
        return ans



    def ask(self, text):
        pass



    def initialize(self, headless=False):
        options = Options()
        options.add_experimental_option('useAutomationExtension',False)
        options.add_experimental_option('excludeSwitches',['enable-automation'])

        if headless:
            options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=options)


    def login(self, login_info):

        user = login_info['username']
        password = login_info['password']

        self.driver.get('https://chat.openai.com/')
        html = self.driver.page_source

        try:
            identifier = self.driver.find_element_by_xpath('//*[@id="challenge-stage"]/div/input')

        except:
            print('no check')
        print(html)
        
    

    def run(self):
        text = input("Me:")
        self.ask(text)

        ans = self.get_answer()

        return ans