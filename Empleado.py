class Empleado:
    def __init__(self,nombre,sueldo_base):
        self.nombre=nombre
        self.sueldo_base=sueldo_base

    def calcular_sueldo(self):
        return self.sueldo_base

class EmpleadoFijo(Empleado):
    # Hereda el __init__ de Empleado automaticamente
    def calcular_sueldo(self):
        # El fijo cobra el base sin cambios
        return self.sueldo_base

class EmpleadoPartTime(Empleado):
    def calcular_sueldo(self):
        # El part-time cobra la mitad
        return self.sueldo_base/2

class EmpleadoComision(Empleado):
    def __init__(self,nombre,sueldo_base,comision):
        super().__init__(nombre,sueldo_base)
        self.comision=comision

    def calcular_sueldo(self):
        # El de comision cobra el base mas su extra
        return self.sueldo_base+self.comision


fijo=EmpleadoFijo("Lucas",500000)
part_time=EmpleadoPartTime("Maria",500000)
comision=EmpleadoComision("Juan",500000,150000)

lista_empleados=[fijo,part_time,comision]

print("--- Liquidacion de Sueldos ---")

for empleado in lista_empleados:
    # Aca ocurre la magia: le pedimos el sueldo a "empleado" sin importar de que tipo sea.
    # Cada uno hace su propia cuenta y devuelve el resultado correcto.
    print("Empleado:",empleado.nombre,"- Sueldo a pagar:",empleado.calcular_sueldo())