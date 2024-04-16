"""
5. Imagine una situación donde pueda ser de utilidad el patrón “flyweight”.
"""

"""
Una situación podría ser la de un club que ofrece distintos tipos de membresías
(por ejemplo, bronce, plata, oro, platino), cada una con un conjunto diferente de
beneficios y descuentos.
Pero, muchos de los beneficios como acceso a ciertas instalaciones, descuentos en eventos
o precios preferenciales en servicios pueden ser comunes entre varias categorías, aunque
el grado del beneficio puede variar.

Entonces el objeto "Flyweight Factory" se encarga de crear y administrar los objetos Flyweight para
los beneficios. Cuando se necesita configurar o modificar los beneficios para una categoría específica,
la fábrica verifica si ya existe un Flyweight para el beneficio y lo reutiliza, ajustando solo los
detalles específicos para esa categoría mediante estados extrínsecos.
Esto permite que cambios en los beneficios comunes se realicen en un solo lugar, afectando
automáticamente a todas las categorías que comparten ese beneficio.
"""
