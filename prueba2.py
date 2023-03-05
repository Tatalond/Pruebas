
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
import time


servicio = Service('driver/chromedriver')

driver = webdriver.Chrome(service=servicio)

driver.get("https://www.exito.com")

menu = driver.find_element(By.ID, 'Enmascarar_grupo_659')

time.sleep(5)



time.sleep(20)
driver.close()
driver.quit()