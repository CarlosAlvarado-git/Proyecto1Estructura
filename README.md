# Proyecto1Estructura
# Api de sistema de cajas fuertes del banco <nombre>. 

  ## Problem:
  No hay un sistema de gestión eficiente de claves de seguridad de cajas fuertes: No hay una forma de manejar eficientemente un sistema de ingreso de claves de seguridad de cajas fuertes para el banco X.
  El usuario no puede gestionar su caja de seguridad: El banco no le provee ningún api para poder gestionar sus propia caja fuerte.
  El banco no tiene una forma de modificar sus parámetros de autenticidad: El banco no tiene una base de datos y un api para poder cambiar sus parámetros de autenticidad.
  ## Goals:
  -API funcional para el 1 de Marzo: Tener un API funcional para que tanto los clientes y el banco puedan gestionar las cajas fuertes. 
  -Software para manejar con facilidad las acciones de las cajas fuertes durante cada día. 
  ## Context:
  -El banco X no cuenta con un sistema para gestionar sus cajas fuertes, además, los clientes del banco no pueden ver información detallada de sus cajas fuertes. Con el nuevo sistema, se busca que tanto el Banco como los clientes puedan obtener información detallada de una caja fuerte y tener una gestión eficiente de cajas fuertes.  
  ## Detailed Solution:
  La API cuenta con tres rutas, la primera es para la creación de cajas fuertes, en esta ruta el cliente puede ingresar su clave, teléfono, dirección y monto (cantidad de dinero), posteriormente se ingresan a la base de datos. La segunda es para la verificación y apertura de la caja fuerte que haya sido seleccionada. La tercera es para eliminar una caja fuerte por medio de una clave.
  ## Dates:
  -Para el Sábado 13, código interno de rutas sin ningún diseño HTML. Es decir, tener el backend de cada ruta. 
  -Para miércoles 17 de Febrero, nueva visualización, rutas adaptadas por cambios al momento de avanzar con el proyecto y decisión de si utilizar un archivo Csv, yaml o json. 
  -Para el miércoles 24, creación de rutas y manejo de archivo csv para utilizarlo como base de datos. 
  -Para el viernes 26, rutas con cProfiling y separación de font y server de la api. 
  -El proyecto se entrega el día lunes 1 de Marzo.
  
  # Diagrama de casos de uso:
  ![image](https://user-images.githubusercontent.com/61554803/109401776-39268800-7916-11eb-9d22-09e221467fe3.png)
  Link: https://lucid.app/lucidchart/invitations/accept/5a2a3726-ce2d-4c1f-881a-db6a1518c77b
  # PROFILING:
  ## Profiling Caja abierta:
  ![image](https://user-images.githubusercontent.com/61555440/109408494-e49ffe80-794f-11eb-8479-1b22b64db6f1.png)
  ## Profiling Caja eliminada:
  ![image](https://user-images.githubusercontent.com/61555440/109408550-65f79100-7950-11eb-870d-a491b472af3d.png)
  ## Profiling Crear caja:
  ![image](https://user-images.githubusercontent.com/61555440/109408621-cedf0900-7950-11eb-89ba-af07380f0b5b.png)
