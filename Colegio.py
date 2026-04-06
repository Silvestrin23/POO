class Persona:
    def __init__(self,nombre,dni):
        self.nombre=nombre
        self.dni=dni
    
class Alumno(Persona):
    def __init__(self,nombre,dni,curso):
        super().__init__(nombre,dni)
        self.curso=curso
    def presentarse(self):
        print("Nombre:",self.nombre,"dni:",self.dni,"curso:",self.curso)

class Docente(Persona):
    def __init__(self,nombre,dni,materia):
        super().__init__(nombre,dni)
        self.materia=materia
    def presentarse(self):
        print("Nombre:",self.nombre,"dni:",self.dni,"materia:",self.materia)

alumno=Alumno("Mateo",435574545,"5B")
profesor=Docente("Diaz",34543543,"Matematicas")
alumno.presentarse()
profesor.presentarse()
