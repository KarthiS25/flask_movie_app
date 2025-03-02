from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://karthi:1234@localhost:5432/movie_db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  print("Database URL:", app.config['SQLALCHEMY_DATABASE_URI'])
  db.init_app(app)
  migrate.init_app(app, db)

  from app.routes import blueprints
  for bp in blueprints:
    app.register_blueprint(bp)

  with app.app_context():
    db.create_all()

  return app