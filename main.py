from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from time import sleep
import os
path = os.path.dirname(os.path.abspath('main.py'))

driver = webdriver.Chrome(str(path) + '\\chromedriver.exe')
driver.get("https://www.sliver.tv")

try:
    WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.CLASS_NAME, 'slvr-navbar__inventory')))
finally:
    inventory = driver.find_element_by_class_name('slvr-navbar__inventory')
    inventory.click()
    sleep(1)
    crateNum = 1
    while crateNum != 0:
        try:
            WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.CLASS_NAME, 'crate-inventory-type')))
        finally:
            crate = driver.find_elements_by_class_name('crate-inventory-type')
            print(str(len(crate)) + ' crates found')
            crateNum = len(crate)
            crate[0].click()
            sleep(1)
            try:
                WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.CLASS_NAME, 'open-crate-button')))
            finally:
                openButton = driver.find_element_by_class_name('open-crate-button')
                openButton.click()
                sleep(13)
                try:
                    WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.CLASS_NAME, 'continue-button')))
                finally:
                    continueButton = driver.find_element_by_class_name('continue-button')
                    continueButton.click()
                    sleep(1)
