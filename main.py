from Classes.Printer import Printer
from Classes.ExcelHandler import ExcelHandler
from database.listadoImpresoras import listado_impresoras

# Lista para almacenar las instancias de las impresoras
impresoras_list = []

for impresora in listado_impresoras:
        
    if impresora["ip"] != "170" and impresora["ip"] != "184" and impresora["ip"] != "10.0.0.133" and impresora["ip"] != "180":
        impresora["URL_BASE"] = f"http://128.110.0.{impresora['ip']}/cgi-bin/dynamic/printer/config/reports/deviceinfo.html"
        printer = Printer(impresora["ip"], impresora["ubicacion"], impresora["numeroSerie"], impresora["modelo"], impresora["URL_BASE"])
        impresoras_list.append(printer)


    elif impresora["ip"] == "170":
        impresora["URL_BASE"] = f"http://128.110.0.{impresora['ip']}/cgi-bin/dynamic/config/reports/deviceinfo.html"
        printer = Printer(impresora["ip"], impresora["ubicacion"], impresora["numeroSerie"], impresora["modelo"], impresora["URL_BASE"])
        impresoras_list.append(printer)

    elif impresora["ip"] == "10.0.0.133":
        impresora["URL_BASE"] = f"http://10.0.0.133/cgi-bin/dynamic/printer/config/reports/deviceinfo.html"
        printer = Printer(impresora["ip"], impresora["ubicacion"], impresora["numeroSerie"], impresora["modelo"], impresora["URL_BASE"])
        impresoras_list.append(printer)

    elif impresora["ip"] == "180":
        impresora["URL_BASE"] = f"http://128.110.0.180/#/Settings/Reports/ReportDeviceGroup"
        printer = Printer(impresora["ip"], impresora["ubicacion"], impresora["numeroSerie"], impresora["modelo"], impresora["URL_BASE"])
        impresoras_list.append(printer)

    elif impresora["ip"]=="184":
        impresora["URL_BASE"] = f"http://128.110.0.184/web/guest/es/websys/status/getUnificationCounter.cgi"
        printer = Printer(impresora["ip"], impresora["ubicacion"], impresora["numeroSerie"], impresora["modelo"],impresora["URL_BASE"])
        impresoras_list.append(printer)



handler = ExcelHandler()

# Guardar datos en Excel
handler.save_printers_to_excel(impresoras_list)

    
        






# from impresoras import *
# import pandas as pd
# from openpyxl import load_workbook
# from impresora180 import agregar180
# from botito import modif

# info_impresiones = {}
# impresiones = []
# cargarDiccionario(info_impresiones)
# agregar170(info_impresiones)
# agregar184(info_impresiones)
# agregar180(info_impresiones)
# agregar133(info_impresiones)

# print(info_impresiones)

# impresiones = info_impresiones.values()

# modif(impresiones)
# print("HECHO!")
# print(impresiones)




