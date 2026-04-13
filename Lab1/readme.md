# Laboratorio 1

### Integrantes
<br>
Nombres: &emsp; &emsp; &emsp; &emsp; &nbsp; &nbsp; &nbsp; RUT:
<br>
José Mena &emsp; &emsp; &emsp; &emsp; &emsp; 21.665.813-2
<br>
Martín Basulto &emsp; &emsp; &emsp; &nbsp; 20.360.437-8
<br>
Mario Rojas &emsp; &emsp; &emsp; &emsp; &ensp; 21.574.655-0
<br>
Marcel Gutierrez &ensp; &ensp; &ensp; &ensp; &nbsp; 21.228.115-8
<br>
Benjamín Leiva &emsp; &emsp; &emsp; &nbsp; 21.679.330-7
<br>
<br>

## Tabla de contenidos
* [Descripción del laboratorio](#descripción-del-laboratorio)
* [Herramientas](#herramientas)
* [Como ejecutar la simulación webots](#instrucciones)

<br><br><br><br><br>

## 2. Descripción del laboratorio
Este laboratorio tiene como objetivo realizar un análisis cinemático de un robot móvil diferencial mediante el software de simulación Webots. A través de la integración de conceptos sobre actuadores y modelos matemáticos de movimiento, se busca programar trayectorias específicas para evaluar el comportamiento dinámico del sistema y validar las fórmulas cinemáticas en un entorno controlado.  

## 3. Herramientas
Para el desarrollo de este laboratorio se utilizaron las siguientes herramientas tecnológicas: Python (versión 3.14.3) y Webots (versión R2025a).

### 3.1 Python
Se empleó el lenguaje de programación Python para programar la lógica de control de los robots. Esto permitió gestionar parámetros como la velocidad y ejecutar las trayectorias necesarias para conformar las figuras propuestas en la guía de laboratorio.

### 3.2 Webots
Se utilizó Webots como entorno de simulación para modelar y observar el comportamiento del robot de tipo diferencial e-puck. Este software permitió visualizar los distintos casos de estudio mencionados anteriormente y proporcionó la interfaz necesaria para integrar el código de control desarrollado en Python.

## 4. Como ejecutar la simulación en webots
A continuación se explicarán los pasos para ejecutar el codigo en webots

### 4.1 PASO 1
Primero debemos cargar el siguiente link : https://github.com/TheFanking/Laboratorio-1.git , que es el link al respositorio de github donde encontraremos los archivos necesarios.

### 4.2 PASO 2
Una vez ingresado al link nos aparecerá algo como esto :
<img width="1369" height="651" alt="Captura desde 2026-04-12 18-14-41" src="https://github.com/user-attachments/assets/99471106-ab9e-48e8-93ca-b27cfb4cb3c9" />
en esta sección deberemos seleccionar la carpeta "Lab1".

### 4.3 PASO 3
Una vez nos encontramos en la carpeta deberemos seleccionar el .zip que se encuentra en la carpeta llamado "Lab1".

### 4.4 PASO 4
Una vez seleccionado nos aparecerá algo como esto 
<br>
<br>
<img width="1773" height="142" alt="Captura desde 2026-04-12 18-25-20" src="https://github.com/user-attachments/assets/e3081069-90c6-488f-899a-7666be50f6ca" />
En esta sección se puede observar un boton que dice "Raw" Y dos botones hacia la iznquierda habra un boton que dice "Download raw file" deberemos clickear en el para descargar el archivo .zip necesario para ejecución de la simulación en webots

### 4.5 PASO 5
Una vez descargardo el arhivo deberemos extraerlo en una carpeta de preferencia. Una vez extraido nos encontraremos con los siguientes archivos
<img width="882" height="547" alt="Captura desde 2026-04-12 18-34-44" src="https://github.com/user-attachments/assets/e522ea97-2048-4f02-b448-21b6c4a79dc0" />

### 4.6 PASO 6
Una vez hecho los pasos anteriores debemos abrir la aplicación de webots.

### 4.7 PASE 7
Una vez iniciado nos aparecerá un menú como esto: 
<img width="1860" height="997" alt="Captura desde 2026-04-12 18-39-11" src="https://github.com/user-attachments/assets/81469aca-e0b8-437e-845c-bcbb4c4d834f" />

ahora en esta sección deberemos clickear la sección "file" que se encuentra en la esquina superior derecha y luego "open World"

### 4.8 PASO 8
Ahora deberemos buscar la carpeta donde se extrajo anteriormente y buscar la carpeta llamada "worlds" y luego seleccionar el archivo main.wbt

### 4.9 PASO 9 
Ahora deberia aparecer lo siguiente donde se nos muestra la simulación y el codigo python para controlar el movimiento
<img width="1860" height="997" alt="Captura desde 2026-04-12 18-44-02" src="https://github.com/user-attachments/assets/4ec55faa-aef7-444e-9950-41cda74c0874" />

### 4.10 PASO EXTRA
Una vez en la interfaz para poder cambiar entre los diferentes desafios debemos ir a la consola dentro de webots y cambiar entre un valor 1 a 5 en la variable DESAFIO y luego apretar el boton "reset simulation" o CTRL + shift + T.

## 5. Cinematica
Para comprender el movimiento del robot, es fundamental definir las ecuaciones que relacionan la velocidad de las ruedas con el movimiento global del sistema en el plano. Estas fórmulas permiten calcular la trayectoria y son la base para la programación de los controladores.

### 5.1 Velocidades Lineal y Angular

En un robot de tracción diferencial, el movimiento depende de la velocidad lineal de su rueda derecha ($v_R$) y su rueda izquierda ($v_L$). Las ecuaciones cinemáticas principales son:

* **Velocidad lineal del centro del robot ($v$):** Es el promedio de las velocidades de ambas ruedas. Representa qué tan rápido se traslada el robot.
    $$v = \frac{v_R + v_L}{2}$$

* **Velocidad angular del robot ($\omega$):** Determina la tasa de rotación del robot sobre su propio eje (en radianes por segundo).
    $$\omega = \frac{v_R - v_L}{L}$$
    *Donde **$L$** representa la distancia entre los puntos de contacto de las ruedas (track width).*

### 5.2. Relación con los Motores (Velocidad Angular de las Ruedas)

Dado que en el entorno de simulación **Webots** el control de los motores se realiza mediante velocidad angular ($\omega_{wheel}$), es necesario considerar el radio de las ruedas ($r$) para realizar la conversión:

$$v_R = r \cdot \omega_R$$
$$v_L = r \cdot \omega_L$$

Al sustituir estas igualdades en las ecuaciones de movimiento, obtenemos las fórmulas finales que se aplican en el código controlador:

1.  **Cálculo de la traslación:** $v = \frac{r}{2}(\omega_R + \omega_L)$
2.  **Cálculo de la rotación:** $\omega = \frac{r}{L}(\omega_R - \omega_L)$

### 5.3 Comportamientos fundamentales
De las ecuaciones anteriores se derivan tres casos canónicos que son la base de todos los desafíos:
<img width="950" height="357" alt="Captura desde 2026-04-12 21-03-22" src="https://github.com/user-attachments/assets/c92414b7-280d-4e30-a580-25a8f7c1b781" />

