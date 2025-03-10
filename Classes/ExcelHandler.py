import openpyxl
import os
from datetime import datetime


class ExcelHandler:
    def __init__(self):
        # Ruta del archivo base
        self._file_path = r"C:\Users\acichello\Desktop\Contadores 2023\appImpresoras\archivo_base.xlsx"

        # Cargar el libro de trabajo
        self._wb = openpyxl.load_workbook(self._file_path)
        self._sheet = self._wb.active  # Hoja activa

    def save_printers_to_excel(self, printers):
        """Guarda los datos en las filas 2 a 15 en la columna G y hace un 'Guardar como' en el Escritorio."""

        # Obtener el mes actual en español
        meses_es = {
            "January": "Enero", "February": "Febrero", "March": "Marzo",
            "April": "Abril", "May": "Mayo", "June": "Junio",
            "July": "Julio", "August": "Agosto", "September": "Septiembre",
            "October": "Octubre", "November": "Noviembre", "December": "Diciembre"
        }
        mes_actual = meses_es[datetime.now().strftime("%B")]

        # Obtener la ruta del Escritorio
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        # Nombre del nuevo archivo
        new_file_name = f"Computos de impresoras {mes_actual}.xlsx"
        new_file_path = os.path.join(desktop_path, new_file_name)

        # Escribir los datos en la columna G (columna 7)
        start_row = 2
        end_row = 15
        column = 6

        for i, printer in enumerate(printers, start=start_row):
            if i > end_row:  # Evitar escribir más allá de la fila 15
                break
            self._sheet.cell(row=i, column=column, value=printer.get_contador())

        # Guardar el archivo con un nuevo nombre en el Escritorio
        self._wb.save(new_file_path)
        print(f"Datos guardados correctamente en: {new_file_path}")