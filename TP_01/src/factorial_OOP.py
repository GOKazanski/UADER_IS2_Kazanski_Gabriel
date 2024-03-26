class Factorial:
    """
    Una clase para calcular el factorial de un número.

    La clase Factorial proporciona métodos para calcular el factorial de un número entero
    no negativo. El factorial de un número n (n!) es el producto de todos los enteros positivos
    menores o iguales a n. Por definición, el factorial de 0 es 1.

    Métodos:
    factorial(num): Calcula el factorial de un número entero no negativo.
    run(num_min, num_max): Imprime los factoriales de todos los enteros en el rango [num_min, num_max].
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de la clase Factorial.
        """
        pass

    def factorial(self, num):
        """
        Calcula el factorial de un número entero no negativo.

        Parámetros:
        num (int): El número entero del cual calcular el factorial.

        Retorna:
        int: El factorial del número dado. Si el número es negativo,
        se imprime un mensaje de error y se retorna None.
        """
        if num < 0:
            print("Factorial de un número negativo no existe.")
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            while(num > 1):
                fact *= num
                num -= 1
            return fact

    def run(self, num_min=1, num_max=60):
        """
        Imprime los factoriales de todos los enteros en el rango especificado, inclusivo.

        Parámetros:
        num_min (int): El límite inferior del rango de números para calcular el factorial. Valor predeterminado = 1.
        num_max (int): El límite superior del rango de números para calcular el factorial. Valor predeterminado = 60.

        Si num_min es mayor que num_max, se imprime un mensaje de error y no se realiza ningún cálculo.
        """
        if num_min > num_max:
            print("El primer número es mayor al segundo.")
            return

        for num in range(num_min, num_max + 1):
            print(f"Factorial {num}! es {self.factorial(int(num))}")

fac = Factorial()

#fac.run()
fac.run(1 , 5)