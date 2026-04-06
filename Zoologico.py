class Animal:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    #????
    def __str__(self):
        print("Nombre:",self.nombre,"edad:",self.edad)
class Leon(Animal):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
        
    def hablar(self):
        print("Nombre:",self.nombre,"edad:",self.edad,"se logra oir: Rawr")

class Pinguino(Animal):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
        
    def hablar(self):
        print("Nombre:",self.nombre,"edad:",self.edad,"se logra oir: (ruido de pinguino)")

class Serpiente(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def hablar(self):
        print("Nombre:",self.nombre,"edad:",self.edad,"se logra oir: tsssst")

leon=Leon("Robert",23)
leon.hablar()
pinguino=Pinguino("Lucas",2)
pinguino.hablar()
serpiente=Serpiente("Cascabel",34)
serpiente.hablar()
