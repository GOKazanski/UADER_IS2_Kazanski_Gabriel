from Components.Log import Log

class CorporateLog:
    # Atributo de clase para almacenar la instancia Singleton
    _instance = None

    @staticmethod
    def getInstance():
        """Obtiene la instancia Singleton de CorporateLog. Si no existe, crea una nueva instancia."""
        if CorporateLog._instance is None:
            CorporateLog._instance = CorporateLog()
        return CorporateLog._instance

    def __new__(cls, *args, **kwargs):
        """Método para asegurar que solo se cree una instancia de CorporateLog (patrón Singleton)."""
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Inicializa la clase CorporateLog creando una instancia de Log para registrar operaciones."""
        self.log = Log()  # Instancia de Log para gestionar los registros de auditoría

    def post(self, uuid_session, accion):
        """Registra una operación en el log.

        Args:
            uuid_session (str): Identificador único de la sesión.
            accion (str): Nombre de la acción a registrar (por ejemplo, el método que fue llamado).
        """
        self.log.post(uuid_session, accion)  # Llama al método post de Log para registrar la acción

    def list(self, uuid_cpu, uuid=None):
        """Lista las entradas de log para una CPU y sesión específicas.

        Args:
            uuid_cpu (int): Identificador único de la CPU.
            uuid (str, opcional): Identificador único de la sesión para filtrar resultados.

        Returns:
            list: Lista de entradas de log que coinciden con los parámetros proporcionados.
        """
        return self.log.list(uuid_cpu, uuid)  # Llama al método list de Log para obtener las entradas de log
