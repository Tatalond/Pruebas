
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

driver.get('https://www.linio.com.co/')



driver.maximize_window()

action = ActionChains(driver)
time.sleep(5)

modal = driver.find_element(By.CSS_SELECTOR, "body > div.dy-modal-container.dy-act-overlay > div.dy-modal-wrapper > div > div.dy-lb-close").click()
time.sleep(5)


menu = driver.find_element(By.CSS_SELECTOR, ".icon-hamburger").click()
time.sleep(1)
 
categoria = driver.find_element(By.XPATH, "//div[@id=\'main-menu\']/nav/ul/li[5]/a/span[2]")
time.sleep(1)

action.move_to_element(categoria).perform()
time.sleep(1)


portatiles = driver.find_element(By.XPATH, "//div[@id=\'main-menu\']/div/div[5]/div/div/div/a[2]").click()

time.sleep(1)
asus = driver.find_element(By.XPATH, '/html/body/div[3]/main/div[1]/div[7]/div[2]/div/div[2]/a[1]/div[2]/p/span').click()

time.sleep(1)
cantidad = driver.find_element(By.XPATH, '//*[@id="display-zoom"]/div[2]/div[3]/div[2]/div[1]/div/button').click()

time.sleep(1)
unidades = driver.find_element(By.XPATH, '//*[@id="select-dropdown-list-product-quantity"]/li[2]').click()

time.sleep(1)
agregar_carrito = driver.find_element(By.XPATH, '//*[@id="buy-now"]').click()

time.sleep(1)
ir_al_carrito = driver.find_element(By.XPATH, '//*[@id="alert-add-to-cart"]/div/div/div[4]/a').click()

time.sleep(1)
procesar_compra = driver.find_element(By.XPATH, '/html/body/div[3]/main/div[1]/div/div[2]/div/ul/ul/li[2]/a').click()

#Inicial sesión
time.sleep(1)
email = driver.find_element(By.ID, 'login_form_email').send_keys("pepito.perez@gmail.com")

time.sleep(1)
password = driver.find_element(By.ID, 'login_form_password').send_keys("123456")

time.sleep(1)
iniciar_sesion = driver.find_element(By.XPATH, '//*[@id="login-form"]/form/button').click()




time.sleep(5)
driver.close()
driver.quit()