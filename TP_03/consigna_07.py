"""
7. Imagine una situación donde pueda ser de utilidad el patrón “abstract factory”.
"""

"""
Una posible aplicación del patrón "Abstract Factory" se encuentra en la industria culinaria,
específicamente en la producción de alimentos como tartas, pastas y empanadas.
Este patrón facilita la elaboración de versiones tradicionales de estos productos,
así como variantes adaptadas a dietas específicas como la celíaca o la vegana.

Abstract Factory:
Se define una interfaz para la creación de diferentes tipos de alimentos relacionados con
la preparación de comidas, tales como Pastas, Empanadas y Tartas.

Concrete Factories:

TraditionalFoodFactory: Produce alimentos tradicionales que contienen gluten.
GlutenFreeFoodFactory: Fabrica alimentos libres de gluten, seguros para personas con celiaquía.
VeganFoodFactory: Elabora alimentos que no contienen productos de origen animal, adecuados para veganos.

Productos:

Pastas: Disponibles en versiones tradicionales, libres de gluten, o veganas,
        utilizando ingredientes específicos para cada dieta.
Empanadas: Varían desde rellenos tradicionales como carne o pollo, hasta versiones con masa sin gluten
        o rellenos veganos como vegetales y sustitutos de carne.
Tartas: Ofrecen una gama de rellenos, adaptadas para ser preparadas con o sin gluten,
        o completamente libres de productos de origen animal.

"""