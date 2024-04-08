"""
1. Provea una clase que dado un número entero cualquiera retorne el factorial del mismo,
debe asegurarse que todas las clases que lo invoquen utilicen la misma instancia de clase.
"""

class SingletonMeta(type):
    """
    Esta es una clase meta que define el comportamiento de Singleton.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class FactorialCalculator(metaclass=SingletonMeta):
    """
    Esta clase calcula el factorial de un número.
    Utiliza el patrón Singleton para asegurar una única instancia.
    """

    def factorial(self, n):
        if n < 0:
            return "El número debe ser no negativo."
        elif n == 0 or n == 1:
            return 1
        else:
            factorial = 1
            for i in range(2, n + 1):
                factorial *= i
            return factorial

# Creando instancias y probando que son la misma
calculator1 = FactorialCalculator()
calculator2 = FactorialCalculator()

if calculator1 == calculator2:
    # Calculando algunos factoriales
    print(calculator1.factorial(5))  # 120
    print(calculator2.factorial(7))  # 5040
