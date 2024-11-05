## Índice
- [Ingeniería de Software II  - Trabajo Práctico Final](#ingeniería-de-software-ii----trabajo-práctico-final)
  - [Docentes](#docentes)
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
    - [Configuración de las credenciales en AWS](#configuración-de-las-credenciales-en-aws)
    - [Resumen de la Arquitectura y Conexiones](#resumen-de-la-arquitectura-y-conexiones)
    - [Componentes de la Aplicación](#componentes-de-la-aplicación)
    - [Ejecución de UADER\_IS2\_TPFI.py](#ejecución-de-uader_is2_tpfipy-1)
    - [Ejecución de UADER\_IS2\_listCorporateData.py](#ejecución-de-uader_is2_listcorporatedatapy)
    - [Ejecución de UADER\_IS2\_listLog.py](#ejecución-de-uader_is2_listlogpy)
    - [Pruebas de test](#pruebas-de-test)

# Ingeniería de Software II  - Trabajo Práctico Final
![image](https://github.com/GOKazanski/UADER_IS2_Kazanski_Gabriel/assets/90653565/8532959d-ba73-435e-b900-b3d7ced1fcc1)

## Docentes
- Profesor Pedro Ernesto Colla
- Auxiliar Hernán Sánchez

## Grupo
- Enzo Etcheto
- Gabriel Omar Kazanski
- Luigi Mete
- Maximiliano Kazanski

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

### Configuración de las credenciales en AWS
En terminal Bash
```
$ aws configure
AWS Access Key ID [None]: ###############
AWS Secret Access Key [None]: ########################
Default region name [None]: us-east-1
Default output format [None]: Json
```

### Resumen de la Arquitectura y Conexiones

- Interacciones: CorporateData interactúa con CorporateLog cuando se registra cada operación realizada en la base de datos. Las llamadas a los métodos en CorporateData (como getData y getCUIT) resultan en registros de auditoría que son gestionados a través de CorporateLog.
- Seguridad y Manejo de Errores: Cada método de consulta en CorporateData y CorporateLog maneja excepciones mediante mensajes de error, asegurando que los errores en la conexión o las consultas a DynamoDB no interrumpan el funcionamiento del sistema.

### Componentes de la Aplicación

- CorporateData - En esta clase se manejan los métodos:
  - GetData: Obtiene los datos de la tabla CorporateData.
  - GetCuit: A través de un ID obtiene la sede y Cuit de la tabla CorporateData.
  - GetSeqID: Obtiene e incrementa el ID de secuencia.
  - ListCorporateData: A través de un ID, lista los elementos que coinciden con el respectivo ID.
  - ListCorporateLog: A través del identificador único de CPU, lista todos los elementos que se encuentren con este identificador.

- CorporateLog - Es una clase intermedia que se utiliza como puente para la clase log, Se manejan los métodos:
  - Post: Se comunica con el post de la clase Log.
  - List: Se comunica con el list de la clase Log.

- Log - En esta clase se manejan los métodos:
  - Post: Registra los datos del CPU, id de sección, método que utiliza, hora y fecha de la máquina.
  - List: Lista a partir del identificador único de CPU los registros asentados en la tabla Corporate log.

- Test_Corporate
  1. Verifica que las instancias de CorporateData y CorporateLog implementen correctamente el patrón Singleton.
  2. Prueba que getData devuelva la información esperada de la sede y contenga claves como sede y domicilio.
  3. Prueba que getCUIT devuelva el CUIT y contenga las claves CUIT y sede.
  4. Verifica que getSeqID retorne el ID de secuencia (idSeq).
  5. Prueba que post de CorporateLog se ejecute sin errores al registrar una operación.
  6. Prueba que list en CorporateLog devuelva una lista de registros, y que cada entrada de log contenga una clave method.
  7. Prueba que listCorporateData retorne una lista con todos los registros de CorporateData.
  8. Verifica que listCorporateLog en CorporateData retorne una lista.
  9. Verifica que getData retorne un error para un ID inexistente.
  10. Verifica que getCUIT retorne un error para un ID inexistente.
  11. Verifica que getSeqID retorne un error para un ID inexistente.
  12. Simula un error de conexión para verificar el manejo de errores.
  13. Verifica que el post en CorporateLog registre una entrada con los datos correctos.
  14. Prueba que getData maneje argumentos faltantes o vacíos.

### Ejecución de UADER_IS2_TPFI.py
![image](https://github.com/user-attachments/assets/0d73c7e5-00ee-4d5a-af30-b8e6b13f0b46)
![image](https://github.com/user-attachments/assets/10c8e5e8-94ff-4e05-b3cc-884723269abb)
![image](https://github.com/user-attachments/assets/b80efbf0-e039-4b28-92c3-f15493cae19b)
![image](https://github.com/user-attachments/assets/82452cc4-b5a4-4941-873b-681e69c07ac3)

### Ejecución de UADER_IS2_listCorporateData.py
![image](https://github.com/user-attachments/assets/c7904a60-cfdc-4a8e-926b-cdb31b985381)

### Ejecución de UADER_IS2_listLog.py
![image](https://github.com/user-attachments/assets/30105e95-e371-498d-8114-0f81c065a708)

### Pruebas de test
![image](https://github.com/user-attachments/assets/40373c2a-59dd-43a1-9def-55714a130cc4)

- [Volver al Índice](#índice)
