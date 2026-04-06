class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
    

class Pizza(Producto):
    def __init__(self,nombre,precio,tamanio):
        super().__init__(nombre,precio)
        self.tamanio=tamanio
    def __str__(self):
        print("Nombre:",self.nombre,"Precio:",self.precio,"Tamaño:",self.tamanio)

class Bebida(Producto):
    def __init__(self,nombre,precio,volumen):
        super().__init__(nombre,precio)
        self.volumen=volumen
    def __str__(self):
        print("Nombre:",self.nombre,"Precio:",self.precio,"Volumen:",self.volumen)

cocacola=Bebida("CocaCola",1500,"chica")
pizza=Pizza("Muzza",10000,8)
cocacola.__str__()
pizza.__str__()