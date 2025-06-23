from marshmallow import Schema, fields, validate

class ThemeUpdateSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(max=100))