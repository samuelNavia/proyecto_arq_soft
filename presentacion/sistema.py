import datetime
import os,sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from negocio.venta import *
from negocio.factura import *
class sistema():
    def __init__(self):
        self.rf=registroFactura()
        self.rV=registroVenta()
        self.elegirOpcion()
        self.salir()
    def elegirOpcion(self):
        salida=0
        while(salida!=2):
            print("bueno en que te puedo ayudar:")
            print("1: quiero realizar el registro de compra de un celular")
            print("2: quiero salir del sistema")
            salida=int(input("que opcion eliges (nro): "))
            if salida==1: 
                self.realizarCompra()
                if(int(input("quiere tenener factura si/no (1/0):"))):
                    self.realizarFactura(self.venta)
        
    
    def realizarCompra(self):
        nombre=input("ingrese el nombre el usuario: ")
        marca=input("ingrese la marca del dispositivo: ")
        idCel=input("ingrese el id del celular comprado: ")
        total=input("ingresar el total del producto comprado:  ")
        
        self.venta=VentaCelular(nombre=nombre,marcaCel=marca,idCelular=idCel,total=total)
        self.rV.registarVentaCelular(self.venta)
        
        
    def realizarFactura(self,venta):
        fecha=str(datetime.date.today())
        print("la fecha de la factura es : "+fecha)
        nombreApe=venta.nombre
        print("el nombre del cliente es: "+nombreApe)
        nroNIT=input("ingrese el numero de NIT: ")
        domicilio=input("ingrese su domicilio:  ")
        producto=venta.marcaCel
        print("el nombre de su producto es: "+producto)
        impuesto=float(input("ingrese el porcentaje de impuesto:"))
        precioUni=int(venta.total) 
        print("el precio unitario es:  "+str(precioUni))
        
        self.rf.rellenar(nombreApellido=nombreApe,fechaExped=fecha,idFiscal=nroNIT,domicilio=domicilio,
                    producto=producto,impuesto=impuesto,precioUnitario=precioUni)
        
        print("el total del precio de la con factura es: "+str(self.rf.facturaObj.total))
            
    def salir(self):
        print("gracias por usar el sistema nos vemos en un futuro")
        

