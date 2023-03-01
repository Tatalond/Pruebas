from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

servicio = Service('driver/chromedriver')


driver = webdriver.Chrome(service=servicio)

driver.get('https://www.linio.com.co/')

driver.maximize_window()

action = ActionChains(driver)

# modal = driver.find_element(By.CSS_SELECTOR, "dy-lb-close").click()
# time.sleep(3)


menu = driver.find_element(By.CSS_SELECTOR, ".icon-hamburger").click()

time.sleep(3)

categoria = driver.find_element(By.XPATH, "//div[@id=\'main-menu\']/nav/ul/li[5]/a/span[2]")

action.move_to_element(categoria).perform()
time.sleep(3)

portatiles = driver.find_element(By.XPATH, "//div[@id=\'main-menu\']/div/div[5]/div/div/div/a[2]").click()

driver.maximize_window()
# time.sleep(5)





""" time.sleep(3)

categoria = driver.find_element(By.XPATH, '/html/body/header/nav/div/div[5]/nav/ul/li[5]/a')

action.move_to_element(categoria).perform()
time.sleep(3)

portatiles = driver.find_element(By.XPATH, '/html/body/header/nav/div/div[5]/div/div[5]/div[1]/div/div[1]/a[2]')

portatiles.click()

time.sleep(3)
asus = driver.find_element(By.XPATH, '/html/body/div[3]/main/div[1]/div[7]/div[2]/div/div[2]/a[1]/div[2]/p/span')

asus.click() """


time.sleep(20)
driver.close()
driver.quit()