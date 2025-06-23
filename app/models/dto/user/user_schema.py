from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=False, validate=validate.Length(max=50))
    last_name = fields.String(required=False, validate=validate.Length(max=50))
    role = fields.String(required=False, validate=validate.OneOf(['admin', 'user', 'participant']))
    active = fields.Boolean(required=False)
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6))