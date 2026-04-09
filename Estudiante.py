class Estudiante:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.__nota=0
        self.nota=nota

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self,valor):
        if valor>=0 and valor<=10:
            self.__nota=valor
        else:
            print("Error: la nota debe estar entre 0 y 10")

    def aprobo(self):
        if self.__nota>=6:
            return True
        else:
            return False

estudiante1=Estudiante("Sofia",8)
print("Estudiante:",estudiante1.nombre,"Nota:",estudiante1.nota)
print("¿Aprobo?:",estudiante1.aprobo())


estudiante1.nota=15


estudiante1.nota=4
print("Actualizacion - Estudiante:",estudiante1.nombre,"Nota:",estudiante1.nota)
print("¿Aprobo?:",estudiante1.aprobo())