import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def generarTest(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    driver.maximize_window()
    time.sleep(8) #para que cargue bien toda la pagina

    # arranque de generacion de datos automatizados
    signIn = driver.find_element(By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/a')
    signIn.click()
    time.sleep(8)

    email = driver.find_element(By.NAME, 'login[username]')
    email.send_keys('unmailcualquiera@gmail.com')
    password = driver.find_element(By.NAME, 'login[password]')
    password.send_keys('Unacontrasenia&')
 
    botonIngresar = driver.find_element(By.NAME, 'send')

    time.sleep(5)

    botonIngresar.send_keys(Keys.ENTER)

    time.sleep(5)

def __main__():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    generarTest(driver)
    driver.close()

if __name__ == '__main__':
    __main__()
