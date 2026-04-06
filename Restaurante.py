class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.__precio=0
        self.set_precio(precio)

    def get_precio(self):
        return self.__precio

    def set_precio(self,valor):
        if valor>=0:
            self.__precio=valor
        else:
            print("Error: el precio no puede ser negativo")

class Entrada(Producto):
    def __init__(self,nombre,precio,tamanio):
        super().__init__(nombre,precio)
        self.tamanio=tamanio
    def __str__(self):
        print("Entrada:",self.nombre,"Precio:",self.get_precio(),"Tamaño:",self.tamanio)

class PlatoPrincipal(Producto):
    def __init__(self,nombre,precio,guarnicion):
        super().__init__(nombre,precio)
        self.guarnicion=guarnicion
    def __str__(self):
        print("Plato:",self.nombre,"Precio:",self.get_precio(),"Guarnicion:",self.guarnicion)

class Postre(Producto):
    def __init__(self,nombre,precio,sabor):
        super().__init__(nombre,precio)
        self.sabor=sabor
    def __str__(self):
        print("Postre:",self.nombre,"Precio:",self.get_precio(),"Sabor:",self.sabor)

class Mesa:
    def __init__(self):
        self.__pedidos=[]

    def agregar_pedido(self,producto):
        self.__pedidos.append(producto)
        print("Se agrego a la mesa el producto:",producto.nombre)

    def calcular_total(self):
        total=0
        for comida in self.__pedidos:
            
            total=total+comida.get_precio()
        print("El total a pagar de la mesa es:",total)


empanadas=Entrada("Empanadas",2500,"Docena")
milanesa=PlatoPrincipal("Milanesa de carne",6500,"Papas fritas")
helado=Postre("Helado",3000,"Dulce de leche")

empanadas.__str__()
milanesa.__str__()
helado.__str__()

mesa1=Mesa()
mesa1.agregar_pedido(empanadas)
mesa1.agregar_pedido(milanesa)
mesa1.agregar_pedido(helado)

mesa1.calcular_total()