from random import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get(
    "https://docs.google.com/forms/d/e/1FAIpQLSeONBFVvBReoboLuxjSQwtysc97U4INCS8kC1QeWvo4hgXe0Q/viewform"
)

ageData = ['14', '16', '18', '20', '21', '22', '23', '25', '31', '32',
           '24', '36', '42', '47', '35', '40', '19', '27', '31', '34', '33', '37', '19', '25', '26', '29', '30', '31', '33']

# ageData = ['31', '34', '33', '37', '40', '42', '45', '46', '47']


def generateRandom(limit):
    return int(random() * limit)


time.sleep(.5)

for i in range(30):

    ageInput = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )

    dosisDeVacuna = [
        driver.find_element(By.XPATH, '//*[@id="i9"]/div[3]/div'),
        # driver.find_element(By.XPATH, '//*[@id="i12"]/div[3]/div'),
    ]

    howManyDoses = [
        # driver.find_element(By.XPATH, '//*[@id="i19"]/div[3]/div'),
        driver.find_element(By.XPATH, '//*[@id="i22"]/div[3]/div'),
        # driver.find_element(By.XPATH, '//*[@id="i25"]/div[3]/div'),
        # driver.find_element(By.XPATH, '//*[@id="i28"]/div[3]/div'),
    ]

    hasDifferentBrand = [
        driver.find_element(By.XPATH, '//*[@id="i35"]/div[3]/div'),
        # driver.find_element(By.XPATH, '//*[@id="i38"]/div[3]/div'),
    ]

    secondaryEffects = [
        driver.find_element(By.XPATH, '//*[@id="i45"]/div[3]/div'),
        # driver.find_element(By.XPATH, '//*[@id="i48"]/div[3]/div'),
    ]

    isSobrepeso = [
        driver.find_element(By.XPATH, '//*[@id="i55"]/div[3]/div'),
        # driver.find_element(By.XPATH, '//*[@id="i58"]/div[3]/div'),
    ]

    sendButton = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    ageInput.send_keys(ageData[generateRandom(len(ageData))])
    dosisDeVacuna[generateRandom(len(dosisDeVacuna))].click()
    howManyDoses[generateRandom(len(howManyDoses))].click()
    hasDifferentBrand[generateRandom(len(hasDifferentBrand))].click()
    secondaryEffects[generateRandom(len(secondaryEffects))].click()
    isSobrepeso[generateRandom(len(isSobrepeso))].click()
    sendButton.click()

    time.sleep(.2)

    driver.find_element(
        By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'
    ).click()

    time.sleep(.2)
