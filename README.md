# Proyecto Arquitectura de Software
## Introducion y Funcionalidad
en la presente actividad se necesito la creacion de producto que ha estado constantemente evolucionando con el plantamiento del problema
este codigo, arquitectura, proyecto tiene el fin de simular un software para la atencion de compra de celulares, por lo cual lo unico que en principio se necesita ejecutar es el "**main.py**" 
la cual ejecuta una interfaz de tipo consola en la cual puede interactuar, dando respuesta del tipo numerico (1,2,3), y completar los campos con Strings como se observa en la captura: 
![Ejemplo]("./img/img1.png")



## Plantamiento del problema
una empresa de celulares XXX nos pide la creacion de un software que le permita gestionar todo lo referente a venta de sus celulares asi que nos pide la creacion de su software, la empresa tiene la ide de tener un servidor dedicado para la ejecucion de su programa, al igual que nosotros por buenas constumbres aplicamos los principios de SOLID y algunos patrones de diseño para la realizacion de software
## Dependencias
este proyecto esta contruido enteramente en python por lo que utilizamos:
### Gestor de Base de Datos
* SqLite3
### Librerias Python
* datetime
* os
* sys
### Python
* Version 3.11.9
## Installacion del Proyecto
para la instalcion del proyecto lo que usted necesisita es Python instalado en su equipo, aunque en la version en realidad no importa, tenga cuidado con la version 2 ya que algunos mecanismo no funciona de la misma forma en python 2 y python 3.  
luego debe descargar el proyecto ya sea usando el ZIP que se obtiene al clickear en **Code**, o clonado el proyecto
utilizando el siguiente comando: 
```
git clone <url del proyecto>
``` 
para ambos cosos usted hara el uso del despliege de **Code** por lo que le dejamos una imagen de referencia
![img de referencia]("./img/img2.png")

luego tengra que descargar la version de sqlite3 para python usando el comando pip 
```
pip install db-sqlite3
``` 
en caso de que el gestor de paquetes no este registrado  **como variable del sistema** puede ejecutar el siguiente comando en una terminal
```
python -m pip install db-sqlite3
``` 

en caso de que no tenga como **variable de entorno python** aconsegamos volver a installar python, usted puede tambien optar por poner su variable de entorno manualmente por lo que le pedimos averiguar el procedimiento para su Sistema operativo
## Principios Solid
* S: Single Responsibility Principle(SRP) cada clase solo llega a tener una única responsabilidad para ser utilizada
* O: open/closed: las clases se pueden extender con nuevas funcionalidades sin la necesidad de modificar el código que ya tienen
* L: Liskov Substitution Principle (LSP) las clases nacen de clases más abstractas por lo que llegan a ser específicas
* I. Interface Segregation Principle(ISP) se crean interfaces específicas para cada interfaz 
* D: Dependency Inversion Principle (DIP) las clases de alto nivel no depende de clases de bajo nivel

## Imprementacion de Patrones de Diseño
* Creacional: Singleton (para la implementación de la clase baseDatos y factura)
* Comportamiento: Intérprete(para la implementación de la clase interpreterDB)
* Estructural: Facade(para la implementación de la clase Sistema)

## Arquitectura 3 Capas
* Capa de acceso a datos: datos
* Capa de negocio: negocio
* Capa de presentación: presentación
