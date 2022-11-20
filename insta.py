#pip install selenium

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import time
import random
import string
import csv

def random_string():
    letters = string.ascii_lowercase
    r = ( ''.join(random.choice(letters) for i in range(10)) )
    return r

with open('accs.csv', newline='') as f:
    reader = csv.reader(f)
    accountsList = list(reader)

with open('random.csv', newline='') as rn:
    rdr = csv.reader(rn)
    textList = list(rdr)

options = Options()
#options.add_argument('--headless')
#un = "harry_angelidis"
#pw = "1012firenze"
un = "username"
pw = "password"

driver = webdriver.Firefox(options=options)
driver.get("https://www.instagram.com/")
accept =wait(driver, 10 ).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/button[1]")))
accept.click()
login_username = wait(driver, 10 ).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")))
login_password = wait(driver, 10 ).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")))
login_username.send_keys(un)
login_password.send_keys(pw)
login_password.send_keys(Keys.RETURN)
time.sleep(5)
driver.get("https://www.instagram.com/p/CONXf-WjtZX/")
i=0
while True:
    commentbox = wait(driver, 10 ).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div")))
    commentbox.click()
    input_form = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
    #driver.execute_script("arguments[0].click();", input_form)
    a=random.choice(accountsList)
    b=random.choice([x for x in accountsList if (x != a) and (x!="")]) 
    c=random.choice([x for x in accountsList if (x != b) and (x!=a) and (x!="")])    
    d = random.choice(textList)    
    text = a[0] + " " + b[0] + " " + c[0] + " " + d[0]
    input_form.send_keys(Keys.CONTROL, "a")
    input_form.send_keys(Keys.DELETE)
    input_form.send_keys(text)
    ##input_form.send_keys(Keys.RETURN)

    post = wait(driver, 10 ).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]")))
    driver.execute_script("arguments[0].click();", post)
    i=i+1
    print(i)
    time.sleep(60)


#driver.quit()