class MedioDePago:
    def pagar():
        pass

class Efectivo(MedioDePago):
    def pagar(self,monto):
        print("Has abonado",monto,"en efectivo")
        
class Tarjeta(MedioDePago):        
    def pagar(self,monto):
        print("Has abonado",monto,"en tarjeta")

class Transferencia(MedioDePago):
    def pagar(self,monto):
        print("Has abonado",monto,"en transferencia")
def procesar_pago(medio,monto):
    medio.pagar(monto)
    
cash=Efectivo()
transferencia=Transferencia()
tarjeta=Tarjeta()

procesar_pago(cash,400)
procesar_pago(transferencia,500)
procesar_pago(tarjeta,600)