from marshmallow import Schema, fields, validate

class UserUpdateSchema(Schema):
    first_name = fields.String(required=False, validate=validate.Length(max=50))
    last_name = fields.String(required=False, validate=validate.Length(max=50))
    email = fields.Email(required=False)
    password = fields.String(required=False, validate=validate.Length(min=6))