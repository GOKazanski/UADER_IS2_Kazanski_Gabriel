import logging
from Components.Log import Log

# Configuración del logger
logger = logging.getLogger('CorporateLogLogger')

class CorporateLog:
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
        self.log = Log()
        logger.debug("Se inicializa la clase CorporateLog")

    def post(self, uuid_session, accion):
        """Registra una operación en el log."""
        logger.debug(f"Registrando operación en log: sesión {uuid_session}, acción {accion}")
        self.log.post(uuid_session, accion)  # Llama al método post de Log

    def list(self, uuid_cpu, uuid=None):
        """Consulta el log para obtener las entradas de una CPU y sesión específicas."""
        logger.debug(f"Consultando entradas en log para CPU: {uuid_cpu}, sesión: {uuid}")
        return self.log.list(uuid_cpu, uuid)
