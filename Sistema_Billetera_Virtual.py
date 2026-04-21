class Cuenta:
    def __init__(self,titular):
        self.titular=titular
        self._saldo=0
        
    
    @property
    def saldo(self):
        return self._saldo
    
    def depositar(self, monto):
        self._saldo+=monto
        print("Depositado") 
    
    def retirar(self,monto):
        if self._saldo>monto:
            self._saldo-=monto
        else:
            print("Saldo insuficiente")
        
    def tipo_cuenta(self):
        return "Cuenta"
    
    def __str__(self):
        print( "Juan Perez | Saldo: $5000") 
    
class CuentaBasica(Cuenta):
    def __init__(self,titular,limite_retiro_diario):
        super().__init__(titular)
        self.limite_retiro_diario=limite_retiro_diario
    
    def tipo_cuenta(self):
        return "Basica"
    
    def __str__(self):
        print("Juan Perez | Cuenta Basica | Saldo: $5000 | Limite diario $10000")

class CuentaPremium(Cuenta):
    def __init__(self,titular,cashback_porcentaje):
        super().__init__(titular)
        self.cashback_porcentaje=cashback_porcentaje
    
    def tipo_cuenta(self):
        return "Premium"
    

    def __str__(self):
        print("Maria Lopez | Cuenta Premium | Saldo: $15000 | Cashback 5%")
        
cuenta_basica= CuentaBasica("Lucio",1000)
cuenta_basica1= CuentaBasica("Mateo",200000000)

cuenta_premium= CuentaPremium("Juan Cruz",80)
cuenta_premium1= CuentaPremium("Valen",3)

lista=[cuenta_basica,cuenta_basica1,cuenta_premium,cuenta_premium1]
for i in range(len(lista)):
    lista[i].__str__()


cuenta_basica.depositar(1000)
cuenta_premium.depositar(100000)

cuenta_basica.retirar(10)

cuenta_basica1.retirar(10000000000000000000)


for i in range(len(lista)):
    lista[i].saldo()
