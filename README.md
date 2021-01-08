# RPC_Agenda

Proyecto realizado para el ramo Sistemas Distribuidos, UCSC. 

## Pre-Requisitos

- python 3
- virtualenv
- Conexión a internet para descargar paquetes

## Instalación pre-requisitos

- Asegurarse de tener instalado python3
>>python3 --version
- Si no tiene instalado Python, instale por terminal
>>sudo apt-get install python3
- Instale un entorno virtual 
>> sudo apt-get install python-virtualenv

## Construir el proyecto

- Puede clonar este repositorio o bien descargarlo.
- Una vez descargado, debe crear un entorno virtual.
- Para crear entorno virtual
>>virtualenv nombre_entorno_virtual --python=python3
- Para activar su entorno virtual
>> source nombre_entorno_virtual/bin/activate

## Instalación requerimientos

- Una vez en su entorno virtual, deberá instalar los siguientes paquetes.
- Para el servidor
>> pip install spyne

>> pip install lxml
- para el cliente
>> pip install Flask

>> pip install flask-wtf

## Ejecutar el Cliente y Servidor

- Para ejecutar el servidor, debe acceder a la carpeta serverAgenda y ejecutar
>> python mainserver.py
- Para ejecutar el cliente, debe acceder a la carpeta clientAgenda y ejecutar
>> python mainclient.py
- Si todo resulta bien, acceda a
- http://127.0.0.1:5000


