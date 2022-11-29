import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def generarTest(driver):
    driver.get('https://www.jotform.com/build/223207084451651')
    driver.maximize_window()
    driver.implicitly_wait(8) #para que cargue bien toda la pagina

    nombre = driver.find_element(By.NAME, "q3_name[first]")
    nombre.send_keys('Nombre test')
    apellido = driver.find_element(By.NAME, 'q3_name[last]')
    apellido.send_keys('Algun apellido')
    numero = driver.find_element(By.NAME, 'q4_numeroDe[full]')
    numero.send_keys('14-2923-4754')
    correo = driver.find_element(By.NAME, 'q5_correoElectronico')
    correo.send_keys('un_mail_cualquiera@gmail.com')
    fecha = driver.find_element(By.ID, 'lite_mode_16')
    fecha.send_keys('12-03-2019')
    hora = driver.find_element(By.NAME, 'q16_fechaDe[timeInput]')
    hora.send_keys('02:02')
    tiempoHorario = driver.find_element(By.NAME, 'q16_fechaDe[ampm]')
    tiempoHorario.send_keys('AM')
    botonEnter = driver.find_element(By.ID, 'input_2')

    time.sleep(5)

    botonEnter.send_keys(Keys.ENTER)

    time.sleep(5)

def __main__():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    generarTest(driver)
    driver.close()

if __name__ == '__main__':
    __main__()
