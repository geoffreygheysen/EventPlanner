from marshmallow import Schema, fields, validate

class ThemeSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(max=100))