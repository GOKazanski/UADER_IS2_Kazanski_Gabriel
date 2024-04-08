"""
2. Elabore una clase para el cálculo del valor de impuestos a ser utilizado por todas las
clases que necesiten realizarlo. El cálculo de impuestos simplificado deberá recibir un
valor de importe base imponible y deberá retornar la suma del cálculo de IVA (21%), IIBB (5%)
y Contribuciones municipales (1,2%) sobre esa base imponible.
"""

class SingletonMeta(type):
    """
    Esta es una metaclase que se encarga de implementar el patrón Singleton.
    Garantiza que solo se cree una instancia de una clase que use esta metaclase.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # Si la instancia no existe, la crea y la guarda en el diccionario.
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        # Retorna la instancia existente.
        return cls._instances[cls]

class TaxCalculator(metaclass=SingletonMeta):
    """
    Esta clase calcula los impuestos sobre un importe base. Implementa el patrón Singleton
    para asegurar que todas las clases que lo utilicen accedan a la misma instancia.
    """

    def calculate_taxes(self, base_amount):
        """
        Calcula los impuestos basados en el importe base proporcionado.

        :param base_amount: El importe base imponible.
        :return: La suma total de los impuestos calculados.
        """
        if base_amount < 0:
            return "El importe base no puede ser negativo."

        IVA = 0.21  # 21%
        IIBB = 0.05  # 5%
        MunicipalContribution = 0.012  # 1.2%

        # Calcula cada uno de los impuestos.
        total_taxes = (base_amount * IVA) + (base_amount * IIBB) + (base_amount * MunicipalContribution)
        return total_taxes

# Uso de la clase TaxCalculator para calcular impuestos
if __name__ == "__main__":
    tax_calculator1 = TaxCalculator()
    tax_calculator2 = TaxCalculator()

    # Verifica si ambas variables apuntan a la misma instancia.
    print(f"¿Es la misma instancia de TaxCalculator?: {tax_calculator1 is tax_calculator2}")

    # Calcula y muestra los impuestos para un importe base.
    base_amount = 1000  # Supongamos un importe base de 1000 unidades monetarias.
    taxes = tax_calculator1.calculate_taxes(base_amount)
    print(f"Total de impuestos sobre un importe base de {base_amount}: {taxes}")
