###############################################################################################################
############################################Capa de logica de negocio#############################################
###############################################################################################################  
import os,sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from datos.DBCelular import *
class Venta:
    def __init__(self,total,nombre):
        self.total=total
        self.nombre=nombre
        

class VentaCelular(Venta):
    def __init__(self,total,nombre,idCelular,marcaCel):
        super().__init__(total,nombre)
        self.idCelular=idCelular
        self.marcaCel=marcaCel

class registroVenta(registroVentaCelular):
    def registarVentaCelular(self,venta):
        rvc=registroVentaCelular()
        rvc.registrarVenta(ventaC=venta)
        print("registro exitoso")
        