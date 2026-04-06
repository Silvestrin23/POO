class Prenda:
    def __init__(self,nombre,talla,precio):
        self.nombre=nombre
        self.talla=talla
        self.__precio=0
        self.set_precio(precio)

    def get_precio(self):
        print("El precio actual es:",self.__precio)

    def set_precio(self,valor):
        if valor>=0:
            self.__precio=valor
        else:
            print("Error: el precio no puede ser menor a cero")

    def aplicar_descuento(self,porcentaje):
        if porcentaje>=0 and porcentaje<=100:
            descuento=self.__precio*(porcentaje/100)
            self.__precio=self.__precio-descuento
            print("Descuento aplicado. Nuevo precio:",self.__precio)
        else:
            print("Error: el porcentaje debe estar entre 0 y 100")

remera=Prenda("Remera","L",15000)
remera.get_precio()
remera.aplicar_descuento(20)
remera.aplicar_descuento(120)
remera.set_precio(-100)
remera.set_precio(20000)
remera.get_precio()