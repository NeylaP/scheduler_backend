# Programación de rutas transpotation SAS
Este proyecto es una solución web desarrollada en Django que permite a los usuarios registrar la flota de vehículos y conductores, además de contar con un cronograma de rutas de trabajo por semanas.
Una vez descargado el proyecto desde el repositorio de Github. En la raíz del proyecto se encuentra un archivo requirements.txt que contiene todas las dependencias necesarias para el proyecto. Para instalar estas dependencias, pero primero debe tener el entorno virtual listo, Para crear un entorno virtual en Python, sigue los siguientes pasos:
Abre la terminal o el símbolo del sistema (en Windows).
Navega hasta la carpeta del proyecto que deseas crear el entorno virtual. Ejecuta el siguiente comando en la terminal: 
python -m venv nombre_del_entorno 
donde "nombre_del_entorno" es el nombre que le quieres dar al entorno virtual. Una vez que se haya creado el entorno virtual, actívalo ejecutando el siguiente comando en la terminal:
.\nombre_del_entorno\Scripts\activate (Esto es en Windows)
Luego ya puede ejecutar el siguiente comando:
pip install -r requirements.txt
# Configuración de la Base de Datos
Para la configuración de la base de datos, es necesario tener un servidor de SQL Server disponible y tener acceso a través de un usuario con permisos de administración. En el archivo de configuración del proyecto (settings.py), se debe definir la cadena de conexión a la base de datos, indicando la dirección del servidor, el nombre de la base de datos, el usuario y la contraseña. Asegúrate de que la base de datos tenga el motor de base de datos adecuado (ejemplo: SQL Server, MySQL, PostgreSQL, etc.) y que los permisos de usuario estén configurados correctamente.
Una vez configurada la base de datos, debes crear las tablas necesarias para el proyecto. Para ello, ejecuta los siguientes comandos en una terminal en la raíz del proyecto:
python manage.py makemigrations
python manage.py migrate
Luego de haber ejecutado los comandos recuerde ejecutar los querys que se le proporcionaron.
# Ejecución del Proyecto
Para ejecutar el proyecto, abre una terminal en la raíz del proyecto y ejecuta el siguiente comando:
python manage.py runserver
Con esto ya estaria corriendo perfectamente la parte del backend.
