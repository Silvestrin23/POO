class MedioDePago:
    def pagar(self,monto):
        print("Procesando pago generico de:",monto)

class Efectivo(MedioDePago):
    def pagar(self,monto):
        print("Se pago",monto,"en efectivo. No hay recargos.")

class Tarjeta(MedioDePago):
    def pagar(self,monto):
        print("Se pago",monto,"con tarjeta. Conectando con el banco...")

class Transferencia(MedioDePago):
    def pagar(self,monto):
        print("Se pago",monto,"por transferencia. Esperando acreditacion...")


def procesar_pago(medio,monto):
    medio.pagar(monto)


pago_efectivo=Efectivo()
pago_tarjeta=Tarjeta()
pago_transferencia=Transferencia()

print("--- Iniciando cobros ---")

procesar_pago(pago_efectivo,5000)
procesar_pago(pago_tarjeta,12500)
procesar_pago(pago_transferencia,8000)