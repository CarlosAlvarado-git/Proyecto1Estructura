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
# JMETER RESULATADOS
## CASO "FORMULADO":
  ### -TENEMOS 251 REQUEST QUE POR CADA USUARIO SE NECESITA 6 SEGUNDOS PARA QUE SE COMPLETEN LAS REQUEST .
    -EN PROMEDIO 1 USURARIO EN HACER LAS 251 REQUEST SE TARDA: 23ms. ENTONCES LA IDEA ES LLEGAR A CIERTO NÚMERO DE USUARIO QUE REALICEN LAS MISMAS REQUEST Y QUE ESE PROMEDIO NO  SUBA POR MÁS DE 70ms.
  ### 1 USUARIO:
  ![image](https://user-images.githubusercontent.com/61555440/109573348-82144300-7ab4-11eb-8e9f-63ade34678b8.png)
  ### NUEVA PRUEBA CON 2 USUARIOS:
      PARA LOGRAR EL FIN, HAY QUE PREGUNTARSE CUÁNTOS USUARIOS LO HARÁN Y EN QUÉ TIEMPO. 
    PRUEBA DE DOS USUARIOS.
    EL PROMEDIO SUBIÓ A 27, OSEA UN CAMBIO DE 5 MS POR USUARIO AGREGADO.
    1 = 23
    2 = 27
    X = 70 
    70/5 = X
    14 USUARIOS EN TEORÍA. 
    14*6S = 84 S, SE UTILIZARÁ (ERA 90 PERO DIÓ ERROR) AL DUPLICAR EL TIEMPO SERÍAN 180 S
   ### 2 USUARIOS
   ![image](https://user-images.githubusercontent.com/61555440/109573374-8b9dab00-7ab4-11eb-9e2e-456981af4029.png)
   ### 
     LUEGO DE LA PRUEBA ANTERIOR, NOS DIMOS CUENTA QUE EL HACERLO CON UNA ECUACIÓN MATEMÁTICA, EL PROMEDIO SIGUE SIN SUBIR A LOS 70 MS QUE BUSCAMOS COMO MÁXIMO. SE AUMENTARÁ LA CANTIDAD DE USUARIOS Y TIEMPO. CON 1216.703/MINUTO DE REQUEST = CON 14 USUARIOS Y 180 S
   ### 14 USUARIOS
   ![image](https://user-images.githubusercontent.com/61555440/109573411-9e17e480-7ab4-11eb-9b9c-a755879c9302.png)
       CON LO ANTERIOR PODEMOS EMPEZAR A SUPONER UNA MAYOR CANTIDAD DE USUARIO PODRÍA REALIZAR UN CAMBIO.
    EL BANCO ESTÁ EN 3 ZONAS DE LA CAPITAL, ENTONCES ESTIMAMOS QUE LAS REQUEST POR MINUTO SERÁN DE 3000. 
    SE BUSCARÁ OBTENER ESE VALOR AUMENTANDO LOS USUARIO. 
    Se intentó duplicar todo pero el programa sigue siendo eficiente con 24ms de promedio al igual que las request por minuto. 
   ### 28 USUARIOS
   ![image](https://user-images.githubusercontent.com/61555440/109573464-bdaf0d00-7ab4-11eb-905b-eb8e4bce0a49.png)
  ### Se buscará un aumento exagerado: 100 usuarios y 20 minutos.
  ![image](https://user-images.githubusercontent.com/61555440/109573475-c69fde80-7ab4-11eb-9a33-e160c39bcb29.png)
  ### 1000 USUARIOS:
  ![image](https://user-images.githubusercontent.com/61555440/109573513-d8818180-7ab4-11eb-93e1-fc9886fdf3d9.png)
  ![image](https://user-images.githubusercontent.com/61555440/109573521-db7c7200-7ab4-11eb-887e-315b201c220e.png)
  ![image](https://user-images.githubusercontent.com/61555440/109573541-de776280-7ab4-11eb-92e8-f5494c8ac6ca.png)

  
