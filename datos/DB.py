###############################################################################################################
############################################Capa de Acceso a Datos#############################################
###############################################################################################################  
import sqlite3
from typing import Any   
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
class baseDatos(object): 
    _instances = None
    def __new__(cls) :
        if baseDatos._instances is None:
            instance=object.__new__(cls)
            baseDatos._instances=instance
        return baseDatos._instances
    
    def __init__(self):
        self.conect=sqlite3.connect("./datos/myBD.db")

        
    
    def realizarConsulta(self,consulta):
        
        resultado="fallo la consulta"
        try:
            resultado=self.conect.execute(consulta)
        except:
            print(resultado)
        self.conect.commit()
        return resultado
    
    def endConnection(self):
        self.conect.close()
