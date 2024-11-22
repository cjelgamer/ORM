from flask import Flask
from routes.movies import movies
from utils.db import db  # Importar la instancia global de db

app = Flask(__name__)

# Configurar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mypassword@localhost/moviesdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy con la aplicación
db.init_app(app)

# Registrar el blueprint de las rutas
app.register_blueprint(movies)
