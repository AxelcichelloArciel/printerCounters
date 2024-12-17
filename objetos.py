import openpyxl as op
class Excel():
    
    def __init__(self, ruta):
        self.libro= op.load_workbook(ruta)
        self.ruta=ruta
        
    def seleccionar_hoja(self, hoja):
        self.sheet= self.libro[hoja]

    def borrar_col(self, colum):
        self.sheet.delete_cols(idx=colum)
    
    def completar_meses(self, celdaVieja, celdaNueva ):
        meses= ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
        for index, mes in enumerate(meses):
            if mes.capitalize()==self.sheet[celdaVieja].value:#N1
                if mes=="diciembre":
                    self.sheet[f'{celdaNueva}']=meses[0].capitalize() #O1
                else:
                    self.sheet[f'{celdaNueva}']=meses[index+1].capitalize() #O1
    
    def completar_computo(self, computo):
        for index, num in enumerate(computo):
            self.sheet[f'Q{index+2}']=num
    
    def completar_total(self):
        letras=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q"]
    
        for index, letra in enumerate(letras):
            if 7 < index < 17:
                
                self.sheet[f"{letra}{3}"]=f"={letras[index-1]}{14}"
                self.sheet[f"{letra}{2}"]=f"=SUM({letras[index-1]}5:{letras[index-1]}18)-{letras[index-1]}14"
                
                for num in range(5, 17):
                    formula = f"='Base de Equipos'!{letras[index]}{num-3}-'Base de Equipos'!{letras[index-1]}{num-3}"
                    self.sheet[f'{letra}{num}'] = formula
         
    def valor_celda(self, celda, texto):
        self.sheet[celda]=texto
    
    def guardar(self):
        self.libro.save(self.ruta)
        
    def olvidar_hoja(self):
        self.sheet=None