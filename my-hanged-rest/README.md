# Esqueleto Flask

Estructura básica de carpetas en Flask

**1 -** Clonar repositorio.

```sh
    git clone https://github.com/danielbalzate/flask-projects.git flask-projects
    cd  flask-projects/my-hanged-rest
```

**2 -** Cree un entorno virtual de Python e instale Flask:

```sh
    virtualenv venv -p python3
    venv/bin/pip install flask
```

**3 -** Ejecute el proyecto de Flask con: (run.py debe tener permisos de ejecución: _chmod + x run.py_):

```sh
    ./run.py
```

Por defecto, este proyecto abrirá el puerto 5555, intente en su navegador con **localhost:5555**

[API USUARIOS]
Login:
POST http://localhost:5555/register
Ejemplo:

```sh
{
	"name": "Daniel",
	"email": "thebest@gmail",
	"pass": "password"
}
```

Respuesta si existe:

```sh
    {
    "message": "That email already exists!"
    }
```

Respuesta si no existe:

```sh
    {
    "message": "Logged!"
    }
```

Consultar todos los usuarios registrados:
GET http://localhost:5555/users

[
{
"id": "5e421d259f1a3b57f304f8bc",
"mail": "thebest@g.com",
"name": "Dani admin"
},
{
"id": "5e421da49f1a3b57f304f8bd",
"mail": "mary@g.com",
"name": "Mary Jane"
}
]

````

Respuesta:

Consultar usuario por id:
GET http://localhost:5555/users/id

Respuesta:

```sh
[
    {
        "id": "5e421d259f1a3b57f304f8bc",
        "mail": "thebest@g.com",
        "name": "Dani admin"
    }
]
````
