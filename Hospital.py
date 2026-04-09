class Paciente:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.__edad=0
        # Al igualar self.edad = edad, Python llama automaticamente al setter de abajo
        self.edad=edad 

    @property
    def edad(self):
        # Aca el return "entrega" el valor para que parezca una variable normal
        return self.__edad

    @edad.setter
    def edad(self,valor):
        if valor>=0 and valor<=120:
            self.__edad=valor
        else:
            print("Error: la edad debe estar entre 0 y 120")

paciente1=Paciente("Martin",30)
print("Paciente ingresado:",paciente1.nombre,"Edad:",paciente1.edad)


paciente1.edad=150
paciente1.edad=-10


paciente1.edad=31

print("Datos actualizados:",paciente1.nombre,"Edad:",paciente1.edad)