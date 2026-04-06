class Socio:
    def __init__(self,nombre,dni,plan):
        self.nombre=nombre
        self.dni=dni
        self.plan=plan
    def mostrar_info(self):
        print("Nombre:",self.nombre,"DNI:",self.dni,"Plan:",self.plan)

socio1=Socio("Mateo",46592256,"premium")
socio2=Socio("Roberto",34543455,"estandar")
socio3=Socio("Marcelo",43453434,"basico")
socio1.mostrar_info()
socio2.mostrar_info()
socio3.mostrar_info()