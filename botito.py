from objetos import Excel
import os

def modif(computos): 
    login = os.getlogin()  
    #excel=Excel(f'C:\Users\\{login}\\OneDrive - Inta\\Documentos - SistemasWeb\\Contadores\\Contadores 2023\\Contadores INTA.xlsx')
    #excel=Excel(f'C:\Users\{login}\OneDrive - Inta\Documentos - SistemasWeb\Contadores\Contadores 2023\Contadores INTA - copia.xlsx')
    excel = Excel(f'C:\\Users\\{login}\\Inta\\SistemasWeb - Documentos\\Contadores\\Contadores 2023\\Contadores INTA - copia.xlsx')


    print('pase nuevo')
    
    excel.seleccionar_hoja('Base de Equipos')
    excel.borrar_col(7)
    excel.completar_meses('P1', 'Q1')
    excel.completar_computo(computos)
    

   


    excel.seleccionar_hoja('Computos Mensuales')
    excel.completar_meses('P4', 'Q4')
    excel.completar_total()
    excel.borrar_col(7)
    excel.valor_celda("P1","TOTAL A FACT.")
    excel.guardar()

    print("Modificado")
