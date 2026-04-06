class Animal():
    def __init__(self,nombre,especie,edad):
        self.nombre=nombre
        self.especie=especie
        self.edad=edad
    def __str__(self):
        print("Nombre:",self.nombre,"| Especie:",self.especie,"| Edad:",self.edad)
    

nombre=input("Ingrese el nombre del animal: ")
especie=input("Ingrese la especie del animal: ")
edad=int(input("Ingrese la edad del animal: "))
animal=Animal(nombre,especie,edad)
animal.__str__()