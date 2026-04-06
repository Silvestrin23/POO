class Vehiculo:
    def __init__(self,patente,marca,modelo):
        self.patente=patente
        self.marca=marca
        self.modelo=modelo

class Estacionamiento:
    def __init__(self):
        self.__vehiculos=[]

    def ingresar(self,vehiculo):
        self.__vehiculos.append(vehiculo)
        print("Vehiculo ingresado con patente:",vehiculo.patente)

    def retirar(self,patente):
        encontrado=False
        for auto in self.__vehiculos:
            if auto==patente:
                self.__vehiculos.remove(auto)
                print("Vehiculo retirado. Patente:",patente)
                encontrado=True
                break
        if encontrado==False:
            print("Error: vehiculo no encontrado")

    def mostrar_disponibles(self):
        print("Autos actualmente en el estacionamiento:")
        for auto in self.__vehiculos:
            print("Patente:",auto.patente,"Marca:",auto.marca,"Modelo:",auto.modelo)

auto1=Vehiculo("AA111AA","Ford","Fiesta")
auto2=Vehiculo("BB222BB","Chevrolet","Cruze")
auto3=Vehiculo("CC333CC","Toyota","Corolla")

estacionamiento=Estacionamiento()

estacionamiento.ingresar(auto1)
estacionamiento.ingresar(auto2)
estacionamiento.ingresar(auto3)

estacionamiento.mostrar_disponibles()

estacionamiento.retirar("BB222BB")

estacionamiento.mostrar_disponibles()