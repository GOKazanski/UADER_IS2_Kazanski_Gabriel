![image](https://github.com/GOKazanski/UADER_IS2_Kazanski_Gabriel/assets/90653565/8532959d-ba73-435e-b900-b3d7ced1fcc1)

# Ingeniería de Software II

## Trabajo Práctico N 06 - Ingeniería Reversa, Re-factoría y Re-Ingeniería

## Índice

* [Consignas](#consignas)
* [Links](#links)
* [Presentación del Trabajo Práctico](#presentación-del-trabajo-práctico)
    - [Taller](#taller)
    - [Consigna 2](#consigna-2)
    - [Consigna 3](#consigna-3)
    - [Consigna 4](#consigna-4)

## Consignas
1) La instalación dispone de un programa llamado getJason.pyc legado de un sistema
ya obsoleto y del cual no existen fuentes. El mismo fue compilado utilizando
Python versión 3.6, la cual es una versión ya deprecada.
2) El mismo permite recuperar el API token para acceder a microservicios bancarios
del Banco XXX contenido en un archivo JSON. Se desea reusar el programa
asegurando que puede recuperarse cualquier clave existente en el archivo JSON el
que ahora contiene claves múltiples indicándola como argumento (siendo el
default “token1”).
- a) Obtenga el programa getJason.pyc junto con el archivo JSON de prueba
provisto y la documentación existente. Utilice Python 3.6. Documente lo que
encuentre.
- b) Ejecútelo, verifique la correspondencia entre lo que indica la documentación y
el comportamiento real. Realice brevemente pasos 1 a 6 de la metodología
explicada para ingeniería reversa.
- c) Instale el paquete Python uncompyle6.
- d) Ejecute uncompyle6 y obtenga el código fuente getJason.py.
- e) Ejecútelo para verificar se comporta como getJason.pyc en el paso 2.b.
- f) Identifique las razones para las diferencias encontradas en el punto anterior
entre el código obtenido y la documentación del mismo.
- g) Modifique el programa getJason.py para que actúe como indica la
documentación y satisfaga los requerimientos de reuso.
- h) Valide y verifique su nuevo comportamiento bajo una versión mas avanzada de
Python (3.11 por ejemplo).
- i) Remueva los comentarios hechos por el proceso de de-compilación.
- j) Genere la nueva versión de getJason.pyc mediante compilación
- l) Utilice python –m compileall getJason.py
- k) Verifique y valide.
3) Continuando con el programa getJason.pyc (y su versión fuente getJason.py) del
ejercicio anterior se ha decidido que el programa tiene un código deficiente para lo
crítico que resulta para la instalación y por lo tanto se lo someterá a un proceso de
re-factoría.
- a) Manteniendo las modificaciones realizadas en el punto anterior analice una
intervención que permita aplicar programación orientada a objetos de forma
que transforme al programa.
- b) La transformación consistirá en reorganizar el código para utilizar un patrón de
diseño “Singleton”.
- c) La clase resultante del punto anterior debe poder ser ejecutada desde línea de
comandos, al efecto deberán mejorarse las condiciones de chequeo de los
parámetros externos de ejecución de forma de hacer a la ejecución más
robusta. El objetivo primario es que el programa nunca termine con un error de
sistema y siempre lo haga con un error del programa controlado.
- d) Para hacer la convergencia entre el programa original y su versión re
factorizada utilice una estrategia “Branching by abstraction”.
- e) Aproveche a agregar comentarios al programa de su funcionamiento y una
carátula donde se especifique es propiedad de la compañía (“copyright UADERFCyT-IS2©2024 todos los derechos reservados).
- f) También mejore el funcionamiento controlando que los argumentos de
ejecución sean correctos y en caso de no serlos la terminación sea con un error
controlado y no una excepción del lenguaje.
- g) Agregue además que si el programa se ejecuta con el argumento “-v” emita la
versión del mismo. En éste caso lo denominará “versión 1.1”.
- h) Haga una corrida de revisión con el analizador estático de código pylint y corrija
las observaciones hasta que el mismo otorgue un puntaje de 8 o superior.
4) Continuando con el programa getJason.py previamente utilizado se usará ahora en
el contexto de un cambio organizacional más profundo, donde resulta indicado
aplicar una intervención de tipo re-ingeniería.
- a) En el proceso de pagos anterior un empleado decide sobre que banco liberar
un pago y elige un token respectivo para poderlo realizar.
- b) En realidad el proceso de decisión se puede automatizar, bastará que exista
saldo en la respectiva cuenta y que los pagos se hagan en forma balanceada.
- c) Partiendo del objeto singleton que dado un nombre de token (banco) da la
clave integrarlo en un nuevo componente que ante una solicitud de pago
seleccione automáticamente la cuenta desde la que se hará el mismo. La
información de relación entre banco (token) y clave está en un archivo JSON
llamado sitedata.json
- d) Se realizará una clase utilizando el patrón “cadena de comando” que controle
las dos cuentas (las correspondientes a “token1” y “token2”, ambas
inicialmente con un saldo de $1000.- la correspondiente a “token1” y $2000.- la
correspondiente a “token2”.
- e) Se realizarán pedidos de pago de $500.- (número de pedido, monto) los que
alternativamente se rutearán a cada cuenta que tenga saldo suficiente., para lo
cual se indicará el número de pedido, el token a utilizar y el monto del pago
realizado como salida de la clase. Prever una función de “listado” que muestre
todos los pagos realizados por orden cronológico (utilizar un patrón iterator al
efecto).
- f) Además se avanzará la versión a 1.2.
- g) Se documentará apropiadamente todo el programa.
- h) Se hará una ejecución de verificación con pylint para chequear el resultado
obteniendo un puntaje de 8 o superior. Hacer las modificaciones que fueran
necesarias para conseguirlo.

