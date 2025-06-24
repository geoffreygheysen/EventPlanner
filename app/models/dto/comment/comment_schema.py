from marshmallow import fields, Schema

class CommentSchema(Schema):
    content = fields.String(required=True, validate=fields.Length(max=500))
    date_created = fields.DateTime(required=True)

    user_id = fields.Integer(required=True)
    event_id = fields.Integer(required=True)