from flask import Blueprint, render_template, request, redirect, url_for
from models.movie import Movie
from utils.db import db

movies = Blueprint("movies", __name__)

# Ruta principal: Mostrar todas las películas
@movies.route("/")
def home():
    movies_list = Movie.query.all()
    return render_template("index.html", movies=movies_list)

# Ruta para mostrar la página con el formulario de agregar película
@movies.route("/new", methods=["GET"])
def new_movie_form():
    return render_template("new.html")

# Ruta para procesar la nueva película
@movies.route("/new", methods=["POST"])
def add_movie():
    nombre = request.form["nombre"]
    duracion = request.form["duracion"]
    genero = request.form["genero"]

    new_movie = Movie(nombre, duracion, genero)
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for("movies.home"))

# Ruta para eliminar una película
@movies.route("/delete/<id>")
def delete(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("movies.home"))

# Ruta para mostrar el formulario de edición
@movies.route("/edit/<id>")
def edit(id):
    movie = Movie.query.get(id)
    return render_template("edit.html", movie=movie)

# Ruta para actualizar los datos de una película
@movies.route("/update/<id>", methods=["POST"])
def update(id):
    movie = Movie.query.get(id)
    movie.nombre = request.form["nombre"]
    movie.duracion = request.form["duracion"]
    movie.genero = request.form["genero"]

    db.session.commit()
    return redirect(url_for("movies.home"))

# Ruta para mostrar información sobre la aplicación
@movies.route("/about")
def about():
    return render_template("about.html")
