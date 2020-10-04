from selenium import webdriver
from getpass import getpass
import requests
import time
from free2 import Free
import random
import re,os
from free2 import Free
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
  os.system("clear")
except:
  pass
##########color#############
def prRed(skk): 
  print("\033[91m {}\033[00m" .format(skk),end="") 
def prGreen(skk):
 print("\033[92m {}\033[00m" .format(skk),end="") 
def prYellow(skk): 
  print("\033[93m {}\033[00m" .format(skk),end="") 
def prLightPurple(skk): 
  print("\033[94m {}\033[00m" .format(skk),end="") 
def prPurple(skk):
  print("\033[95m {}\033[00m" .format(skk),end="") 
def prCyan(skk): 
  print("\033[34m {}\033[00m" .format(skk),end="") 
def prLightGray(skk): 
  print("\033[97m {}\033[00m" .format(skk),end="") 
def prBlack(skk): 
  print("\033[98m {}\033[00m" .format(skk),end="") 
prCyan('''
    "welcome to my free fire cracking tool"
''')
prRed('''

 ______ _______ ______         _____  __   _ _______
  ____/ |______ |     \       |     | | \  | |______
 /_____ |______ |_____/ _____ |_____| |  \_| |______
                                                    

''')

class FacebookLogin():
    def __init__(self, email, password, browser='Chrome'):
        # Store credentials for login
        self.email = email
        self.password = password
        if browser == 'Chrome':
            # Use chrome
            self.driver = webdriver.Chrome(drive)
        elif browser == 'Firefox':
            # Set it to Firefox
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get(LOGIN_URL)
        time.sleep(1) # Wait for some time to load



    def login(self):
        email_element = self.driver.find_element_by_id('email')
        email_element.send_keys(self.email) # Give keyboard input

        password_element = self.driver.find_element_by_id('pass')
        password_element.send_keys(self.password) # Give password as input too

        login_button = self.driver.find_element_by_id('loginbutton')
        login_button.click() # Send mouse click
        time.sleep(6) # Wait for 2 seconds for the page to show up
        ACCESS_URL= self.driver.current_url
        self.driver.quit()
        prYellow('[-] ')
        print('the url is', end= '')
        prYellow(": ")
        print(ACCESS_URL)
        s=0
        prYellow("[-] ")
        print("follow the video to add the access token:")
        token=getpass("enter the token: ")
        Free(drive,token=token).exploiting()
        
if __name__ == '__main__':
    email= input("input your email: ")
    password= getpass("input your password: ")
    try:
       with open("chromedriver.txt",'r') as f:
          drive=(f.readlines())
       driver= webdriver.Chrome(drive)
    except:   
       drive=input("webdriver path: ")
       with open("chromedriver.txt",'w') as f:
           f.writelines(drive)
       driver= webdriver.Chrome(drive)

    # Enter your login credentials here
    browser=driver.get("https://reward.ff.garena.com/")
    free_log=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, '//span[@class="btn-item facebook"]')))
    free_log.click()
    LOGIN_URL = driver.current_url
    driver.quit()
    fb_login = FacebookLogin(email, password, browser='Chrome')
    fb_login.login()
