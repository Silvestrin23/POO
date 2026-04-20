from abc import ABC, abstractmethod

class Contenido(ABC):
    def __init__(self,titulo,duracion_minutos):
        self.titulo=titulo
        self.duracion_minutos=duracion_minutos
        self.__cantidad_reproducciones=0
        
    @property 
    def duracion_minutos(self):
        return self.__duracion_minutos
    
    @duracion_minutos.setter
    def duracion_minutos(self,duracion_minutos):
        if duracion_minutos<=0:
            print("Error, la duracion no puede ser 0 o negativa")
        else:
            self.__duracion_minutos=duracion_minutos

    def reproducir(self):
        self.__cantidad_reproducciones+=1
    
    @abstractmethod
    def duracion_total(self):
        pass
        
class Pelicula(Contenido):
    def __init__(self,titulo,duracion_minutos,director):
        super().__init__(titulo,duracion_minutos)
        self.director=director
    
    def __str__(self):
        return self.titulo + " | Dir: " + self.director
        
    def duracion_total(self):
        return "Duracion de la pelicula: ", self.duracion_minutos

class Serie(Contenido):
    def __init__(self,titulo,duracion_minutos,cantidad_episodios):
        super().__init__(titulo,duracion_minutos)
        self.cantidad_episodios=cantidad_episodios
        
    def __str__(self):
        return self.titulo + " | Episodios: " + str(self.cantidad_episodios)
        
    def duracion_total(self):
        return "Duracion de la serie: ", self.duracion_minutos * self.cantidad_episodios
    
def mostrar_catalogos(contenidos):
    for i in range(len(contenidos)):
        print(contenidos[i])
        print(contenidos[i].duracion_total())

def mostrar_beneficios(usuario):
    print(usuario.nombre, usuario._plan)
    print(usuario.calidad_maxima())
    print(usuario.limite_dispositivos())

class Usuario(ABC):
    def __init__(self,nombre,plan):
        self.nombre=nombre
        self._plan=plan

    @abstractmethod
    def calidad_maxima(self):
        pass

    @abstractmethod
    def limite_dispositivos(self):
        pass

class UsuarioBasico(Usuario):
    def calidad_maxima(self):
        return "480p"
    
    def limite_dispositivos(self):
        return "Cantidad dispositivos",1
    
class UsuarioEstandar(Usuario):
    def calidad_maxima(self):
        return "1080p"

    def limite_dispositivos(self):
        return "Cantidad dispositivos",2
        
class UsuarioPremium(Usuario):
    def calidad_maxima(self):
        return "4K HDR"

    def limite_dispositivos(self):
        return "Cantidad dispositivos",4

peli1 = Pelicula("Inception", 148, "Christopher Nolan")
peli2 = Pelicula("The Matrix", 136, "Hermanas Wachowski")
serie1 = Serie("Breaking Bad", 47, 62)
serie2 = Serie("The Office", 22, 201)

contenidos = [peli1, peli2, serie1, serie2]

user1 = UsuarioBasico("Juan", "Basico")
user2 = UsuarioEstandar("Maria", "Estandar")
user3 = UsuarioPremium("Carlos", "Premium")

usuarios = [user1, user2, user3]

peli1.reproducir()
peli1.reproducir()
serie1.reproducir()

mostrar_catalogos(contenidos)

for i in range(len(usuarios)):
    mostrar_beneficios(usuarios[i])

peli1.duracion_minutos = -5
