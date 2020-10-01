from selenium import webdriver
import random
import time
import requests
link="https://reward.ff.garena.com/?access_token="


class Free:
 def __init__(self,link,s,drive):
   self.link=link
   self.s=s
   self.drive=drive
   from getpass import getpass
   token= getpass("enter the token: ")
   link= link+token
   time.sleep(2)
 def randome():
    myList=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    c=""
    d=0
    while d<4:
      d=d+1
      k=random.choice(myList)
      c=c+k
    return c
 def exploiting(self):
    driver = webdriver.Chrome(self.drive)
    browser=driver.get(link)
    time.sleep(4.2)
    driver.refresh()
    while True:
     try:
      a=Fire.randome()
      b=Fire.randome()
      c=Fire.randome()
      driver.find_element_by_id("input_serial_1").send_keys(a)
      driver.find_element_by_id("input_serial_2").send_keys(b)
      driver.find_element_by_id("input_serial_3").send_keys(c)
      driver.find_element_by_class_name("confirm-btn").click()
      time.sleep(0.9)
      driver.get(link)
      time.sleep(1)
     except KeyboardInterrupt:
      print("you tried",s, "times")
      quit()
     except:
      driver.quit()
      exploiting(link,s)
      print("a problem had popped out :")
      print("you tried",s, "times")
     s=s+1
# exploiting(link,s)
