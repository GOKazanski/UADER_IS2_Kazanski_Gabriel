## Índice
- [Ingeniería de Software II  - Trabajo Práctico Final](#ingeniería-de-software-ii----trabajo-práctico-final)
  - [Grupo](#grupo)
  - [Entrega 1 - Diseño de componentes](#entrega-1---diseño-de-componentes)
    - [Diagrama de Clases](#diagrama-de-clases)
    - [Diagrama de Secuencia](#diagrama-de-secuencia)
    - [Diagrama de Actividad](#diagrama-de-actividad)
    - [Diagrama de Casos de uso](#diagrama-de-casos-de-uso)
    - [Diagrama de Estados](#diagrama-de-estados)
    - [Diagrama de Componentes](#diagrama-de-componentes)
  - [Entrega 2 - Aplicativo implementado](#entrega-2---aplicativo-implementado)
    - [Ejecución de UADER\_IS2\_TPFI.py del grupo](#ejecución-de-uader_is2_tpfipy-del-grupo)
  - [Entrega 3 - Aplicativo probado](#entrega-3---aplicativo-probado)
    - [Ejecución de UADER\_IS2\_TPFI.py](#ejecución-de-uader_is2_tpfipy)
    - [Ejecución de test\_corporate.py](#ejecución-de-test_corporatepy)
  - [Entrega 4 - Memoria](#entrega-4---memoria)
    - [Archivos del TP](#archivos-del-tp)
    - [Descripción del Diseño del Sistema](#descripción-del-diseño-del-sistema)
    - [Patrón Singleton](#patrón-singleton)
    - [Uso de AWS DynamoDB](#uso-de-aws-dynamodb)
    - [Resumen de la Arquitectura y Conexiones](#resumen-de-la-arquitectura-y-conexiones)
    - [Ejecución de UADER\_IS2\_listCorporateData.py](#ejecución-de-uader_is2_listcorporatedatapy)
    - [Ejecución de UADER\_IS2\_listLog.py](#ejecución-de-uader_is2_listlogpy)
    - [Pruebas de test](#pruebas-de-test)

# Ingeniería de Software II  - Trabajo Práctico Final
![image](https://github.com/GOKazanski/UADER_IS2_Kazanski_Gabriel/assets/90653565/8532959d-ba73-435e-b900-b3d7ced1fcc1)

## Grupo
- Enzo Etcheto
- Luigi Mete
- Maximiliano Kazanski
- Gabriel Omar Kazanski

## Entrega 1 - Diseño de componentes

Se debe desarrollar una aplicación para gestionar una infraestructura que permita proveer servicios corporativos para la adquisición de datos centralizados desde una base de datos.
Se compone por tres bloques de componentes: FrontEnd, BackEnd y la Base de datos

FrontEnd:
Contiene la interfaz de usuario, la cual mostrará los datos devueltos por el componente del BackEnd

BackEnd:
Contiene los componentes desarrollados en Python de CorportateData el cual obtiene los datos que obtiene desde la base de datos por medio de un JSON y CorporateLog que realiza una auditoría de cada movimiento que se hace para obtener los datos obtenidos de la clase log que guarda cada transacción.

Base de datos:
La base de datos de estilo DynamoDB que se encuentra alojada en AWS, donde los componentes del Back obtienen los datos.

### Diagrama de Clases
![image](https://github.com/user-attachments/assets/a2ed8469-74dd-4fc7-bf94-be2211b14261)

### Diagrama de Secuencia
![image](https://github.com/user-attachments/assets/a8a903ba-ec6d-4825-ab92-cc2c6d94d7fc)

### Diagrama de Actividad
![image](https://github.com/user-attachments/assets/50031db3-7fef-4c65-99db-277269db2b3e)

### Diagrama de Casos de uso
![Imagen de WhatsApp 2024-10-23 a las 19 55 59_a3f0c4f9](https://github.com/user-attachments/assets/e968b386-fcd6-4934-9c7a-63adfaa78d96)

### Diagrama de Estados
![Imagen de WhatsApp 2024-10-23 a las 19 55 58_bd0a91d4](https://github.com/user-attachments/assets/2c0ce10e-28c1-4ff1-8203-f195bddab820)

### Diagrama de Componentes
![Imagen de WhatsApp 2024-10-23 a las 19 55 58_8b5f1541](https://github.com/user-attachments/assets/c54528a9-517b-4d4c-932b-d0153c59a8be)

- [Volver al Índice](#índice)

## Entrega 2 - Aplicativo implementado

### Ejecución de UADER_IS2_TPFI.py del grupo
![Imagen de WhatsApp 2024-10-29 a las 19 03 23_b55c0b2c](https://github.com/user-attachments/assets/4c4425f4-8628-40d7-b36f-e17b4582c06c)

- [Volver al Índice](#índice)

## Entrega 3 - Aplicativo probado

### Ejecución de UADER_IS2_TPFI.py
![image](https://github.com/user-attachments/assets/c8a3910d-87a2-4ddf-ab1f-136b4d3e134d)

### Ejecución de test_corporate.py
![image](https://github.com/user-attachments/assets/2d19e4b9-84ad-4c3e-8322-89be712cca30)

- [Volver al Índice](#índice)

## Entrega 4 - Memoria

### Archivos del TP
- TP_Final\
  - Components\
    - CorporateData.py
    - CorporateLog.py
    - Log.py
  - .gitignore
  - clear_dynamodb_table.py
  - Readme.md
  - test_corporate.py
  - UADER_IS2_listCorporateData.py
  - UADER_IS2_listLog.py
  - UADER_IS2_TPFI.py

### Descripción del Diseño del Sistema

- Objetivo: El sistema tiene como objetivo gestionar datos corporativos de una organización, incluyendo información sobre la sede y su número de identificación fiscal (CUIT), con registro de operaciones en una base de datos de log en DynamoDB.
- Componentes Principales:
  - CorporateData: Responsable de manejar datos específicos de la sede, como CUIT, idSeq, y otros atributos de ubicación.
  - CorporateLog y Log: Gestionan el registro y recuperación de operaciones en la tabla CorporateLog en DynamoDB.

### Patrón Singleton

- Descripción: El patrón Singleton se utiliza en CorporateData y CorporateLog para asegurar que solo exista una instancia de cada clase en el sistema. Esto evita la duplicación de instancias y asegura que todas las operaciones interactúen con la misma instancia, optimizando el uso de recursos y controlando el acceso a la información.
- Implementación: En ambas clases (CorporateData y CorporateLog), el método getInstance() revisa si existe una instancia ya creada. Si no, crea una nueva. Esto asegura que cualquier llamada al método retorne siempre la misma instancia de la clase.

### Uso de AWS DynamoDB

- Base de Datos: El sistema utiliza AWS DynamoDB para manejar dos tablas:
  - CorporateData: Almacena información relevante de la sede, como domicilio, localidad, CUIT y el identificador de secuencia idSeq.
  - CorporateLog: Almacena registros de operaciones realizadas en el sistema. Cada entrada incluye session_id, CPUid, method (nombre del método ejecutado), y timestamp (momento de ejecución).

### Resumen de la Arquitectura y Conexiones

- Interacciones: CorporateData interactúa con CorporateLog cuando se registra cada operación realizada en la base de datos. Las llamadas a los métodos en CorporateData (como getData y getCUIT) resultan en registros de auditoría que son gestionados a través de CorporateLog.
- Seguridad y Manejo de Errores: Cada método de consulta en CorporateData y CorporateLog maneja excepciones mediante mensajes de error, asegurando que los errores en la conexión o las consultas a DynamoDB no interrumpan el funcionamiento del sistema.

### Ejecución de UADER_IS2_listCorporateData.py


### Ejecución de UADER_IS2_listLog.py


### Pruebas de test
![image](https://github.com/user-attachments/assets/40373c2a-59dd-43a1-9def-55714a130cc4)

- [Volver al Índice](#índice)