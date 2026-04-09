class Deposito:
    def __init__(self,nombre,stock_inicial):
        self.nombre=nombre
        self.__stock=0
        self.stock=stock_inicial

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self,valor):
        if valor>=0:
            self.__stock=valor
        else:
            print("Error: el stock no puede ser negativo")

    def agregar(self,cantidad):
        if cantidad>0:
            self.stock=self.stock+cantidad
            print("Se agregaron",cantidad,"unidades. Stock actual:",self.stock)
        else:
            print("Error: la cantidad a agregar debe ser mayor a cero")

    def retirar(self,cantidad):
        if cantidad>0:
            nuevo_stock=self.stock-cantidad
            if nuevo_stock>=0:
                self.stock=nuevo_stock
                print("Se retiraron",cantidad,"unidades. Stock actual:",self.stock)
            else:
                print("Error: no hay suficiente stock para retirar",cantidad)
        else:
            print("Error: la cantidad a retirar debe ser mayor a cero")


deposito1=Deposito("Galpon Central",50)
print("Deposito:",deposito1.nombre,"Stock inicial:",deposito1.stock)

deposito1.agregar(20)


deposito1.retirar(100)


deposito1.retirar(30)


deposito1.stock=-10