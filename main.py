from impresoras import *
#import pandas as pd
#from openpyxl import load_workbook
from impresora180 import agregar180
from botito import modif

info_impresiones = {}
impresiones = []
cargarDiccionario(info_impresiones)
agregar170(info_impresiones)
agregar184(info_impresiones)
agregar180(info_impresiones)

print(info_impresiones)

impresiones = info_impresiones.values()

modif(impresiones)
print("HECHO!")
#print(impresiones)




