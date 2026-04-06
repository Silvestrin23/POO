class Libro:
    def __init__(self,titulo,autor,anio,disponible):
        self.titulo=titulo
        self.autor=autor
        self.anio=anio
        self.disponible=disponible
    def esta_disponible(self):
        return self.disponible
    def __str__(self):
        print("El libro",self.titulo,"cuyo autor es:",self.autor,"y su disponibilidad:",self.disponible)

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez",9, True)
libro2 = Libro("1984", "George Orwell",10, False)
libro3 = Libro("El resplandor", "Stephen King",20,False)
libro1.__str__()
libro2.__str__()
libro3.__str__()