[Volver al índice](#índice)

## Links
+ [Facultad de Ciencia y Tecnología - UADER](https://fcytcdelu.uader.edu.ar/).
+ [Documentación del README.md](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

[Volver al índice](#índice)

## Presentación del Trabajo Práctico

### Taller
```
pip install uncompyle6
uncompyle6 old_primes.pyc
uncompyle6 old_primes.pyc > old_primes_00.py

python -m compileall old_primes_02.py
```
### Consigna 2
Punto 2. b)
```
PS C:\Users\gokaz\OneDrive\Documentos\UADER\3Anio\IS2\Códigos\UADER_IS2_Kazanski_Gabriel\TP_06> python --version
Python 2.7.18
PS C:\Users\gokaz\OneDrive\Documentos\UADER\3Anio\IS2\Códigos\UADER_IS2_Kazanski_Gabriel\TP_06> python.exe .\getJason.pyc ./sitedata.json token1
C598-ECF9-F0F7-881A
```
+ Paso 1: Colección de datos
    - Código fuente: getJason.pyc
    - Librerías: json, sys
+ Paso 2: Extraer información
    - Inventario de objetos disponibles: Archivos: getJason.py, sitedata.json - Librerías: json, sys
+ Paso 3: Extraer estructura
    - Variables: jsonfile, jsonkey, myfile, data, obj
+ Paso 4: Registra funcionalidad
    - ![image](https://github.com/GOKazanski/UADER_IS2_Kazanski_Gabriel/assets/90653565/796c35ea-8d83-4877-8ed4-0e6041080abc)
+ Paso 5: Registra flujo de datos
    - Secuencia: Leer archivo -> obtener datos de JSON -> Acceder a clave -> Imprimir resultado
+ Paso 6: Documentación
    - ![image](https://github.com/GOKazanski/UADER_IS2_Kazanski_Gabriel/assets/90653565/89e2a871-741d-4feb-8d11-1ce3e46bf17f)

Punto 2. d)
```
PS C:\Users\gokaz\OneDrive\Documentos\UADER\3Anio\IS2\Códigos\UADER_IS2_Kazanski_Gabriel\TP_06> uncompyle6 getJason.pyc > getJason.py
PS C:\Users\gokaz\OneDrive\Documentos\UADER\3Anio\IS2\Códigos\UADER_IS2_Kazanski_Gabriel\TP_06> more getJason.py
# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55
import json, sys
jsonfile = sys.argv[1]
jsonkey = sys.argv[2]
with open(jsonfile, 'r') as myfile:
    data = myfile.read()
obj = json.loads(data)
print str(obj[jsonkey])

# okay decompiling getJason.pyc
```
Punto 2. e)
![image](https://github.com/GOKazanski/UADER_IS2_Kazanski_Gabriel/assets/90653565/0a88911b-2a77-42d7-9e94-b6364c703b82)

Punto 2. h)
![image](https://github.com/GOKazanski/UADER_IS2_Kazanski_Gabriel/assets/90653565/ec50c1ad-092c-43b1-91b9-367cd06fa405)

Punto 2. l)
![image](https://github.com/GOKazanski/UADER_IS2_Kazanski_Gabriel/assets/90653565/b7fff3b6-8556-4297-acdd-b19f043531a4)

Punto 2. k)
![image](https://github.com/GOKazanski/UADER_IS2_Kazanski_Gabriel/assets/90653565/a7aa76d6-d330-4357-a3be-f9dc060791c6)

[Volver al índice](#índice)

### Consigna 3
Punto 3. g)
![image](https://github.com/GOKazanski/UADER_IS2_Kazanski_Gabriel/assets/90653565/b85f1088-2485-46d6-bb10-68c18977f39a)

Punto 3. h)
![image](https://github.com/GOKazanski/UADER_IS2_Kazanski_Gabriel/assets/90653565/dd655b8e-bbdf-4428-8dc8-b5b1a6e8e875)

[Volver al índice](#índice)

### Consigna 4
Punto 4. h)
![image](https://github.com/GOKazanski/UADER_IS2_Kazanski_Gabriel/assets/90653565/14b10e93-b2f4-4027-abc0-ead839fc13d8)

![image](https://github.com/GOKazanski/UADER_IS2_Kazanski_Gabriel/assets/90653565/efa10bba-b093-4e03-81a3-39ad4fd40aa0)

![image](https://github.com/GOKazanski/UADER_IS2_Kazanski_Gabriel/assets/90653565/99084524-9f76-43a6-8100-a7f46bd6477a)

[Volver al índice](#índice)
