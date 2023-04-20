import time
from selenium import webdriver

#Abrir la pagina donde se va a crear el test
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

#Se hara el llenado de los campos
driver.find_element("xpath", "//input[contains(@id,'userName')]").send_keys("Roberto")
driver.find_element("xpath", "//input[contains(@id,'userEmail')]").send_keys("robertTester@gmail.com")
driver.find_element("xpath", "//textarea[contains(@id,'currentAddress')]").send_keys("Av Lopez Mateos, Calles del centro")
driver.find_element("xpath", "//textarea[contains(@id,'permanentAddress')]").send_keys("Calle Flores, Zona Sur")

#Generar un evento Click
driver.find_element("xpath", "//button[contains(@id,'submit')]").click()
time.sleep(3)

#Hacer un scroll hacia abajo -> window.scrollTo(X,Y)
driver.execute_script("window.scrollTo(0,200)")

#Se intergra un tiempo de espera de 3 segundos para apreciar el llenado de la pagina
time.sleep(3)