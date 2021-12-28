# reconocimiento-facial
Este repositorio contiene un ejemplo de reconocimiento facial basado en deepface, ESP32CAM, python y nodeRed.

Este ejercicio requiere lo siguiente:

- NodeRed
    Se requieren los siguientes nodos
    - node-red-dashboard
    - node-red-contrib-string
    - node-red-contrib-calc

- Python 3.9
    Se requieren los siguientes complementos
    - PIP
    - deepFace
    - pandas
    - paho-mqtt

- Mosquitto MQTT

- Arduino IDE
    Se requieren los siguientes complementos
    - Espressiff board manager

Para hacer comparaciones de rostro, se requiere una base de datos conformada por una serie de sub carpetas que contengan imagenes de las personas registradas. Cada vez que se agrega una persona, debe eliminarse el archivo representations_vgg_face.pkl que se crea en la carpeta my_db

El flow toma una fotografía, la cual será analaizada. Deben actualizarse todas las rutas en los nodos function, exec y string. Debe actualizarse la IP de la cámara en el nodo template.