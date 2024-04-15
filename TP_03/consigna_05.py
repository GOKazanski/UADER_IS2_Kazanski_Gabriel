"""
5. Extienda el ejemplo visto en el taller en clase de forma que se pueda utilizar para construir
aviones en lugar de vehículos. Para simplificar suponga que un avión tiene un “body”, 2 turbinas,
2 alas y un tren de aterrizaje.

Con Builder
"""

import os
#*--------------------------------------------------------------------
#* La clase Director orquesta la construcción del objeto indicando
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------
class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getPlane(self):
        plane = Plane()

        # Fuselaje
        body = self.__builder.getBody()
        plane.setBody(body)

        # Turbinas
        for _ in range(2):
            turbine = self.__builder.getTurbine()
            plane.attachTurbine(turbine)

        # Alas
        for _ in range(2):
            wing = self.__builder.getWing()
            plane.attachWing(wing)

        # Tren de aterrizaje
        landing_gear = self.__builder.getLandingGear()
        plane.setLandingGear(landing_gear)

        # Retorna el avion completo
        return plane

#*----------------------------------------------------------------
#* Esta es la definición de un objeto vehiculo inicializando
#* todos sus atributos
#*----------------------------------------------------------------
class Plane:
    def __init__(self):
        self.__turbines = []
        self.__wings = []
        self.__body = None
        self.__landing_gear = None

    def setBody(self, body):
        self.__body = body

    def attachTurbine(self, turbine):
        self.__turbines.append(turbine)

    def attachWing(self, wing):
        self.__wings.append(wing)

    def setLandingGear(self, landing_gear):
        self.__landing_gear = landing_gear

    def specification(self):
        print("Fuselaje: %s" % (self.__body.shape))
        print("Cantidad de turbinas: %d, %d HP cada una" % (len(self.__turbines), self.__turbines[0].horsepower))
        print("Cantidad de alas: %d, Tipo: %s" % (len(self.__wings), self.__wings[0].type))
        print("Tren de aterrizaje: %s" % (self.__landing_gear.type))


#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class Builder:
    def getBody(self): pass
    def getTurbine(self): pass
    def getWing(self): pass
    def getLandingGear(self): pass

#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un avion
#* Establece instancias para tomar fuselaje, turbinas, alas y tren de aterrizaje
#* estableciendo las partes específicas que, un avion,
#* deben tener esas partes
#*-------------------------------------------------------
class PlaneBuilder(Builder):
    def getBody(self):
        body = Body()
        body.shape = "Aerodinámico"
        return body

    def getTurbine(self):
        turbine = Turbine()
        turbine.horsepower = 2500
        return turbine

    def getWing(self):
        wing = Wing()
        wing.type = "Comercial"
        return wing

    def getLandingGear(self):
        landing_gear = LandingGear()
        landing_gear.type = "Retráctil"
        return landing_gear

#*----------------------------------------------------------------
#* Define partes genéricas para un avion (sin inicializar)
#*----------------------------------------------------------------
class Body:
    shape = None

class Turbine:
    horsepower = None

class Wing:
    type = None

class LandingGear:
    type = None

#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():

#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el
#* proceso de construcción
#*----------------------------------------------------------------
    planeBuilder = PlaneBuilder()
    director = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un avion
#*----------------------------------------------------------------
    director.setBuilder(planeBuilder)

#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un avion según
#* la hoja de ruta
#*----------------------------------------------------------------
    plane = director.getPlane()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
    plane.specification()
    print ("\n\n")

#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
    os.system("cls")
    print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avión\n")

    main()
