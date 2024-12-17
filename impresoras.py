from bs4 import BeautifulSoup
import re
import requests

def cargarDiccionario(info_impresiones):
    impresoras = [170,172,173,175,176,177,178,179,180,181,182,184,133]

    for impresora in impresoras:
        try:
            URL_BASE = f'http://128.110.0.{impresora}/cgi-bin/dynamic/printer/config/reports/deviceinfo.html'
            pedido_obtenido = requests.get(URL_BASE)
            html_obtenido = pedido_obtenido.text
            soup = BeautifulSoup(html_obtenido, "html.parser")
            data = soup.find(string=re.compile("= *"))
            info_impresiones[impresora] = int(data[2:])
        except:
            info_impresiones[impresora] = 0

    return  

def LlamarURL(url):
    try:
        pedido_obtenido = requests.get(url)
        pedido_obtenido.encoding = 'utf-8'
        if pedido_obtenido.status_code == 200:
            html_obtenido = pedido_obtenido.text
            soup = BeautifulSoup(html_obtenido, "html.parser")
            return soup
        else:
            print(f"Error al acceder a la página: {soup.status_code}")
            return None
    except Exception as e:
        print(f"Se produjo un error al realizar la solicitud: {e}")
        return None

def agregar170(diccionario):
    data = LlamarURL('http://128.110.0.170/cgi-bin/dynamic/config/reports/deviceinfo.html')
    p_computo = data.find('p', text = 'Cómputo de pág.')
    p_value = p_computo.find_next('p')
    value = p_value.text.strip().replace('=', '').strip()
    diccionario[170] = int(value)

def agregar184(diccionario):
    data = LlamarURL('http://128.110.0.184/web/guest/es/websys/status/getUnificationCounter.cgi')
    p_computo = data.find('td', text = ':')
    p_value = p_computo.find_next('td')
    value = p_value.text
    diccionario[184] = int(value)


def agregar133(diccionario):
    data = LlamarURL('http://10.0.0.133/cgi-bin/dynamic/printer/config/reports/deviceinfo.html')
    p_computo = data.find('tr')
    print(p_computo)
    p_value = p_computo.find_next('tr').find_next('td').find_next('td').find_next('p')
    value = p_value.text.strip().replace('=','').strip()
    diccionario[133] = int(value)

    
