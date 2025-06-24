from marshmallow import fields, Schema, validate

class EventSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(max=100))
    location = fields.String(required=False, allow_none=True, validate=validate.Length(max=200))
    status = fields.String(required=True, validate=validate.OneOf(['scheduled', 'completed', 'cancelled']))
    date_start = fields.Date(required=True)
    date_end = fields.Date(required=True)

    user_id = fields.Integer(required=True)
    theme_id = fields.Integer(required=True)

    comments = fields.List(fields.Nested('CommentSchema', only=('id', 'content', 'date_created', 'user_id')), dump_only=True)
    
    