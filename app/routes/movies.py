from flask import request, jsonify, Blueprint
from app import db
from app.models.movies import Movie
from marshmallow import ValidationError
from app.schemas.movie_schemas import MovieSchema

movies_bp = Blueprint('movies', __name__)
@movies_bp.route('/movies', methods=["POST", "GET"])
def movies():
  if request.method == "POST":
    schema = MovieSchema()
    try:
      data = schema.load(request.get_json())
    except ValidationError as err:
      return jsonify({
        "error": "Invalid data",
        "message": err.messages
      }), 404
    movie = Movie(**data)
    db.seesion(movie)
    db.seesion.commit()
    return jsonify({
      "message": "Movie added successfully",
      data: movie.to_dist()
    }), 200

  else:
    movies = Movie.query.order_by(Movie.title).all()
    movie_list = [movie.to_dist() for movie in movies]
    if movies:
      return jsonify({
        "message": "Movies list",
        "data": movie_list
      })
    else:
      return jsonify({
        "message": "No movies found"
      }), 404
