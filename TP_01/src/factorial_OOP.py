class Factorial:
    def __init__(self):
        pass

    def factorial(self, num):
        if num < 0:
            print("Factorial de un número negativo no existe")
        elif num == 0:
            return 1
        else:
            fact = 1
            while(num > 1):
                fact *= num
                num -= 1
        return fact

    def run(self, min_num = 1, max_num = 60):
        if min_num > max_num:
            print("El primer número es mayor al segundo.")
            return

        for num in range(min_num, max_num + 1):
            print("Factorial ", num, "! es ", self.factorial(int(num)))