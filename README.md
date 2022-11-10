# Repositorio_prueba_tecnica_Django
FRAMEWORK: DJANGO
LENGUAJE: PYTHON

ACTIVIDAD:
Se debe desarrollar una página web que contenga un formulario donde se pueda realizar el alta de personas y la visualización de los datos cargados mediante una
tabla.


DOCUMENTACIÓN.
Para poder encontrar los archivos que nombrare a posterior ingresar en la carpeta App. Los archivos son: models.py, forms.py, urls.py, views.py,la carpeta de templates, entre otros.

Models.py:
En este archivo podemos encontrar los modelos de datos usados por el backend.Este proyecto consta de un solo modelo que se describirá a continuación.

Descripcion: modelo Usuario. Campos: -nombre(CharField, nombre del usuario) -apellido(CharField,apellido del usuario) -correo(CharField, correo electrónico del usuario.) 

Forms.py:
En este archivo podemos encontrar un solo formulario para cargar los datos que quedan guardados en nuestra base de datos.Además se aplica la validacion de los campos (-nombre y apellido: no aceptan números, correo:tiene que respetar el formato ejemplo@ejemplo.com) mediante el uso de widgets.

Urls.py:
Contiene cada una de las rutas de las vistas de la app. 

Views.py:
Aparecen todas las vistas que se utilizan en la app. Se poseen dos vista para crear y mostrar a los usuarios

Crear un usuario: vista registrarUsuario.

Mostrar todos los usuarois: vista mostrarUsuarios

Templates:
Es una carpeta donde se encuentran todos los archivos HTML,usados por la app. Se utilza una platilla de BOOSTRAP y se aplica el concep de herencia a cada archivo.

Autor: Joner Claudio
