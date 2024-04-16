"""
4. Implemente una clase que permita a un número cualquiera imprimir su valor,
luego agregarle sucesivamente.
a. Sumarle 2.
b. Multiplicarle por 2.
c. Dividirlo por 3.
Mostrar los resultados de la clase sin agregados y con la invocación anidada a
las clases con las diferentes operaciones. Use un patrón decorator para
implementar.

Con Decorator
"""
import os

# Clase base que contiene el número original
class Number:
    def __init__(self, value):
        self._value = value

    def calculate(self):
        return self._value

    def history(self):
        return str(self._value)

# Decorador que suma 2 al número
class AddTwo(Number):
    def __init__(self, number):
        self._number = number

    def calculate(self):
        return self._number.calculate() + 2

    def history(self):
        return f"(Número original: {self._number.history()} + 2)= {self._number.calculate()+2}"

# Decorador que multiplica el número por 2
class MultiplyByTwo(Number):
    def __init__(self, number):
        self._number = number

    def calculate(self):
        return self._number.calculate() * 2

    def history(self):
        return f"({self._number.history()} * 2)= {self._number.calculate()*2}"

# Decorador que divide el número por 3
class DivideByThree(Number):
    def __init__(self, number):
        self._number = number

    def calculate(self):
        return self._number.calculate() / 3

    def history(self):
        return f"({self._number.history()} / 3)= {self._number.calculate()/3}"

# Main para demostrar el funcionamiento
if __name__ == '__main__':
    os.system("cls" if os.name == 'nt' else "clear")  # Limpia la consola según el sistema operativo
    Numero_ingresado=int(input("Ingrese un numero: "))
    original_number = Number(Numero_ingresado)
    modified_number = DivideByThree(MultiplyByTwo(AddTwo(original_number)))

    # Mostrando los resultados sin y con modificaciones
    print("\nNúmero original: %s" % (original_number.calculate()))
    print("\nAnidación de operaciones: %s\n" % (modified_number.history()))
    print("Número modificado: %s\n" % (modified_number.calculate()))
