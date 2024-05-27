


class factura():
    _instances = None
    def __new__(cls) :
        if factura._instances is None:
            instance=object.__new__(cls)
            factura._instances=instance
        return factura._instances
    
    def __init__(self) :
        self.numeroFac=0
        self.fechaExped="0000-00-00"
        self.nombreApellido=""
        self.idFiscal=0
        self.domicilio=""
        self.producto=""
        self.impuesto=0
        self.precioUnitario=0
        self.total=0
        
    
class registroFactura():
    def __init__(self):
        self.facturaObj=factura()
    
    def rellenar(self,fechaExped,nombreApellido,idFiscal,domicilio,producto,impuesto,precioUnitario):
        self.facturaObj.numeroFac=self.facturaObj.numeroFac+1
        self.facturaObj.fechaExped=fechaExped
        self.nombreApellido=nombreApellido
        self.facturaObj.idFiscal=idFiscal
        self.facturaObj.domicilio=domicilio
        self.facturaObj.producto=producto
        self.facturaObj.impuesto=impuesto
        self.facturaObj.precioUnitario=precioUnitario
        self.facturaObj.total=precioUnitario*(1+impuesto)



##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
