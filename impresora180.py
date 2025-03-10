import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

os.environ['PATH']+=rf"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\chrome-win64\\chrome.exe"
driver= webdriver.Chrome()
driver.get("http://128.110.0.180/#/Settings/Reports/ReportDeviceGroup")

def seleccionar(metodo, valor):
    variable= WebDriverWait(driver, 15).until(EC.element_to_be_clickable((metodo, valor)))
    return variable

def pag_prin():
    pag_contador= seleccionar(By.XPATH, "//a[.//span[@data-textid='70510']]")
    pag_contador.click()

def pag_contador():
    value_e = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//li[.//span[text()='Cómputo de páginas']]//span[@class='report-item-value']")))
    value = int(value_e.text.strip())
    return int(value)

def agregar180(diccionario):
    pag_prin()
    impresiones = pag_contador()
    driver.quit()
    diccionario[180] = impresiones