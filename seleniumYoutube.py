from random import random
from re import search
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get(
    "https://www.amazon.com.mx/"
)

search = driver.find_element(
    By.XPATH, '//*[@id="twotabsearchtextbox"]')

search.send_keys("Oculus Rift")
search.send_keys(u'\ue007')
search.send_keys(By.XPATH, '')
time.sleep(50)
