from app import db
from datetime import datetime

class Movie(db.Model):
  __tablename__ = 'movies'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(200), nullable=False)
  release_date = db.Column(db.DateTime)
  post_date = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<Movie %r>' % self.id

  def to_dist(self):
    return {
      "id": self.id,
      "title": self.title,
      "release_date": self.release_date,
      "post_date": self.post_date
    }