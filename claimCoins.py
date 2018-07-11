from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from time import sleep
import os
path = os.path.dirname(os.path.abspath('claimCoins.py'))

driver = webdriver.Chrome(str(path) + '\\chromedriver.exe')
driver.get("https://www.sliver.tv")

try:
    WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.CLASS_NAME, 'slvr-navbar__inventory')))
finally:
    inventory = driver.find_element_by_class_name('slvr-navbar__inventory')
    inventory.click()
    sleep(1)
    coinNum = 1
    while coinNum != 0:
        try:
            WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.CLASS_NAME, 'coins-inventory-type')))
        finally:
            coin = driver.find_elements_by_class_name('coins-inventory-type')
            print(str(len(coin)) + ' coins found')
            crateNum = len(coin)
            with open('coinList.txt', 'a') as f:
                f.write(coin[0].find_element_by_class_name('name').text + '\n')
            coin[0].find_element_by_class_name('action-button').click()
            sleep(2)
