import requests
import unicodedata
from bs4 import BeautifulSoup
import re
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Printer:
    def __init__(self, ip, ubicacion, numeroSerie, modelo, urlBase):
        self._ip = ip
        self._ubicacion = ubicacion
        self._numeroSerie = numeroSerie
        self._modelo = modelo
        self._urlBase = urlBase
        self._contador = self.buscarContador()

    def get_contador(self):
        return self._contador

    def __str__(self):
        return f"\nPrinter(ip={self._ip}, ubicacion={self._ubicacion}, numeroSerie={self._numeroSerie}, modelo={self._modelo}, urlBase={self._urlBase}, contador={self._contador})"

    def quitar_caracteres_especiales(self, texto):
        """Elimina los caracteres especiales y convierte a minúsculas."""
        # Normalizamos el texto para eliminar los acentos
        texto = unicodedata.normalize('NFD', texto)
        texto = ''.join([c for c in texto if unicodedata.category(c) != 'Mn'])  # Eliminamos los acentos
        # Reemplazamos caracteres no alfabéticos por un espacio
        texto = re.sub(r'[^a-zA-Z0-9\s]', '', texto)
        texto = re.sub(r'\s+', ' ', texto).strip()  # Reemplazamos espacios múltiples por uno solo
        return texto.lower()

    def normalizar_texto(self, texto):
        """Convierte el texto a formato ASCII y normaliza espacios."""
        texto = self.quitar_caracteres_especiales(texto)  # Aplica la eliminación de caracteres especiales
        return texto

    def buscarContador(self):

        if self._ip != "180" :

            try:
                pedido_obtenido = requests.get(self._urlBase, timeout=5)
                pedido_obtenido.encoding = 'ISO-8859-1'  # Usamos 'ISO-8859-1' como codificación predeterminada

                if pedido_obtenido.status_code == 200:
                    html_obtenido = pedido_obtenido.text

                    soup = BeautifulSoup(html_obtenido, "html.parser")

                    if self._ip != "184":
                        filas = soup.find_all('tr')

                        for fila in filas:
                            celdas = fila.find_all('td')
                            if len(celdas) >= 2:
                                texto_primera_celda = self.normalizar_texto(celdas[0].get_text())

                                # print(f"🔸 Celda encontrada: {texto_primera_celda}")  # Depuración

                                # 🔍 Expresión regular para detectar "Cómputo de pág." con cualquier variación
                                if re.search(r"c[oó]mputo\s+de\s+p[áa]g|camputo de pag", texto_primera_celda, re.IGNORECASE):

                                    return self.normalizar_texto(celdas[1].get_text())

                    elif self._ip == "184":
                        p_computo = soup.find('td', text=':')
                        p_value = p_computo.find_next('td')
                        value = p_value.text
                        return value


                return None

            except requests.RequestException as e:
                print(f"⚠️ Error al acceder a la impresora en {self._ubicacion} ({self._ip}): {e}")
                return 0
            except (AttributeError, ValueError) as e:
                print(f"⚠️ Error al procesar los datos de la impresora {self._ubicacion} ({self._ip}): {e}")
                return 0

        else:
            driver = webdriver.Chrome()
            driver.get("http://128.110.0.180/#/Settings/Reports/ReportDeviceGroup")
            pag_contador = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//a[.//span[@data-textid='70528']]")))
            pag_contador.click()
            value_e = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='ReportDeviceStatisticsPopupContents']/div/table[38]/tbody/tr/td[2]")))
            value = int(value_e.text.strip())
            return value