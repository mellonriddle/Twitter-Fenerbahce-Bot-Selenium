from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import random
import time

# Loading environment variables
load_dotenv(".env")
TWITTER_ID = os.getenv("TW_Username")
TWITTER_PASSWORD = os.getenv("TW_Password")

# Setting up our web driver
chrome_driver_path = r"C:\Development\chromedriver.exe"
my_service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=my_service)
driver.maximize_window()

# We need to sleep random times occasionally, because we don't want to be banned on Twitter

driver.get("https://twitter.com/i/flow/login")
time.sleep(random.uniform(2, 3))

# Sign in with our credentials
form1 = driver.find_element(By.NAME, "text")
form1.send_keys(TWITTER_ID)


btn2 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div'
                                     '/div[2]/div[2]/div/div/div/div[6]/div')

btn2.click()
time.sleep(random.uniform(2, 3))

form2 = driver.find_element(By.NAME, "password")
form2.send_keys(TWITTER_PASSWORD)
btn3 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/'
                                     'div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
btn3.click()
time.sleep(random.uniform(3, 4))

# Find my favorite team's latest tweet and retweet it
driver.get("https://twitter.com/search?q=from%3Afenerbahce&src=typed_query")
time.sleep(random.uniform(1, 2))
btn4 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/"
                                     "div/div/div[1]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/"
                                     "div[2]/div/div/div[1]")
btn4.click()


btn5 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div"
                                     "/div/div[2]/div/span")
btn5.click()


# Done & Finish
time.sleep(random.uniform(3, 4))
driver.quit()
