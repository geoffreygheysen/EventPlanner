from marshmallow import fields, Schema, validate

class EventUpdateSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(max=100))
    location = fields.String(required=False, allow_none=True, validate=validate.Length(max=200))
    status = fields.String(required=True, validate=validate.OneOf(['scheduled', 'completed', 'cancelled']))
    date_start = fields.DateTime(required=True)
    date_end = fields.DateTime(required=True)