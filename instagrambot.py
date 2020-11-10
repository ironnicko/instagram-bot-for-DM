from selenium import webdriver
import os
import time
import getpass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


usern = input('Username of the person you want to send message >>')


class bot:
    def __init__(self, user):
        self.username = input('enter your username')
        self.password = getpass.getpass('enter your password')
        self.user = user
        self.base_url = 'https://www.instagram.com/'
        try:
            self.bot = webdriver.Chrome(os.getcwd()+"/chromedriver")
        except:
            self.bot = webdriver.Chrome(os.getcwd()+r'\chromedriver.exe')
        self.login()


    def login(self):
        self.bot.get(self.base_url)
        
        enter_username = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)
        self.bot.get("https://www.instagram.com/direct/inbox")
        self.bot.find_element_by_xpath("//*[contains(@class, 'aOOlW   HoLwm ')]").click()
        self.bot.find_element_by_xpath('//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Direct"]').click()
        time.sleep(3)
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button').click()
        time.sleep(2)
        self.bot.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(self.user)
        time.sleep(2)
        self.bot.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div').click()
        time.sleep(2)
        self.bot.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
        time.sleep(2)
        while True:
            message = input('Enter your message')
            self.bot.find_element_by_css_selector('textarea[placeholder="Message..."]').send_keys(message)
            time.sleep(1)
            self.bot.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

def init():     
    bot(usern)
    input("DONE")

init()
