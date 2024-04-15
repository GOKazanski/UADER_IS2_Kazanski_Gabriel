"""
2. Elabore una clase para el cálculo del valor de impuestos a ser utilizado por todas las
clases que necesiten realizarlo. El cálculo de impuestos simplificado deberá recibir un
valor de importe base imponible y deberá retornar la suma del cálculo de IVA (21%), IIBB (5%)
y Contribuciones municipales (1,2%) sobre esa base imponible.

Con Factory
"""

from abc import ABC, abstractmethod


class TaxCalculator(ABC):
    @abstractmethod
    def calculate(self, amount: float) -> float:
        pass


# devuelve a cliente el calculo de los impuestos más el importe cargado
class GeneralTaxCalculator(TaxCalculator):
    def calculate(self, amount: float) -> float:
        IVA = 0.21 #21%
        IIBB = 0.05 #5%
        CONTRIBUCIONES = 0.012 #1,2%
        total_tax = amount * (IVA + IIBB + CONTRIBUCIONES)
        return total_tax + amount


class TaxCalculatorFactory:
    @staticmethod
    def get_tax_calculator() -> TaxCalculator:
        return GeneralTaxCalculator()


# Cliente (main)
if __name__ == "__main__":
    # El cliente solicita al factory una instancia de una calculadora de impuestos.
    tax_calculator = TaxCalculatorFactory.get_tax_calculator()

    importe_base = 10000  # Importe base imponible
    total_con_impuestos = tax_calculator.calculate(importe_base)

    impuestos = total_con_impuestos - importe_base

    print(f"Importe base: {importe_base}")
    print(f"La suma de los impuestos es: {impuestos}")
    print(f"Total con impuestos: {total_con_impuestos}")
