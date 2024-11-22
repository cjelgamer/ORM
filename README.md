# Gestión de Películas (CRUD con Flask y SQLAlchemy)

Este proyecto es un sistema de gestión de películas desarrollado en Python con Flask y SQLAlchemy. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una base de datos MySQL.

---

## 🚀 Características
- Gestión completa de películas (CRUD).
- Uso de **Flask** como framework web.
- Conexión a una base de datos MySQL utilizando **SQLAlchemy** como ORM.
- Diseño moderno y responsivo con **Bootstrap** y **CSS personalizado**.
- Organización del código en rutas, modelos y utilidades.

---

## 📁 Estructura del Proyecto

```plaintext
ORM/
├── models/
│   └── movie.py         # Modelo para la tabla 'Movie'
├── routes/
│   └── movies.py        # Rutas principales del CRUD
├── static/
│   └── styles.css       # CSS personalizado
├── templates/
│   ├── index.html       # Página principal (lista de películas)
│   ├── edit.html        # Formulario para editar películas
│   └── new.html         # Formulario para agregar películas
├── utils/
│   └── db.py            # Configuración de la base de datos
├── app.py               # Configuración principal de Flask
├── index.py             # Entrada principal para ejecutar el proyecto
└── venv/                # Entorno virtual (no incluido en el repositorio)
```

## 🛠️ Configuración del Proyecto
### 1. Clonar el repositorio
```
git clone <[URL del repositorio](https://github.com/cjelgamer/ORM.git)>
```
```
cd ORM
```

### 2. Crear y activar el entorno virtual
En Windows:
```
python -m virtualenv venv
```
activar:
```
.\venv\Scripts\activate
```


### 4. Instalar el cliente MySQL
En Windows:
```
pip install mysqlclient
```

## 5. Configurar la base de datos
Crea una base de datos en MySQL llamada moviesdb:

sql
```
CREATE DATABASE moviesdb;
```
Actualiza la configuración de la base de datos en el archivo app.py:

python
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<usuario>:<contraseña>@localhost/moviesdb'
```

## 🚀 Ejecución del Proyecto
### 1. Inicializar la base de datos
Ejecuta el archivo index.py para crear las tablas necesarias:

bash
```
python index.py
```
### 2. Iniciar la aplicación
Ejecuta el servidor:

bash
```
python index.py
```
Accede a la aplicación en http://127.0.0.1:5000.

## 💻 Dependencias
Python 3.x
Flask
Flask-SQLAlchemy
MySQL
mysqlclient
Bootstrap 5 (CDN)
## 🌟 Funcionalidades
Crear Película:
Completa el formulario en la página de agregar y guarda los datos.
Listar Películas:
Muestra todas las películas en la página principal.
Editar Película:
Haz clic en "Editar" para modificar los detalles de una película.
Eliminar Película:
Haz clic en "Eliminar" para borrar una película.
