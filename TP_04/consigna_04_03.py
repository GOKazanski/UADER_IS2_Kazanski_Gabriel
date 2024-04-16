"""
3. Represente la lista de piezas componentes de un ensamblado con sus
relaciones jerárquicas. Empiece con un producto principal formado por tres
sub-conjuntos los que a su vez tendrán cuatro piezas cada uno. Genere clases
que representen esa configuración y la muestren. Luego agregue un subconjunto
opcional adicional también formado por cuatro piezas. (Use el patrón
composite).

Con Composite
"""
import os

# --------------------------------------------------------------------
# Ejemplo de pattern composite adaptado para ensamblaje de productos
# Se genera una clase Component que representa nodos terminales (Piece)
# y una Composite que representa al conjunto (Assembly) y las piezas
# que de él dependen.
# --------------------------------------------------------------------

# ------------- Define una clase para las piezas (componentes terminales)
class Piece:

    def __init__(self, *args):
        # Indenta las posiciones a medida que se agregan
        self.name = args[0]

    def showDetails(self):
        # Imprime el nombre de la pieza
        print("\t" * 2, end="")
        print(self.name)

# ---- Elemento compuesto, representa un conjunto en cualquier nivel de la jerarquía

class Assembly:

    def __init__(self, *args):
        self.name = args[0]
        self.components = []

    def add(self, component):
        self.components.append(component)

    def remove(self, component):
        self.components.remove(component)

    def showDetails(self):
        # Muestra el nombre del conjunto y luego los detalles de cada componente
        print(self.name)
        for component in self.components:
            print("\t", end="")
            component.showDetails()

# Main method
if __name__ == "__main__":
    os.system("cls" if os.name == 'nt' else "clear")  # Limpia la consola según el sistema operativo

    # ------ Crea el nivel superior del ensamblado
    mainProduct = Assembly("Producto Principal")

    # ----- Crea el primer subconjunto y sus piezas
    assembly1 = Assembly("Subconjunto 1")
    assembly1.add(Piece("Pieza 1.1"))
    assembly1.add(Piece("Pieza 1.2"))
    assembly1.add(Piece("Pieza 1.3"))
    assembly1.add(Piece("Pieza 1.4"))

    # ----- Crea el segundo subconjunto y sus piezas
    assembly2 = Assembly("Subconjunto 2")
    assembly2.add(Piece("Pieza 2.1"))
    assembly2.add(Piece("Pieza 2.2"))
    assembly2.add(Piece("Pieza 2.3"))
    assembly2.add(Piece("Pieza 2.4"))

    # ----- Crea el tercer subconjunto y sus piezas
    assembly3 = Assembly("Subconjunto 3")
    assembly3.add(Piece("Pieza 3.1"))
    assembly3.add(Piece("Pieza 3.2"))
    assembly3.add(Piece("Pieza 3.3"))
    assembly3.add(Piece("Pieza 3.4"))

    # ---- Agrega los tres subconjuntos al producto principal
    mainProduct.add(assembly1)
    mainProduct.add(assembly2)
    mainProduct.add(assembly3)

    # ---- Muestra el resultado inicial
    mainProduct.showDetails()

    # ---- Agrega un subconjunto adicional
    print("\nAgrega un subconjunto adicional (Opcional)\n")
    assembly4 = Assembly("Subconjunto 4 (Opcional)")
    assembly4.add(Piece("Pieza 4.1"))
    assembly4.add(Piece("Pieza 4.2"))
    assembly4.add(Piece("Pieza 4.3"))
    assembly4.add(Piece("Pieza 4.4"))

    mainProduct.add(assembly4)

    # ---- Muestra el resultado con el subconjunto adicional
    mainProduct.showDetails()

    # ---- Muestra el resultado final tras la adición
    print("\n-- Resultado final --\n")
    mainProduct.showDetails()
