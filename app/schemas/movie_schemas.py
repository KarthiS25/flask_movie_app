from marshmallow import fields, Schema

class MovieSchema(Schema):
  title = fields.Str(required=True)
  release_date = fields.Date(required=True)
  post_date = fields.Date(required=True)

  class Meta:
    strict=True