from app import db

class Theatre(db.Model):
  __tablename__ = 'theatres'
  id =db.Column(db.Integer, primary_key=True)
  name =db.Column(db.String(200), nullable=False)
  post_date =db.Column(db.DateTime)

  def __repr__(self):
    return '< Theatre %r >' % self.id

  def to_dist(self):
    return {
      "id": self.id,
      "name": self.name,
      "post_date": self.post_date
    }