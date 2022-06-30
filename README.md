
# FIFA API

Rest API para consolidar la informaci'on de todos los equipos que van a ir al próximo mundial.



## Descripción del proyecto

La FIFA te ha contactado para que le ayudes a consolidar la información de todos los equipos que
van a ir al próximo mundial, así que te dicen que debes crear una API con un CRUD para cada una
de la siguiente información:

• Equipo

    - Nombre del Equipo
    - Imagen de Bandera
    - Escudo del Equipo

• Jugadores del equipo, con los siguientes datos de cada jugador:

    - Foto del jugador
    - Nombre
    - Apellido
    - Fecha de nacimiento
    - Posición en la que juega
    - Número de camiseta
    - ¿Es titular?
• Cuerpo técnico

    - Nombre
    - Apellido
    - Fecha de nacimiento
    - Nacionalidad
    - Rol (técnico | asistente | médico | preparador)




## API contruida con
Los requerimientos especificos se encuentran en el archivo requeriments.txt
 - [Python](https://www.python.org/)
 - [Django](https://www.djangoproject.com/)
 - [Django Rest Framework](https://www.django-rest-framework.org/)
 - [Postgres](https://www.postgresql.org/)
 - [Swagger](https://swagger.io/)



## Authors

- [@devSantiago18](https://www.github.com/octokatherine)


## Puesta en marcha

Para hacer uso de nuestra API debemos:

* Clonar el repositorio de la aplicacion en el directorio de nuestra preferencia 

```bash
  $ git clone https://github.com/devSantiago18/prueba_rebus.git
```

* Crear un entorno virtual Utilizando Python3

```bash
  $ python3 -m virtualenv env
```

* Activar nuestro repositorio
```bash
# Windows
  $ .\env\Scripts\activate
# Unix
  $ source env/Scripts/Activate
```
* Instalar los requerimientos desde nuestro archivo de requerimientos

```bash
  $ pip install -r requeriments.txt
```

Una vez cumplidos estos pasos ya nuestro entorno debe estar preparador para ejecutar nuestro servidor

```
  Usted debe tener instalador el sistema gestor de bases de datos PostgreSql,
  creado y configurado la base de datos para que todo vaya correctamente 
```
- [Configuracion PostgreSql con Django](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04)

* Finalmente iniciamos nuestro sevidor local

```bash
  $ python manage.py runserver
```

# ¡ Vamos a Jugar !
Para hacer uso de esta API y entender como funciona puede acceder:
```bash
  http://localhost:8000/swagger/
```
Tambien puede acceder a la documentacion en:
```bash
  http://localhost:8000/redoc/
```
