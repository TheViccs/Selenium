import time
from selenium import webdriver

#Se importan las funcionalidades de Keys
from selenium.webdriver.common.keys import Keys

#En este ejercicio se simulara la acción de un TAB, esto con la implementación de un keys.tab

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

#Keys.TAB se encarga de simular el tabulador
tabulador = driver.find_element("xpath", "//input[contains(@id,'userName')]")
tabulador.send_keys("Roberto")
tabulador.send_keys(Keys.TAB + "Roberto@gmail.com" + Keys.TAB + "Direccion 1" + Keys.TAB + "Dirección 2")

#Generar el evento click
driver.find_element("xpath", "//button[contains(@id,'submit')]").click()
time.sleep(2)

