import os,sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from .DB import baseDatos
from .intepreteDB import interpreterDB
class conectorDBVentaCelular(baseDatos):
    def __init__(self):
        super().__init__()
        self.crearTablaVenta()
        
    def crearTablaVenta(self):
        consulta=interpreterDB.Create("ventaCelular","nombre_cliente,marca_celular,id_celular,monto_total")
        self.realizarConsulta(consulta=consulta)

class registroVentaCelular(conectorDBVentaCelular):
    def registrarVenta(self,ventaC):
        nombre=ventaC.nombre
        marcaCel=ventaC.marcaCel
        idCel=ventaC.idCelular
        total=ventaC.total
        consulta=interpreterDB.Insert("ventaCelular","('{nombre}','{marca}','{idCel}',{total})"
                                          .format(nombre=nombre,marca=marcaCel,idCel=idCel,total=total))
        self.realizarConsulta(consulta=consulta)
        self.endConnection()